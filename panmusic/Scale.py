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
            #Diatonic Modes
            "Ionian": IonianScale(root),
            "Dorian": DorianScale(root),
            "Phrygian": PhrygianScale(root),
            "Lydian": LydianScale(root),
            "Mixolydian": MixolydianScale(root),
            "Aeolian": AeolianScale(root),
            "Locrian": LocrianScale(root),

            #Melodic Modes
            "Melodic Minor": MelodicMinor(root),
            "Dorian b2": Dorianb2(root),
            "Lydian Augmented": LydianAugmented(root),
            "Lydian Dominant": LydianDominant(root),
            "Melodic Major": MelodicMajor(root),
            "Half Diminished": HalfDiminished(root),
            "Super Locrian": SuperLocrian(root),

            #Harmonic Series

            #Harmonic Major Modes
            "Harmonic Major": HarmonicMajor(root),
            "Dorian b5": Dorianb5(root),
            "Phrygian b4": Phrygianb4(root),
            "Lydian Diminished": LydianDiminished(root),
            "Mixolydian b2": Mixolydianb2(root),
            "Lydian Augmented Sharp 2": LydianAugmentedSharp2(root),
            "Locrian Diminished 7" : LocrianDiminished7(root),

            #Harmonic Minor Modes
            "Harmonic Minor": HarmonicMinor(root),
            "Locrian Sharp 6": LocrianSharp6(root),
            "Ionian Augmented": IonianAugmented(root),
            "Romainian": Romainian(root),
            "Phrygian Dominant": PhrygianDominant(root),
            "Lydian Sharp 2": LydianSharp2(root),
            "Ultra Locrian": UltraLocrian(root),


            "Double Harmonic Major": DoubleHarmonicMajor(root),
            
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

'''class DoubleHarmonicMajorScale(Heptatonic):
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

'''
    
    
    

"""The Modal Scales. Heptatonic. Diatonic."""
class IonianScale(Diatonic):
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

class DorianScale(Diatonic):
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

class PhrygianScale(Diatonic):
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

class LydianScale(Diatonic):
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

class MixolydianScale(Diatonic):
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

class AeolianScale(Diatonic):
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

class LocrianScale(Diatonic):
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
class MelodicMinorMode(Heptatonic):
    pass


class MelodicMinor(MelodicMinorMode):
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


        self.names = [
            "Melodic Minor",
            "Ascending Melodic Minor",
            "Jazz Melodic Minor Scale"
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()


class Dorianb2(MelodicMinorMode):
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
        self.names = [
            "Dorian b2",
            "Phrygian Natural 6",
            "Javanese",
            "Phrygidorian"
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class LydianAugmented(MelodicMinorMode):
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
        self.names = [
            "Lydian Augmented",
            "Lydian #5",
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class LydianDominant(MelodicMinorMode):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Lydian Dominant"
        self.root = root
        self.names = [
            "Lydian Dominant",
            "Lydian b7",
            "Acoustic",
            "Mixolydian #4",
            "Overtone",
            "Lydomyxian"
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class MelodicMajor(MelodicMinorMode):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Melodic Major"
        self.root = root
        self.names = [
            "Melodic Major",
            "Mixolydian b6",
            "Fifth Mode of Melodic Major",
            "Jazz Minor",
            "Myxaeolian",
            "Aeolian Dominant",
            "Mixolydian b13",
            "Hindu"
        ] 
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class HalfDiminished(MelodicMinorMode):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.DIMINISHED_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Half diminished"
        self.root = root
        self.names = [
            "Half Diminished",
            "Locrian Natural 2",
            "Aeolocrian",
            "Aeolian b5",
        ] 
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class SuperLocrian(MelodicMinorMode):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Super Locrian"
        self.root = root
        self.names = [
            "Super Locrian",
            "Altered",
            "Altered Dominant",
        ] 
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()




#Harmonic Series
class Harmonic(Heptatonic):
    pass



class HarmonicMajor(Harmonic):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Harmonic Major"
        self.root = root
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()


#Harmonic Major Modes
class HarmonicMajorMode(Harmonic):
    pass



#Harmonic Minor Modes
class HarmonicMinorMode(Harmonic):
    pass

#I
class HarmonicMajor(HarmonicMajorMode):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Harmonic Major"
        self.root = root
        self.names = [
            "Harmonic Major",
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class Dorianb5(HarmonicMajorMode):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.DIMINISHED_FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Dorian b5"
        self.root = root
        self.names = [
            "Dorian b5",
            "Locrian #2",
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class Phrygianb4(HarmonicMajorMode):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.MAJOR_THIRD,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Phrygian b4"
        self.root = root
        self.names = [
            "Phrygian b4",
            "Super Phrygian",
            "Super Locrian Natural 5",
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class LydianDiminished(HarmonicMajorMode):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Lydian Diminished"
        self.root = root
        self.names = [
            "Lydian Diminished",
            "Lydian Diminished 7",
            "Locrian bb7",
            
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class Mixolydianb2(HarmonicMajorMode):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Mixolydian b2"
        self.root = root
        self.names = [
            "Mixolydian b2",
            "Mixolydian b9",
            
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class LydianAugmentedSharp2(HarmonicMajorMode):
    intervals = [
        Interval.MINOR_THIRD,
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Lydian Augmented #2"
        self.root = root
        self.names = [
            "Lydian Augmented #2",
            "Lydian #2 #5",
            
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class LocrianDiminished7(HarmonicMajorMode):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.DIMINISHED_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SIXTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Locrian Diminished 7"
        self.root = root
        self.names = [
            "Locrian Diminished 7",
            "Locrian bb7",
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

#i
class HarmonicMinor(HarmonicMinorMode):
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
        self.names = [
            "Harmonic Minor",
            "Aeolian Major 7",
            "Aeolian Natural 7"
            "Melodic Minor b6",
            "Mohammedan"
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

''' '''
class LocrianSharp6(HarmonicMinorMode):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.DIMINISHED_FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Locrian #6"
        self.root = root
        self.names = [
            "Locrian #6",
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class IonianAugmented(HarmonicMinorMode):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Ionian Augmented"
        self.root = root
        self.names = [
            "Ionian Augmented",
            "Ionian #5",
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class Romainian(HarmonicMinorMode):
    intervals = [
        Interval.MAJOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Romainian"
        self.root = root
        self.names = [
            "Romainian",
            "Romanian Minor",
            "Ukranian Dorian",
            "Dorian #4",
            "Dorian #11",
            "Altered Dorian",
            "Misheberakh"
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

#V
class PhrygianDominant(HarmonicMinorMode):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MAJOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Phrygian Dominant"
        self.root = root
        self.names = [
            "Phrygian Dominant",
            "Phrygian Major",
            "Phrygian #3",
            "Mixolydian b2 b6",
            "Mixolydian b9 b13",
            "Spanish Gipsy",
            "Ahava Rabah"
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class LydianSharp2(HarmonicMinorMode):
    intervals = [
        Interval.MINOR_THIRD,
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.FIFTH,
        Interval.MAJOR_SIXTH,
        Interval.MAJOR_SEVENTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Lydian #2"
        self.root = root
        self.names = [
            "Lydian #2",
        ]
        self.generate_notes()
        self.add_triads()
        self.add_seventh_chords()

class UltraLocrian(HarmonicMinorMode):
    intervals = [
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MAJOR_SIXTH
    ]


    def __init__(self, root):
        self.name = root.__str__() + " Ultra Locrian"
        self.root = root
        self.names = [
            "Ultra Locrian",
            "Super Locrian bb7",
            "Super Locrian Diminished 7",
        ]
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
                
    