from django.conf.urls import url

from . import views


app_name = 'notary'

urlpatterns = [
    url(r'^notary/thanks/$', views.thanks, name='thanks'),
    url(r'^$', views.get_name, name='get_name'),
    url(r'^$', views.index, name='index'),
]
