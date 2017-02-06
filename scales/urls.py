from django.conf.urls import url
from . import views
from Scale import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^Dorian/', views.dorian, name='dorian'),
    url(r'^(?P<scale_type>\w+)/', views.scale, name = 'scale')
    #url(r'^scales/', include('scales.urls')),
    
]