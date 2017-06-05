from Note import *
from enum import Enum
from Fretboard import *

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



    def set_fingerprint(self):
        self.fingerprint = frozenset(self.notes)
        #print("FINGERPRINT----",self.fingerprint)

    def set_fingerprints():

        #chords = Chord.all()

        triads = Triad.create(root = "All", triad = "All")
        tetrads = Tetrad.create(root = "All", tetrad = "All")

        chords = triads + tetrads

        #print(["car, happy"])
        #print("MY BIG ARRAY---------",chords)

        for chord in chords:
            print("\n Chord: ", chord)

        fingerprints = {}

        for chord in chords:

            #if fingerprint doesn't already exist, add that key (fingerprint) and value (chord) simply
            if chord.fingerprint not in fingerprints:
                #print("Added fingerprint:", chord.fingerprint)
                fingerprints[chord.fingerprint] = chord

            #fingerprint already exists, add it either to list or create list and add to list
            else:
                if isinstance(fingerprints[chord.fingerprint], list):
                    #add to list if there is already a list of multiple chord objects for this fingerprint
                    fingerprints[chord.fingerprint].append(chord)
                else:
                    #create list from element and add to it because this is not a list and only one exists
                    fingerprints[chord.fingerprint] = [fingerprints[chord.fingerprint]]
                    fingerprints[chord.fingerprint].append(chord)

        #print("--------------FINGERPRINTS",fingerprints,"____________________")

        Chord.fingerprints = fingerprints
    

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
            #print("\n self.root------------",self.root)
            self.notes.append(self.root.plus(interval))

        #need to move this into creation I guess?
        self.set_fingerprint()

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


    #This is probably deprecated
    def is_major(self):
        #If self.triad has been set as Major, we already know because we set this ourselves
        if self.triad == "Major":
            return True


        #This is a custom chord created with Chord(*notes)
        #We must calculate intervals between the notes and check for intervals
        intervals = self.calculate_intervals()
        print("THE INTERVALS", intervals)

        if Interval.MAJOR_THIRD in intervals:
            if Interval.FIFTH in intervals:
                return True
        
        return False
    
        
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



    def constructors(triad_type):
        triad_type = triad_type.replace(" ", "")
        return globals()[triad_type + "Triad"]

    def generate_triad(triad, root):
        constructor = Triad.constructors(triad)
        return constructor(root)

    #all for note, not all for all
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

    def __init__(self, triad, root):


        if triad == "Diminished":
            self.type = "Half Diminished Seven"
        elif triad == "Augmented":
            self.type = triad + " Seven"
        elif triad == "Flat Five":
            self.type = "Seven Flat Five"
        elif triad == "Minor":
            self.type = triad + " Seven"
        elif "Suspended" in triad:
            self.type = "Seven " + triad
        else:
            self.type = "Seven"

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




#helper functions go here
'''
def set_fingerprints(self):

    #chords = Chord.all()

    triads = Triad.create(root = "All", triad = "All")
    tetrads = Tetrad.create(root = "All", tetrad = "All")

    chords = triads + tetrads

    #print(["car, happy"])
    #print("MY BIG ARRAY---------",chords)

    for chord in chords:
        print("\n Chord: ", chord)

    fingerprints = {}

    for chord in chords:

        #if fingerprint doesn't already exist, add that key (fingerprint) and value (chord) simply
        if chord.fingerprint not in fingerprints:
            #print("Added fingerprint:", chord.fingerprint)
            fingerprints[chord.fingerprint] = chord

        #fingerprint already exists, add it either to list or create list and add to list
        else:
            if isinstance(fingerprints[chord.fingerprint], list):
                #add to list if there is already a list of multiple chord objects for this fingerprint
                fingerprints[chord.fingerprint].append(chord)
            else:
                #create list from element and add to it because this is not a list and only one exists
                fingerprints[chord.fingerprint] = [fingerprints[chord.fingerprint]]
                fingerprints[chord.fingerprint].append(chord)

    #print("--------------FINGERPRINTS",fingerprints,"____________________")

    Chord.fingerprints = fingerprints
'''


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








'''

        if chord.fingerprint in fingerprints:
            if isinstance(fingerprints[chord.fingerprint], list):
                #add to list
                fingerprints[chord.fingerprint].append(tetrad)
                #print("list")
            else:
                outlog += "\n Found a match: "
                outlog += "\n \t" + fingerprints[chord.fingerprint].__str__() + ":"

                #print("\n Found a match: ")
                #print("\n \t", fingerprints[tetrad.fingerprint], ":")
                uhm = fingerprints[chord.fingerprint]
                outlog += "\n \t \t Notes:" + uhm.notes.__str__()
                outlog += "\n \t \t Triad:" + uhm.triad.__str__()
                outlog += "\n \t \t Tetrad:" + uhm.tetrad_type
                #print("\n \t \t ","Notes:", uhm.notes)
                #print("\n \t \t ","Triad:", uhm.triad)
                #print("\n \t \t ","Tetrad:", uhm.tetrad_type)

                outlog += "\n \t [Equals] " + tetrad.__str__() + ":"
                outlog += "\n \t \t Notes:" + tetrad.notes.__str__()
                outlog += "\n \t \t Triad:" + tetrad.triad.__str__()
                outlog += "\n \t \t Tetrad:" + tetrad.tetrad_type
                #print("\n \t EQUALS", tetrad, ":")
                #print("\n \t \t ","Notes:", tetrad.notes)
                #print("\n \t \t ","Triad:", tetrad.triad)
                #print("\n \t \t ","Tetrad:", tetrad.tetrad_type)

                #make value of dict a list if it isn't
                fingerprints[chord.fingerprint] = [fingerprints[chord.fingerprint]]
                #add to this list
                fingerprints[chord.fingerprint].append(tetrad)
        else:
            fingerprints[chord.fingerprint] = tetrad
'''

Chord.fingerprints = {}



''

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