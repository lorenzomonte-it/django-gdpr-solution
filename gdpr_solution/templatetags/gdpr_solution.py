import json
from django import template
from ..models import CookieScript, CookieConsentSettings
import re


register = template.Library()


@register.simple_tag(takes_context=True)
def gdpr_cookie_banner(context):
    template_cookie = template.loader.get_template('cookiebanner.html')
    cookie_script = CookieScript.objects.all()
    data = {}
    data['cookie_script'] = cookie_script
    data['has_cookie_scripts_analytics'] = cookie_script.filter(cookie_type=1).exists()
    data['has_cookie_scripts_targeting'] = cookie_script.filter(cookie_type=2).exists()
    data['cookie_settings'] = CookieConsentSettings.objects.all().first()
    return template_cookie.render(data, request=context['request'])


@register.filter()
def regex_script(script, script_type):
    script = re.sub(r'(<script)', r'\1 type="text/plain" data-cookiecategory="' + script_type + r'"', script)
    return script
