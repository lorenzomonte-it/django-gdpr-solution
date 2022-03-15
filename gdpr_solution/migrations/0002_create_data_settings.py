# -*- coding: utf-8 -*-
from django.db import migrations


def create_data_settings(apps, schema_editor):
    # Get model
    CookieConsentSettings = apps.get_model("gdpr_solution.CookieConsentSettings")

    # Create a new cookie settings
    cookie_settings_object = CookieConsentSettings.objects.create(
        title_banner="Questo sito web utilizza i cookie",
        description_banner="Ciao, questo sito web utilizza cookie necessari per garantire il suo corretto funzionamento.",
        title_modal="Utilizzo dei cookie",
        description_modal="Usiamo i cookie per garantire le funzionalità di base del sito web e per migliorare la tua esperienza online. Puoi scegliere per ogni categoria cosa attivare e disattivare quando vuoi. Per ulteriori dettagli relativi ai cookie e ad altri dati sensibili, si prega di leggere la Privacy Policy e la Cookie Policy.",
        description_technical="",
        description_analytics="",
        description_marketing="",
        description_information="",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("gdpr_solution", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_data_settings, ),
    ]
