This is a tutorial for integrating django with javascript. Here are the steps to achieve that:

1. Ensure that django.contrib.staticfiles is included in your INSTALLED_APPS1.

2. Define STATIC_URL in your settings file. For example:
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

3. In your templates, use the static template tag to build the URL for the given relative path using the configured staticfiles storage1. For example, if your JavaScript file is named my_script.js and is located in the static folder of your app (let’s say the app is named my_app), you can include it in your HTML file as follows:

{% load static %}
<script src="{% static 'my_app/my_script.js' %}"></script>
