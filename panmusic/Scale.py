from Note import Note
from Chord import *

class Scale():
    notes = []
    name = "Scale"

    types = [
        ("Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian (Natural Minor)", "Locrian",
            "Melodic Minor", "Dorian b2", "Lydian Augmented")
    ]
    
    def factory(type, root):
        types = {
            "Ionian": IonianScale(root),
            "Dorian": DorianScale(root),
            "Phrygian": PhrygianScale(root),
            "Lydian": LydianScale(root),
            "Mixolydian": MixolydianScale(root),
            "Aeolian": AeolianScale(root),
            "Locrian": LocrianScale(root),

            "Melodic Minor": MelodicMinor(root),
            "Dorian b2": Dorianb2(root),
            "Lydian Augmented": LydianAugmented(root),

            "Double Harmonic Major": DoubleHarmonicMajor(root),
            "Harmonic Minor": HarmonicMinor(root),
            "Custom Scale": CustomScale(root)
        }
        return types.get(type)

    def generate_notes(self):
        self.notes = [self.root]
        for interval in self.intervals:
            self.notes.append(self.root.plus(interval))
    
    def add_triads(self):
        self.triads = {}
        for note in self.notes:
            print ("\nChords for",note)
            self.triads[note] = self.generate_triads(note)


    def add_seventh_chords(self):
        self.seven_chords = {}

        for triads in self.triads.values():
            for triad in triads:
                print("Seven chords for", triad)
                self.seven_chords[triad] = self.generate_seven_chords(triad.type, triad.root)



        #for triad in self.triads.values():
        #    print("Seven chords for", triad)
        #    self.seven_chords[triad] = self.generate_seven_chords(triad, triad.root)


    def generate_seven_chords(self, triad, root):
        seven_chords = []

        print("Checking note: ", root)


        for seven_chord in SeventhChord.types:
            print("----------------",triad,seven_chord)


            #if minor triad/major sixth e.g. Cm6 and etc
            #This is really sloppy but just trying to get this working
            if triad != "Diminished" and seven_chord == "Diminished Seven":
                continue
            elif triad == "Flat Five" and seven_chord == "Major Seven":
                continue

            #chord = Chord.create(seven_chord, root, triad)
            chord = Chord.create(
                root = root,
                triad = triad,
                tetrad = seven_chord
            )
            if self.has_chord(chord):
                seven_chords.append(chord)
                print(self, " has Chord: ", chord)
                print("------------- Notes: ", chord.notes)

        for seven_chord in seven_chords:
            print("SEVEN:    ",seven_chord)

        return seven_chords
            
            
        
            
    def generate_triads(self, root):
        triads = []

        for triad in Triad.types:
            chord = Triad.create(triad = triad,root = root)
            if self.has_chord(chord):
                triads.append(chord)

        """Print debug"""
        #for triad in triads:
            #print(triad)
        return triads

    def get_triads(self, note):
        return self.triads[note]

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
    
    



    #These are the types, direct children of Scale, as Chord they are based on # of notes
class Heptatonic(Scale):
    pass

class Diatonic(Heptatonic):
    pass

class DoubleHarmonic(Heptatonic):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Harmonic Major Scale"
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class DoubleHarmonic(Heptatonic):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]

    names = [
        "Double Harmonic",
        "Double Harmonic Major"
    ]



    def __init__(self, root):
        self.name = root.__str__() + " Harmonic Major Scale"
        self.root = root




        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()


    
    
    

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
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

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
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

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
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

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
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

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
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

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
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

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
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()
        

#Melodic minor modes
class MelodicMinor(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Melodic Minor"
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class Dorianb2(Scale):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Dorian b2"
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class LydianAugmented(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Lydian Augmented"
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()




####################
class DoubleHarmonicMajor(Scale):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Double Harmonic Major"
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class HarmonicMinor(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Harmonic Minor"
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()


class CustomScale(Scale):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH

    ]


    def __init__(self, root):
        self.name = root.__str__() + " Harmonic Minor"
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()


        


        
        
#scl = PhrygianScale(Note.E)
#print(PhrygianScale(Note.E).notes)
#print("SDFFFFFFFF")
#print(PhrygianScale(Note.E).notes)

#print(MajorChord(Note.E).notes)
#print(MajorChord(Note.E).notes)
#print(MajorChord(Note.E).notes)
#print(PhrygianScale(Note.E).triads)


#scl = LocrianScale(Note.B)
#print(LocrianScale(Note.B).notes)
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
                
    