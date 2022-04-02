from .app_config import COOKIEBANNER_IS_WAGTAIL_PROJECT


if COOKIEBANNER_IS_WAGTAIL_PROJECT:
    from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
    from wagtail.contrib.modeladmin.helpers import PermissionHelper
    from .models import CookieConsentLog, CookieScript, CookieConsentSettings
    import datetime

    class CookieConsentLogValidationPermissionHelper(PermissionHelper):
        def user_can_list(self, user):
            return True

        def user_can_create(self, user):
            return False

        def user_can_edit_obj(self, user, obj):
            return False

        def user_can_delete_obj(self, user, obj):
            return False

    class CookieConsentSettingsValidationPermissionHelper(PermissionHelper):
        def user_can_list(self, user):
            return True

        def user_can_create(self, user):
            return False if self.model.objects.count() > 0 else True

        def user_can_delete_obj(self, user, obj):
            return False

    class CookieConsentLogAdmin(ModelAdmin):
        model = CookieConsentLog
        permission_helper_class = CookieConsentLogValidationPermissionHelper
        inspect_view_enabled = True
        menu_label = "Cookie log"
        menu_icon = "pick"
        exclude_from_explorer = False
        list_export = ('consent_date_time', 'consent_token', 'consent_url', 'consent_user_agent', 'consent_anonymize_ip')
        export_filename = 'Cookie_Consent_Log_' + str(datetime.datetime.now())
        list_display = ('consent_date_time', 'consent_token', 'consent_url', 'consent_anonymize_ip')
        search_fields = ['consent_token', 'consent_date_time']

    class CookieScriptAdmin(ModelAdmin):
        model = CookieScript
        list_display = ('cookie_name', 'cookie_type', 'cookie_script')

    class CookieConsentSettingsAdmin(ModelAdmin):
        model = CookieConsentSettings
        permission_helper_class = CookieConsentSettingsValidationPermissionHelper
        menu_label = "Cookie settings"
        menu_icon = "cog"
        # list_display = ('campo',)

    class GdprSolutionGroup(ModelAdminGroup):
        menu_label = 'GDPR Solution'
        menu_icon = 'pick'
        menu_order = 1000
        items = (CookieScriptAdmin, CookieConsentLogAdmin, CookieConsentSettingsAdmin)

    modeladmin_register(GdprSolutionGroup)
