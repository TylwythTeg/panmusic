from Note import *
from enum import Enum

#import itertools
#this is some helper stuff that needs a home
#This might actually not be essential at all, but I'll see. Not really "using" it right now
def combinations(array):
    #Gets combinations by iterating through list.
    #For every element, it creates a new list and adds the rest of the elements on top
    #This list of lists is returned as combinations
    combinations = []
    for element in array:
        temp_array = [element]
        for temp_element in array:
            if temp_element != element:
                temp_array.append(temp_element)
        combinations.append(temp_array)

    return combinations 
#this is some helper stuff that needs a home



class Chord():
    name = None
    notes = []
    tetrad = None
    triad = None
    root = None


    #so that we can use chords as dictionary keys.
    #I guess this makes them immutable
    #Change notes to a frozenset rather than a list?
    def __eq__(self, other):
        #if a root isn't established, then we need to compare notes
        if self.root is None or other.root is None:
            return frozenset(self.notes) == frozenset(self.notes)
        #root established, so check other established info against eachother
        else:
            return (self.root == other.root
                and frozenset(self.notes) == frozenset(other.notes)
                and self.name == other.name
                and self.type == other.type)

    def __hash__(self):
        return hash((self.root, tuple(self.notes), self.name, self.type))






    #############
    def all():
        triads = Triad.create(root = "All", triad = "All")
        tetrads = Tetrad.create(root = "All", tetrad = "All")

        return triads + tetrads







    def set_fingerprint(self):
        self.fingerprint = frozenset(self.notes)

    #global / static
    #add a chord to the Chord.fingerprints dictionary
    #Note: looks like I can reuse this for Scale objects
    def add_to_fingerprints(chord):
        if chord.fingerprint not in Chord.fingerprints:
            Chord.fingerprints[chord.fingerprint] = [chord]
        else:
            Chord.fingerprints[chord.fingerprint].append(chord)


    #global / static 
    #Group all chords under fingerprints under Chord.fingerprints
    def set_fingerprints():
        Chord.fingerprints = {}

        chords = Chord.all()

        for chord in chords:
            Chord.add_to_fingerprints(chord)

        #print("--------------FINGERPRINTS",Chord.fingerprints,"____________________")
    

    def __init__(self, notes , root = None):
        self.notes = []

        for note in notes:
            self.notes.append(note)

        if root is not None:
            self.root = root

        self.set_fingerprint()

    def generate_notes(self):
        self.notes = [self.root]
        for interval in self.intervals:
            self.notes.append(self.root.plus(interval))
        

    def generate_inversions(self):
         self.inversions = combinations(self.notes)

    #I don't know what use this could ever really be yet
    def generate_inversion_intervals(self):
        self.inversion_intervals = []

        first = True
        for inversion in self.inversions:
            if first:
                last_inversion = inversion
                first = False
                continue

            ch = Chord(inversion)
            inters = ch.calculate_intervals()

            inters = frozenset(inters)

            self.inversion_intervals.append(inters)

        self.inversion_intervals = frozenset(self.inversion_intervals)

    def create(root = None, triad = None, tetrad = None ):

        if tetrad is None:
            return Triad.create(root = root, triad = triad)
        else:    
            return Tetrad.create(tetrad = tetrad,triad = triad,root = root)


    def calculate_intervals(self):
        intervals = []

        first = True
        for note in self.notes:
            if first == True:
                last_note = note
                first = False
                
                continue

            interval = Interval.between(self.notes[0], note)
            intervals.append(interval)
            last_note = note
        return intervals

        
    def __str__(self):
        return self.name

    
            

class Triad(Chord):
    types = [
        "Major",
        "Minor",
        "Suspended Two",
        "Suspended Four",
        "Diminished",
        "Augmented",
        "Flat Five"
    ]

    '''
    def liste(root = None, triad = None):
        def notes(root):
            return isinstance(root, list)
        def root(root):
            return root is not None
        def triad(triad):
            return triad is not None

        def all():
            return Triad.create(root = "All", triad = "All")

        if root(root) and triad(triad):
            print(root, triad)
            print("\n sdfsdf")
            #Return a list of triads that go with those notes
            #i.e return chords that are minor and exist in [A,C,E,G,F]
            return
        if root():
            return Triad.create(root = root, triad = "All")
        if triad():
            return Triad.create(root = "All", triad = "All" )
        else:
            return all()





        #if notes == None or notes == "All"

    '''
    def constructors(triad_type):
        triad_type = triad_type.replace(" ", "")
        return globals()[triad_type + "Triad"]

    def generate_triad(triad, root):
        constructor = Triad.constructors(triad)
        return constructor(root)

    #all for note, not all for all notes
    def generate_all(root):
        triads = []
        for chord in Triad.types:
            new_triad = Triad.generate_triad(chord, root)
            triads.append(new_triad)
        return triads



    

    def create(root = None, triad = None ):

        if triad == "All":
            #function
            if root is "All":
                triads = []
                for note in Note:
                    triads += Triad.generate_all(note)
                return triads
            else:
                #print("DEBUG3-----------", triad, root)
                return Triad.generate_all(root)

        #print("DEBUG-----------", triad, root)
        triad = Triad.generate_triad(triad, root)
        return triad



    def __str__(self):
        return self.name




