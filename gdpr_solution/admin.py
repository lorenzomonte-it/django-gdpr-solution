from django.contrib import admin
from .models import CookieConsentLog, CookieConsentSettings, CookieScript
from .app_config import DJANGO_VERSION_LESS_THAN_2

if DJANGO_VERSION_LESS_THAN_2:
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


@admin.register(CookieScript)
class CookieScriptAdmin(admin.ModelAdmin):
    list_display = ('cookie_name', 'cookie_type', 'cookie_script')


@admin.register(CookieConsentSettings)
class CookieConsentSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (),
            'description': "<h2>Attenzione: ogni volta che questa pagna viene salvata, aumenta il numero di revisioni del banner, e all\'utente verrà rimostrato il banner per acconsentire alla nuova versione dei cookie</h2>"
        }),
        ("Banner", {
            'fields': ('title_banner', 'description_banner', 'layout_banner', 'position_y_banner', 'position_x_banner')
        }),
        ("Modal", {
            'fields': ('title_modal', 'description_modal', 'layout_modal', 'position_modal')
        }),
        ("Descrizione cookie", {
            'fields': ('description_technical', 'description_analytics', 'description_marketing')
        }),
        ("Altro", {
            'fields': ('description_information', )
        }),
        (None, {
            'fields': ('banner_is_active',),
            'description': "<h2>Modalità di utilizzo: <ul style='margin-left:12px;'><li style='list-style-type:square;'>Attivando il banner hai la possibilità di gestire il consenso di tutti i cookie;</li><li style='list-style-type:square;'>Se invece disattivi il banner, verranno mostrati solo i cookie tecnici/necessari, mostrando all'utente solo il banner informativo.</li></ul></h2>"
        }),
    )
    # list_display = ()
    # search_fields = []

    def has_add_permission(self, request):
        if DJANGO_VERSION_LESS_THAN_2:
            return False if self.model.objects.count() > 0 else super(CookieConsentSettingsAdmin, self).has_add_permission(request)
        else:
            return False if self.model.objects.count() > 0 else super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CookieConsentLog)
class CookieConsentLogAdmin(admin.ModelAdmin):
    list_display = ('consent_date_time', 'consent_token', 'consent_url', 'consent_cookie')
    search_fields = ['consent_token', 'consent_date_time']

    def has_add_permission(self, request):
        return False

    if not DJANGO_VERSION_LESS_THAN_2:
        def has_change_permission(self, request, obj=None):
            return False

    def has_delete_permission(self, request, obj=None):
        return False
