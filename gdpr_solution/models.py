from django.db import models
from .app_config import COOKIEBANNER_IS_WAGTAIL_PROJECT, DJANGO_VERSION_LESS_THAN_2

if DJANGO_VERSION_LESS_THAN_2:
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _

if COOKIEBANNER_IS_WAGTAIL_PROJECT:
    from wagtail.core.fields import RichTextField
    from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, HelpPanel


COOKIE_TYPE_CHOICE = (
    (0, _('Tecnici/Necessari')),
    (1, _('Statistiche')),
    (2, _('Marketing')),
)


class CookieScript(models.Model):
    cookie_name = models.CharField(_("Nome"), max_length=200)
    cookie_type = models.IntegerField(_("Tipologia"), choices=COOKIE_TYPE_CHOICE, default=1)
    cookie_script = models.TextField(_("Script JS"))

    def __str__(self):
        return self.cookie_name

    class Meta:
        verbose_name_plural = "Cookie Scripts"
        ordering = ['cookie_type', ]


class CookieConsentLog(models.Model):
    consent_token = models.CharField(_("Chiave consenso"), max_length=50, unique=True)
    consent_url = models.URLField(_("Consenso Cookie Url"), max_length=200)
    consent_date_time = models.DateTimeField(_("Data e Ora"), auto_now=False, auto_now_add=True, editable=False)
    consent_user_agent = models.TextField(_("User Agent"))
    consent_anonymize_ip = models.CharField(_("IP Anonymize"), max_length=20)
    consent_cookie = models.TextField(_("Lista cookie accettati"))

    def __str__(self):
        return self.consent_token

    class Meta:
        verbose_name_plural = "Cookie Log"
        ordering = ['-consent_date_time', ]


class CookieConsentSettings(models.Model):
    title_banner = models.CharField(_("Titolo banner"), max_length=255, blank=True)
    title_modal = models.CharField(_("Titolo modal"), max_length=255, blank=True)

    if COOKIEBANNER_IS_WAGTAIL_PROJECT:
        description_banner = RichTextField(_("Descrizione banner"), features=['link'], blank=True)
        description_modal = RichTextField(_("Descrizione modal"), features=['link'], blank=True)
        description_technical = RichTextField(_("Descrizione cookie tecnici"), features=['bold', 'link'], blank=True)
        description_analytics = RichTextField(_("Descrizione cookie statistici"), features=['bold', 'link'], blank=True)
        description_marketing = RichTextField(_("Descrizione cookie marketing"), features=['bold', 'link'], blank=True)
        description_information = RichTextField(_("Maggiori informazioni"), features=['bold', 'link'], blank=True)
    else:
        description_banner = models.TextField(_("Descrizione banner"), blank=True)
        description_modal = models.TextField(_("Descrizione modal"), blank=True)
        description_technical = models.TextField(_("Descrizione  cookie tecnici"), blank=True)
        description_analytics = models.TextField(_("Descrizione  cookie statistici"), blank=True)
        description_marketing = models.TextField(_("Descrizione cookie marketing"), blank=True)
        description_information = models.TextField(_("Maggiori informazioni"), blank=True)

    layout_banner = models.CharField(_("Layout banner"), max_length=255, choices=(('box', 'Box'), ('cloud', 'Cloud'), ('bar', 'Bar')), default='box')
    position_y_banner = models.CharField(_("Posizione Y banner"), max_length=255, choices=(('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom')), default='bottom')
    position_x_banner = models.CharField(_("Posizione X banner"), max_length=255, choices=(('left', 'Left'), ('center', 'Center'), ('right', 'Right')), default='left')
    layout_modal = models.CharField(_("Layout modal"), max_length=255, choices=(('box', 'Box'), ('bar', 'Bar')), default='box')
    position_modal = models.CharField(_("Posizione modal"), max_length=255, choices=(('left', 'Left'), ('right', 'Right')), default='left')

    banner_is_active = models.BooleanField(_("Attivare il banner?"), default=True)
    revision_banner = models.IntegerField(default=0)

    if COOKIEBANNER_IS_WAGTAIL_PROJECT:
        panels = [
            HelpPanel(content='<div class="help-block help-info"><p>Attenzione: ogni volta che questa pagna viene salvata, aumenta il numero di revisioni del banner, e all\'utente verrà rimostrato il banner per acconsentire alla nuova versione dei cookie</p></div>'),
            MultiFieldPanel([
                FieldPanel("title_banner"),
                FieldPanel("description_banner"),
                FieldPanel("layout_banner"),
                FieldPanel("position_y_banner"),
                FieldPanel("position_x_banner"),
            ], heading="Banner"),
            MultiFieldPanel([
                FieldPanel("title_modal"),
                FieldPanel("description_modal"),
                FieldPanel("layout_modal"),
                FieldPanel("position_modal"),
            ], heading="Modal"),
            MultiFieldPanel([
                FieldPanel("description_technical"),
                FieldPanel("description_analytics"),
                FieldPanel("description_marketing"),
            ], heading="Descrizione cookie"),
            FieldPanel('description_information'),
            MultiFieldPanel([
                HelpPanel(content="<ul style='margin-left:12px;margin-top:-40px;margin-bottom:-24px;'><li style='list-style-type:square;'>Attivando il banner hai la possibilità di gestire il consenso di tutti i cookie;</li><li style='list-style-type:square;'>Se invece disattivi il banner, verranno mostrati solo i cookie tecnici/necessari, mostrando all'utente solo il banner informativo.</li></ul>"),
                FieldPanel("banner_is_active"),
            ], heading="Modalità di utilizzo"),
        ]

    def save(self, *args, **kwargs):
        self.revision_banner = self.revision_banner + 1
        if DJANGO_VERSION_LESS_THAN_2:
            super(CookieConsentSettings, self).save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return 'Settings'

    class Meta:
        verbose_name_plural = "Cookie settings"
