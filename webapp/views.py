from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import register

import sys
sys.path.append("C:/Users/Rob/Django-Projects/mysite/panmusic/")
from Scale import *
from Note import *
from Chord import *

# Create your views here.

#@register.filterf
#def get_item(dictionary, key):
    #return dictionary.get(key)

def index_scales(request):
    return render(request, 'chordscales/home_scales.html',{'content': Scale.types })

def index_chords(request):
    return render(request, 'chordscales/home_chords.html',{'content': Chord.triad_types })


def scale(request, scale_type):
    print(scale_type)
    scl = Scale.factory(scale_type, Note.E)

    return render(request, 'chordscales/scale.html',{'content': scl.notes,'scale_name': scl.name, 'scale' : scl, 'the_triads': scl.triads })

def chord(request, chord_type):
    chr = Chord.factory(Triad.from_string(chord_type), Note.E)
    print(chr.notes)
    return render(request,'chordscales/chord.html', {'chord': chr } )