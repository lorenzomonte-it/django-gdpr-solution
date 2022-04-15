<h1 align="center" style="text-align: center;">Django GDPR solution</h1>
<div align="center" style="text-align: center;">

**[CookieConsent](https://github.com/orestbida/cookieconsent/)** integration for [Django](https://www.djangoproject.com/) Web Framework.

![PyPI](https://img.shields.io/pypi/v/django-gdpr-solution)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-gdpr-solution)
![PyPI - License](https://img.shields.io/pypi/l/django-gdpr-solution)

</div>

## 🚀️ Quick start

Install the package

```shell
pip install django-gdpr-solution
```

Add `gdpr_solution` on` INSTALLED_APPS`

```python
INSTALLED_APPS = [
  ...
  'gdpr_solution',
  ...
]
```

Include the urls

```python
urlpatterns = [
  ...
  path('django-gdpr-solution/', include('gdpr_solution.urls')),
  ...
]
```

`--> [OPTIONAL] Remember that you can change the name path of the url`

Complete the installation with migrations

```shell
python manage.py makemigrations
python manage.py migrate
```

Last step: load gdpr_solution and add templatetag on top of head tag on template

```html
{% load gdpr_solution %}

<head>
    ...
    {% gdpr_cookie_banner %}
    ...
</head>
```

---

## 📖 Dependencies

[CookieConsentJs](https://github.com/orestbida/cookieconsent/) repository (orestbida/cookieconsent) for gdpr compliant cookie consent.
For customize the cookie banner and all its functionality, go to the official repo.
