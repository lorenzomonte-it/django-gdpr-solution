import django
from pkg_resources import parse_version

try:
    from wagtail import __version__ as WAGTAIL_VERSION
except ImportError:
    WAGTAIL_VERSION = False


DJANGO_VERSION_LESS_THAN_2 = False
if parse_version(django.get_version()) < parse_version('2.0.0'):
    DJANGO_VERSION_LESS_THAN_2 = True


COOKIEBANNER_IS_WAGTAIL_PROJECT = False
if WAGTAIL_VERSION and parse_version(WAGTAIL_VERSION) >= parse_version('2.0.2'):
    COOKIEBANNER_IS_WAGTAIL_PROJECT = True
