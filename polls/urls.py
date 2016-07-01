from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^inicio/$', views.inicio, name='inicio'),
        url(r'^login/$', views.login, name='login'),
        #url(r'^login?next=(?P<next>\w+)$', views.login, 'login_redirect'),
        url(r'^registro/$', views.registro, name='registro'),
        url(r'^logout/$', views.logout, name = 'logout'),
    ]
