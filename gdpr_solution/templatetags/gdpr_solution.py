import json
from django import template
from ..models import CookieScript, CookieConsentSettings
import re


register = template.Library()


@register.simple_tag(takes_context=True)
def gdpr_cookie_banner(context):
    t = template.loader.get_template('cookiebanner.html')
    data = {}
    data['cookie_scripts'] = CookieScript.objects.all()
    data['cookie_settings'] = CookieConsentSettings.objects.all().first()
    return t.render(data, request=context['request'])


@register.filter()
def regex_script(script, script_type):
    script = re.sub(r'(<script)', r'\1 type="text/plain" data-cookiecategory="' + script_type + r'"', script)
    return script
