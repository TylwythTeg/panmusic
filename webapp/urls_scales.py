from django.conf.urls import url
from . import views
from Scale import *

urlpatterns = [
    url(r'^$', views.index_scales, name='index_scales'),
    url(r'^(?P<scale_type>[\w|\W]+)/', views.scale, name = 'scale'),
    #url(r'^(?P<chord_type>[\w|\W]+)/$', views.chord, name = 'chord')
    
]