from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import register

import sys
sys.path.append("C:/Users/Rob/Django-Projects/mysite/panmusic/")
from Scale import *
from Note import *

# Create your views here.

#@register.filter
#def get_item(dictionary, key):
    #return dictionary.get(key)

def index(request):
    return render(request, 'scales/home.html',{'content': Scale.types })


def scale(request, scale_type):
    print(scale_type)
    scl = Scale.factory(scale_type, Note.E)
    the_triads = {}

    for note in scl.notes:
        triads_for_note_list = []
        for triad in scl.triads[note]:
            triads_for_note_list.append(triad)
            the_triads[note] = triads_for_note_list


    #return HttpResponse("HEY")
    return render(request, 'scales/scale.html',{'content': [scl.notes],'scale_name': scl.name, 'scale' : scl, 'the_triads': the_triads })