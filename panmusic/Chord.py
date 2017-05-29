from Note import *
from enum import Enum
from Fretboard import * 

class Chord():
    name = None
    notes = []
    tetrad = None
    triad = None
    

    def __init__(self, root):
        self.root = root
        self.name = "Scale"

    def generate_notes(self):
        self.notes = [self.root]
        for interval in self.intervals:
            self.notes.append(self.root.plus(interval))





    #Keywords:
    #   root
    #   triad
    #   tetrad
    def create(root = None, triad = None, tetrad = None ):

        if tetrad is None:
            return Triad.create(root = root, triad = triad)
        else:    
            return Tetrad.create(tetrad = tetrad,triad = triad,root = root)





    



        
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
        return globals()[triad_type + "Triad"]
    

    def create(root = None, triad = None ):

        #Does suspended need to be a tier of class? like Sus < 2,4
        if "Suspended" in triad:
            #triad = triad.split()[1]
            sus = {
                "Two" : Interval.MAJOR_SECOND,
                "Four" : Interval.FOURTH
            }
            interval = sus[triad.split()[1]]
            constructor = globals()["SuspendedTriad"]

            return SuspendedTriad(root, interval )

        elif "Flat Five" in triad:
            return FlatFiveTriad(root)


               



        constructor = Triad.constructors(triad)
        return constructor(root)

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
        
class SuspendedTriad(Triad):

    def __init__(self, root, interval):

        if interval == Interval.MAJOR_SECOND:
            self.type = "Suspended Two"
        elif interval == Interval.FOURTH:
            self.type = "Suspended Four"
        self.name = root.__str__() + " " + self.type
        self.susInterval = interval

        self.intervals = [
            self.susInterval,
            Interval.FIFTH
        ]

        self.root = root
        self.generate_notes()
        
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
  


class Tetrad(Chord):
    types = [
        "Seven",
        "Six",
    ]

    def constructors(tetrad_type):
        tetrad_type = tetrad_type.replace(" ", "")
        return globals()[tetrad_type + "thChord"]

    def create(tetrad = None, triad = None, root = None):
        constructor = Tetrad.constructors(tetrad)
        return constructor(triad, root)


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


        #setType()
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

        print("Reached here!")
        #t_triad = self.triad

        self.name = root.__str__() + " " + self.type
        print(self.name)
        self.root = root
        self.tetrad_type = "Dominant Seventh"

        self.triad = Triad.create(
            triad = triad,
            root = root)

        #t_intervals = self.intervals
        #t_triad_intervals = self.triad.intervals

        self.intervals = self.triad.intervals + self.seventh_interval

        self.generate_notes()

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
        #print("intervals:", self.intervals)
        

        self.generate_notes()

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








my_chord = Chord.create(
        root = Note.F,
        triad = "Major",
        tetrad = "Dominant Seven"
    )


print("My Chord:", my_chord, my_chord.name)
'''
print("--------:", my_chord.notes)

my_chord.triad = "Minor"
print("My Chord:", my_chord)

my_chord.triad = "Diminished"

'''


'''
The Testing Ground For Fellowship
'''

h = Fretboard()

for i in h.strings:
    print(i)

print(len(h.strings))


'''
The Testing Ground For Fellowship
'''


#########
# I need to figure out how to update the Chord.type string or whatever
#########