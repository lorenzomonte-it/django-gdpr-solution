# django-gdpr-solution


### 📖 Dependencies
[CookieConsentJs](https://github.com/orestbida/cookieconsent/tree/v2.8.0) repository (orestbida/cookieconsent) for gdpr compliant cookie consent.
For customize the cookie banner and all its functionality, go to the official repo.

------------------

## 🚀️ Installation
- Install app with pip
```console
$ pip install django-gdpr-solution
```


- Add app on INSTALLED APPS
```bash
INSTALLED_APPS = [
    ...
    'gdpr_solution',
    ...
]
```


- Include urls of app 
```bash
urlpatterns = [
    ...
    path('django-gdpr-solution/', include('gdpr_solution.urls')),
    ...
]
```
`--> [OPTIONAL] You can change the name path of the url`


- Complete the installation with migrations
```console
$ ./manage.py makemigrations
$ ./manage.py migrate
```


- Last step is to load gdpr_solution and add templatetag on top of head tag on template
```
{% load gdpr_solution %}

<head>
    {% gdpr_cookie_banner %}
    ...
    ...
</head>
```