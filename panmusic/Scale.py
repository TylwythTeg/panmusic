from Note import Note
from Chord import *
import sys
import json

class Scale():
    notes = []
    name = "Scale"

    types = [
        ("Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian (Natural Minor)", "Locrian",
            "Melodic Minor", "Dorian b2", "Lydian Augmented")
    ]
    
    def factory(type = None, root = None):
        def all():
            return type is None and root is None




        types = {
            #Diatonic Modes
            "Ionian": IonianScale,
            "Dorian": DorianScale,
            "Phrygian": PhrygianScale,
            "Lydian": LydianScale,
            "Mixolydian": MixolydianScale,
            "Aeolian": AeolianScale,
            "Locrian": LocrianScale,

            #Melodic Modes
            "Melodic Minor": MelodicMinor,
            "Dorian b2": Dorianb2,
            "Lydian Augmented": LydianAugmented,
            "Lydian Dominant": LydianDominant,
            "Melodic Major": MelodicMajor,
            "Half Diminished": HalfDiminished,
            "Super Locrian": SuperLocrian,

            #Harmonic Series

            #Harmonic Major Modes
            "Harmonic Major": HarmonicMajor,
            "Dorian b5": Dorianb5,
            "Phrygian b4": Phrygianb4,
            "Lydian Diminished": LydianDiminished,
            "Mixolydian b2": Mixolydianb2,
            "Lydian Augmented Sharp 2": LydianAugmentedSharp2,
            "Locrian Diminished 7" : LocrianDiminished7,

            #Harmonic Minor Modes
            "Harmonic Minor": HarmonicMinor,
            "Locrian Sharp 6": LocrianSharp6,
            "Ionian Augmented": IonianAugmented,
            "Romainian": Romainian,
            "Phrygian Dominant": PhrygianDominant,
            "Lydian Sharp 2": LydianSharp2,
            "Ultra Locrian": UltraLocrian,

            #Double Harmonic Major Modes
            "Double Harmonic Major": DoubleHarmonicMajor,
            #"Lydian #2 #6": LydianSharp2Sharp6,
            #"UltraPhrygian": UltraPhrygian,
            #"Hungarian Minor": HungarianMinor,
            #"Oriental": Oriental,
            #"Ionian Augmented 2": IonianAugmented2,
            #"Locrian bb3 bb7": Locrianbb3bb7,

            
            "Custom Scale": CustomScale
        }

        if all():
            return types

        constructor = types.get(type)
        return constructor(root)
        #return types.get(type)

    ###############Dict stuff ####################
    def as_dict(self):
        #check if or set before


        scale_dict = {}

        scale_dict["root"] = self.root.__str__()
        scale_dict["notes"] = list(map(str,self.notes))
        scale_dict["intervals"] = list(map(str, self.intervals))
        scale_dict["interval_dict"] = self.interval_dict()
        scale_dict["triads"] = self.triads_dict()


        #scale_dict["intervals"] = list(map(int, scale.intervals))

        print("\n \n \n ", scale_dict)
        print(list(map(str,self.notes)))
        #print("\n \n \t ", scale_dict)
        print("\n size:", sys.getsizeof(scale_dict))
        print(scale_dict["triads"])
        print("\n intervals",scale_dict["intervals"])
        print("\n int_dict",scale_dict["interval_dict"])

        return scale_dict

    def triads_dict(self):
        dict = {}
        for root,triads in self.triads.items():
            dict[root.__str__()] = json.dumps(list(map(Chord.as_dict,triads)))
            print("\n \t ", list(map(str,triads)))
        return dict
    ############### Dict stuff ####################



    ############### Fingerprints ####################
    def set_fingerprint(self):
        self.fingerprint = frozenset(self.notes)

    #global / static
    #add a chord to the Chord.fingerprints dictionary
    #Note: looks like I can reuse this for Scale objects
    def add_to_fingerprints(scale):
        if scale.fingerprint not in Scale.fingerprints:
            Scale.fingerprints[scale.fingerprint] = [chord]
        else:
            Scale.fingerprints[scale.fingerprint].append(scale)


    #global / static 
    #Group all chords under fingerprints under Chord.fingerprints
    def set_fingerprints():
        Scale.fingerprints = {}

        scales = Scale.factory()

        for key,scale in scales.items():
            Scale.add_to_fingerprints(scale)

    def all():
        for scale in Scale.factory():
            print("hey")
    ############### Fingerprints ####################







    ############## Notes ##############
    def generate_notes(self):

        
        self.notes = [self.root]
        for interval in self.intervals:
            self.notes.append(self.root + interval)


    ############## Triads ##############
    def generate_triads(self, root):

        self.set_fingerprint()
        
        triads = []

        for triad in Triad.types:
            chord = Triad.create(triad = triad,root = root)
            if self.has_chord(chord):
                triads.append(chord)
                
        return triads
    
    def add_triads(self):
        self.triads = {}
        for note in self.notes:
            self.triads[note] = self.generate_triads(note)
            #self.triads[note] = Triad.generate_triads(note, self)


    ############## Tetrads ##############
    def chords_in_scale(self, chords):
        for chord in chords:
            if self.has_chord(chord):
                yield chord

    def add_tetrad(self, tetrad):
        triad = tetrad.triad
        #if key doesn't exist, initialize first tetrad within a new list
        if triad not in self.tetrads:
            self.tetrads[triad] = [tetrad]
        #else append to current list of tetrad(s)
        else:
            self.tetrads[triad].append(tetrad)

    def generate_tetrads(self):
        self.tetrads = {}

        #gives us all tetrads from roots that we need to filter
        tetrads = Tetrad.from_notes(self.notes)

        # use a generator to filter away all tetrads that don't exist in this scale
        for tetrad in self.chords_in_scale(tetrads):
            self.add_tetrad(tetrad)
            
                

    



            
        
            


    def get_triads(self, note):
        return self.triads[note]

    def has_chord(self, chord):
        return self.has_notes(chord.notes)

    def __str__(self):
        return self.name
   

    def has_notes(self, notes):
        return set(self.notes) >= set(notes)
                
            
    def has_note(self, note):
        #print("\n \n \n \n \n \n YESSS print it:", self, note, note in self.notes)
        return note in self.notes
    



#These are the types, direct children of Scale, as Chord they are based on # of notes
class Heptatonic(Scale):
    # for matching a note to an interval in regards to the scale, with dictionary
    def interval_dict(self):
        
        notes = map(str, self.notes[1:])
        intervals =  map (str, self.intervals)

        dictionary = dict(zip(notes, intervals ))
        print(" \n \n \t \t HEY ", dictionary)
        return dictionary



class Diatonic(Heptatonic):
    pass
    
    

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
        self.generate_tetrads()
        print("--------------",self.tetrads)

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()
        


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
        self.generate_tetrads()


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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()




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
        self.generate_tetrads()


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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()

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
        self.generate_tetrads()




####################
class DoubleHarmonicMajor(Heptatonic):
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
        self.generate_tetrads()




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
        self.generate_tetrads()


        


        
        
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
                
    