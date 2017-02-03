from Note import Note
from Chord import *

class Scale():
    notes = []
    name = "Scale"
    
    #def factory()

    def generate_notes(self):
        self.notes = [self.root]
        for interval in self.intervals:
            self.notes.append(self.root.plus(interval))
    
    def add_triads(self):
        self.triads = {}
        for note in self.notes:
            print ("\nChords for",note)
            self.triads[note] = self.generate_triads(note)
            
            
        print("\nTest:")
        for triad in self.triads[Note.E]:
            print(triad)
            
    def generate_triads(self, root):
        triads = []

        for triad in Triad:
            chord = Chord.factory(triad,root)
            if self.has_chord(chord):
                triads.append(chord)

        """Print debug"""
        for triad in triads:
            print(triad)
        return triads



    def has_chord(self, chord):
        return self.has_notes(chord.notes)

    def __str__(self):
        return self.name
   

    def has_notes(self, notes):
        for note in notes:
            if not self.has_note(note):
                return False
        return True
                
            
    def has_note(self, note):
        for scale_note in self.notes:
            if note == scale_note:
                return True
        return False
    
    
    
    
    
    
    

"""The Modal Scales. Heptatonic. Diatonic."""
class IonianScale(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Major (Ionian) Scale"
        print(self.name)
        self.root = root
        self.generate_notes()
        self.add_triads()

class DorianScale(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Dorian Scale"
        print(self.name)
        self.root = root
        self.generate_notes()
        self.add_triads()

class PhrygianScale(Scale):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Phrygian Scale"
        print(self.name)
        self.root = root
        self.generate_notes()
        self.add_triads()

class LydianScale(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Lydian Scale"
        print(self.name)
        self.root = root
        self.generate_notes()
        self.add_triads()

class MixolydianScale(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Mixolydian Scale"
        print(self.name)
        self.root = root
        self.generate_notes()
        self.add_triads()

class AeolianScale(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Aeolian (Natural Minor) Scale"
        print(self.name)
        self.root = root
        self.generate_notes()
        self.add_triads()

class LocrianScale(Scale):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.DIMINISHED_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Locrian Scale"
        print(self.name)
        self.root = root
        self.generate_notes()
        self.add_triads()
        
        


        
        
scl = PhrygianScale(Note.E)
print(PhrygianScale(Note.E).notes)
print("SDFFFFFFFF")
print(PhrygianScale(Note.E).notes)

print(MajorChord(Note.E).notes)
print(MajorChord(Note.E).notes)
print(MajorChord(Note.E).notes)
#print(PhrygianScale(Note.E).triads)


scl = LocrianScale(Note.B)
print(LocrianScale(Note.B).notes)
#print(scl)
#print(scl.hasTriad(Note.F, Triad.FLAT_FIFTH))

#for note in scl.notes:
#    print("CHORDS FOR NOTE: " + note.__str__())
#    print(scl.triads[note])
#print(scl.triads)
#print(scl.notes)

#print(scl.hasNotes(MajorChord(Note.F).notes))
#print(MajorChord(Note.F).notes)
#print(MajorChord(Note.F).notes)
#print(MajorChord(Note.F).notes)

#chr = MajorChord(Note.F)
#print(chr.notes)
#print(MajorChord(Note.F).notes)
#print(MajorChord(Note.F).notes)

#chrs = MajorChord(Note.F)
#print(chrs.notes)
#MajorChord(Note.F)
#chr = MajorChord(Note.F)
#print(chr.notes)


#print("sdf")
#hat = Chord.factory(Triad.MAJOR, Note.E)
#print(hat.notes)
                
    