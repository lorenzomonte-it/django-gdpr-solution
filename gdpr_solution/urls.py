from django.urls import path
from .views import CookieCreateView, DjangoExportView

urlpatterns = [
    path('create-cookie/', CookieCreateView.as_view(), name='create_cookie_view'),
    path('export-django/', DjangoExportView.as_view(), name='export_django'),
]
