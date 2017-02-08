from django.conf.urls import url
from . import views
from Scale import *

urlpatterns = [
    url(r'^$', views.index_chords, name='index_chords'),
    url(r'^(?P<chord_type>\w+)/$', views.chord, name = 'chord')
    
]