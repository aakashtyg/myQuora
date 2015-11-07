"""myQuora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'account.views.login', name = 'login'),
    url(r'^account/', include('account.urls')),
    url(r'^question/', include('question.urls')),
    url(r'^home/$', 'account.views.home', name = 'home'),
    url(r'^signup/$', 'account.views.signup', name = 'signup'),
    url(r'^addquestion/$', 'question.views.addQuestion', name = 'addquestion'),
] + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# +..... added to serve media files