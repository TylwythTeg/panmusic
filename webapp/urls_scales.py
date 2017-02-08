from django.conf.urls import url
from . import views
from Scale import *

urlpatterns = [
    url(r'^$', views.index_scales, name='index_scales'),
    url(r'^(?P<scale_type>\w+)/', views.scale, name = 'scale')
    
]