class MajorTriad(Triad):
    intervals = [
        Interval.MAJOR_THIRD,
        Interval.FIFTH
    ]
    def __init__(self, root):
        self.root = root
        self.type = "Major"
        self.name = root.__str__() + " " + self.type
        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()

        
class MinorTriad(Triad):
    intervals = [
        Interval.MINOR_THIRD,
        Interval.FIFTH
    ]
    def __init__(self, root):
        self.type = "Minor"
        self.name = root.__str__() + " " + self.type
        self.root = root
        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()
        
class SuspendedTriad(Triad):
    pass

class SuspendedTwoTriad(SuspendedTriad):
    suspended_interval = Interval.MAJOR_SECOND
    intervals = [
            Interval.MAJOR_SECOND,
            Interval.FIFTH
        ]
    
    def __init__(self, root):

        self.type = "Suspended Two"
        self.name = root.__str__() + " " + self.type

        self.root = root
        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()

class SuspendedFourTriad(SuspendedTriad):
    suspended_interval = Interval.FOURTH
    intervals = [
            Interval.FOURTH,
            Interval.FIFTH
        ]
    
    def __init__(self, root):

        self.type = "Suspended Four"
        self.name = root.__str__() + " " + self.type


        self.root = root
        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()
        
class AugmentedTriad(Triad):
    intervals = [
        Interval.MAJOR_THIRD,
        Interval.MINOR_SIXTH
    ]
    def __init__(self, root):
        self.type = "Augmented"
        self.name = root.__str__() + " " + self.type
        self.root = root
        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()

        
class DiminishedTriad(Triad):
    intervals = [
        Interval.MINOR_THIRD,
        Interval.DIMINISHED_FIFTH
    ]
    def __init__(self, root):
        self.type = "Diminished"
        self.name = root.__str__() + " " + self.type
        self.root = root
        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()


class FlatFiveTriad(Triad):
    intervals = [
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH
    ]
    def __init__(self, root):
        self.type = "Flat Five"
        self.name = root.__str__() + " " + self.type
        self.root = root
        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()
  


class Tetrad(Chord):
    types = [
        "Dominant Seven",
        "Major Seven",
        "Diminished Seven",
        "Six"
    ]

    def constructors(tetrad_type):
        tetrad_type = tetrad_type.replace(" ", "")
        return globals()[tetrad_type + "thChord"]

    def generate_tetrad(tetrad, triad, root):
        constructor = Tetrad.constructors(tetrad)
        return constructor(triad, root)

    #generate all tetrads for root note given
    def generate_all(root):
        tetrads = []



        for triad in Triad.types:
            for tetrad in Tetrad.types:
                new_tetrad = Tetrad.create(root = root, triad = triad, tetrad = tetrad)
                if "Error" not in new_tetrad.type:
                    if tetrad == "Six" and triad != "Diminished":
                        tetrads.append(new_tetrad)
                    elif tetrad != "Six":
                        tetrads.append(new_tetrad)
        return tetrads

    def create(tetrad = None, triad = None, root = None):
        if tetrad == "All":

            tetrads = []
            if root is "All":
                for note in Note:
                    tetrads += Tetrad.generate_all(note)
                return tetrads

            return Tetrad.generate_all(root)

        return Tetrad.generate_tetrad(tetrad, triad, root)


    #doesn't currently filter to have only chords with these notes, but gives chords for all notes as root
    def from_notes(notes):
        tetrads = []
        for note in notes:
            tetrad = Tetrad.create(tetrad = "All", root = note)
            tetrads += tetrad
        return tetrads

