from wagtail import __version__ as WAGTAIL_VERSION
from pkg_resources import parse_version


COOKIEBANNER_IS_WAGTAIL_PROJECT = False
if WAGTAIL_VERSION and parse_version(WAGTAIL_VERSION) >= parse_version('1.13.4'):
    COOKIEBANNER_IS_WAGTAIL_PROJECT = True
