from .views import CookieCreateView, DjangoExportView
from .app_config import DJANGO_VERSION_LESS_THAN_2


if DJANGO_VERSION_LESS_THAN_2:
    from django.conf.urls import url
else:
    from django.urls import path


if DJANGO_VERSION_LESS_THAN_2:
    urlpatterns = [
        url(r'^create-cookie/', CookieCreateView.as_view(), name='create_cookie_view'),
        url(r'^export-django/', DjangoExportView.as_view(), name='export_django'),
    ]
else:
    urlpatterns = [
        path('create-cookie/', CookieCreateView.as_view(), name='create_cookie_view'),
        path('export-django/', DjangoExportView.as_view(), name='export_django'),
    ]