class SixthChord(Tetrad):
    sixth_interval = [
    Interval.MAJOR_SIXTH
    ]
    def __init__(self, triad, root):


        #setType()
        if triad == "Minor":
            self.type = "Minor Major Six"
        if triad == "Major":
            self.type = "Six"
        else:
            self.type = "Six " + triad

        self.name = root.__str__() + " " + self.type
        self.root = root
        self.tetrad_type = "Sixth"

        self.triad = Triad.create(
            triad = triad,
            root = root)

        self.intervals = self.triad.intervals + self.sixth_interval

        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()


        #create harmonic. Probably not necessary given self.fingerprint
        note = Note.from_int(root.value + Interval.MAJOR_SIXTH.value)

        self.enharmonic = [
            Chord.create(tetrad = "Dominant Seven", triad = "Minor", root = note)
        ]

        #print(self.enharmonic[0].type)


class SeventhChord(Tetrad):
    types = [
        "Dominant Seven",
        "Major Seven",
        "Diminished Seven"
    ]

class DominantSeventhChord(SeventhChord):
    seventh_interval = [
    Interval.MINOR_SEVENTH
    ]

    def set_type(self,triad):
        types = {
            "Diminished": "Half Diminished Seven",
            "Augmented": triad + " Seven",
             "Minor": triad + " Seven",
            "Flat Five": "Seven Flat Five",
            "Suspended Two": "Seven " + triad,
            "Suspended Four": "Seven " + triad,
        }

        self.type = types.get(triad, "Seven")

    def __init__(self, triad, root):
        self.set_type(triad)

        self.name = root.__str__() + " " + self.type
        self.root = root
        self.tetrad_type = "Dominant Seventh"

        self.triad = Triad.create(
            triad = triad,
            root = root)

        self.intervals = self.triad.intervals + self.seventh_interval

        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()

class MajorSeventhChord(SeventhChord):
    seventh_interval = [
    Interval.MAJOR_SEVENTH
    ]

    def __init__(self, triad, root):
        if triad in ("Minor", "Augmented", "Diminished"):
            self.type = triad + " " + "Major Seven"
        elif "Suspended" in triad:
            self.type = "Major Seven " + triad
        else:
            self.type = "Major Seven"


        
        
        self.name = root.__str__() + " " + self.type
        self.root = root
        self.tetrad_type = "Major Seventh"
        self.triad = Triad.create(
                    triad = triad,
                    root = root
                    )
        self.intervals = self.triad.intervals + self.seventh_interval

        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()

class DiminishedSeventhChord(SeventhChord):
    seventh_interval = [
    Interval.MAJOR_SIXTH
    ]

    def __init__(self, triad, root):
        if triad in ("Diminished"):
            self.type = "Diminished Seven"
        else:
            self.type = "Error Diminished 7"

        

        self.name = root.__str__() + " " + self.type
        self.root = root
        self.tetrad_type = "Diminished Seventh"
        self.triad = Triad.create(
                    triad = triad,
                    root = root
                    )
        self.intervals = self.triad.intervals + self.seventh_interval
        
        self.generate_notes()
        self.generate_inversions()
        self.generate_inversion_intervals()
        self.set_fingerprint()





#helper
def export_fingerprints():
    fingerprint_log = ""

    for fingerprint in Chord.fingerprints:
        #print("\n Checking fingerprint: ",fingerprint,Chord.fingerprints[fingerprint])

        value = Chord.fingerprints[fingerprint]
        fingerprint_log += "\n Chord for notes: " + list(fingerprint).__str__()

        if not isinstance(value, list):
            value = [value]

        for chord in value:
            fingerprint_log += "\n \t Chord:" + chord.name
            fingerprint_log += "\n \t \t Notes:" + chord.notes.__str__()
            if len(chord.notes) > 3:
                fingerprint_log += "\n \t \t Triad:" + chord.triad.__str__()
            if len(chord.notes) > 3:
                fingerprint_log += "\n \t \t Tetrad:" + chord.tetrad_type


    new_file = open("fingerprints.txt", "w")
    new_file.write(fingerprint_log)
    new_file.close()


Chord.set_fingerprints()
export_fingerprints()

print("sdfsdfsdfsdfdsfsdfsdfdsfsdf",len(Chord.fingerprints))









#Chord.fingerprints = {}





#my_chord = Chord.create(
#        root = Note.F,
#        triad = "Major",
#        tetrad = "Dominant Seven"
#    )
#
#print("My Chord:", my_chord, my_chord.name)
'''
print("--------:", my_chord.notes)

my_chord.triad = "Minor"
print("My Chord:", my_chord)

my_chord.triad = "Diminished"

'''


'''
The Testing Ground For Fellowship
'''

#h = Fretboard()

#for i in h.strings:
#    print(i)

#print(len(h.strings))


'''
The Testing Ground For Fellowship
'''


#########
# I need to figure out how to update the Chord.type string or whatever
#########