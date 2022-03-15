from django.views import View
from django.http.response import JsonResponse
from django.http import HttpResponse

import string
import secrets
import datetime
import csv

from .models import CookieConsentLog


# Create your views here.
class CookieCreateView(View):
    def post(self, request, **kwargs):
        if request.is_ajax():
            cookie_preferences = request.POST.get('user_preferences')
            cookie_from_url = request.POST.get('request_url')

            # Anonymize the IP Address by hidden last group
            consent_anonymize_ip = None
            if request.META.get('HTTP_X_FORWARDED_FOR'):
                consent_anonymize_ip = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
            else:
                consent_anonymize_ip = request.META.get('REMOTE_ADDR')
            ca_ip = consent_anonymize_ip.split('.')
            consent_anonymize_ip = f'{ca_ip[0]}.{ca_ip[1]}.{ca_ip[2]}.0'

            cookie_model_obj = CookieConsentLog()
            cookie_model_obj.consent_token = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(35)) + '=' + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
            cookie_model_obj.consent_url = cookie_from_url
            cookie_model_obj.consent_user_agent = request.META['HTTP_USER_AGENT']
            cookie_model_obj.consent_anonymize_ip = consent_anonymize_ip
            cookie_model_obj.consent_cookie = cookie_preferences
            cookie_model_obj.save()

            data = {'consent_token': cookie_model_obj.consent_token}

            response = JsonResponse(data, safe=False)
            return response


class DjangoExportView(View):
    def get(self, request, **kwargs):
        model_obj = CookieConsentLog.objects.all().first()._meta.fields
        field_names = [field.name for field in model_obj]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=Cookie_Consent_Log-{datetime.datetime.now()}.csv'

        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in CookieConsentLog.objects.all():
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response