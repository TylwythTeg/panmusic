from Note import *
from enum import Enum

class Chord():
    name = None
    notes = []
    _tetrad = None
    triad = None
    

    def __init__(self, root):
        self.root = root
        self.name = "Scale"

    def generate_notes(self):
        self.notes = [self.root]
        for interval in self.intervals:
            self.notes.append(self.root.plus(interval))
    
    def old_create(type, root, triad = "None"):
        types = {
            "Major": MajorTriad(root),
            "Minor": MinorTriad(root),
            "Suspended Two": SuspendedTriad(root, Interval.MAJOR_SECOND),
            "Suspended Four": SuspendedTriad(root, Interval.FOURTH),
            "Augmented": AugmentedTriad(root),
            "Diminished": DiminishedTriad(root),
            "Flat Five": FlatFiveTriad(root),

            "Dominant Seven": DominantSeventhChord(triad,root),
            "Major Seven": MajorSeventhChord(triad,root),
            "Diminished Seven": DiminishedSeventhChord(triad,root),

            #"All": AllChords(root)
        }
        return types.get(type)

    def tetrad_setter(self, tetrad):
        self._tetrad = tetrad

    def tetrad_getter(self):
        return self._tetrad

    tetrad = property(tetrad_getter, tetrad_setter)




    def triad_setter(self, triad):
        self.triad = triad
        print("-------------------------",triad)
        '''
        #If no tetrad in Chord, use the triad string as the class
        if self.tetrad is None:

            #check if object instead of string and get string
            if isinstance(triad,Triad):
                triad = triad.type

            #update() can use self.update but would go through all checks
            #update(triad) 
            triad = triad.__str__()
            self.__class__ = globals()[triad + "Triad"]
            self.type = triad
            self.name = self.root.__str__() + " " + self.type
        else:

            tetrad_type = self.tetrad_type.replace(" ","")

            self.__class__ = globals()[tetrad_type + "Chord"]
            print("CLASS IS :",self.__class__)
            #will want to do based on type
            self. type = tetrad
            self.name = self.root__str_() + "" + self.type
            #update class by 7

        print("CASDD",self.__class__)
        #self._class_ = Triad.classes['triad']

    def triad_getter(self):
        return self._triad

    triad = property(triad_getter,triad_setter)
    '''




    #Keywords:
    #   root
    #   triad
    #   tetrad
    def create(root = None, triad = None, tetrad = None ):
        #no tetrad, so go down one
        print(root, triad, tetrad,"-----------------")

        if tetrad is None:
            return Triad.zcreate(root, triad)
        #creating a tetrad
        else: 
            #print("I got a this chord///////////////////////////////")
            #return Chord.old_create(tetrad, root, triad)
            #return Tetrad.create(root =x_root, triad =x_triad, tetrad = x_tetrad)
            #print(root, triad, tetrad)
            
            return Tetrad.create(tetrad, triad, root)



    def kcreate(**chord):
        for k,v in chord.items():
            print(k,v)

        #no tetrad, so go down one
        if 'tetrad' not in chord:
            return Triad.kcreate(**chord)
        else:
            return Chord.create(chord['tetrad'], chord['root'], chord['triad'])



            #triad = chord["triad"]
            #constructor = Triad.constructors[triad]
            #return constructor(chord["root"])

        #constructor = Triad.constructors.get(chord["triad"]):


        '''
        triads = {
            "Major" = MajorTriad(root),
            "Minor": = MinorTriad(root),
            "Suspended Two": SuspendedTriad(root, Interval.MAJOR_SECOND),
            "Suspended Two": SuspendedTriad(root, Interval.MAJOR_SECOND),
            "Augmented": AugmentedTriad(root),
            "Diminished": DiminishedTriad(root),
            "Flat Five": FlatFifthTriad(root),
        }
        '''



        #if 'tetrad' not in kwargs:
            #for k,v in kwargs.items():





    



        
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
        #for triad in types:
        print("CHECKECKECKECKECKEKECKECKECKECKECKECKECKECKECKECKECKEKCECKCEK")
        return globals()[triad_type+"Triad"]

        triads = {
            "Major": MajorTriad(root),
            "Minor": MinorTriad(root),
            "Suspended Two": SuspendedTriad(root, Interval.MAJOR_SECOND),
            "Suspended Two": SuspendedTriad(root, Interval.MAJOR_SECOND),
            "Augmented": AugmentedTriad(root),
            "Diminished": DiminishedTriad(root),
            "Flat Five": FlatFiveTriad(root),
        }
        return triads.get(triad_type,"what")
    

    def create(triad, root):
        types = {
            "Major": MajorTriad(root),
            "Minor": MinorTriad(root),
            "Suspended Two": SuspendedTriad(root, Interval.MAJOR_SECOND),
            "Suspended Four": SuspendedTriad(root, Interval.FOURTH),
            "Augmented": AugmentedTriad(root),
            "Diminished": DiminishedTriad(root),
            "Flat Five": FlatFiveTriad(root)
            }
        return types.get(triad)


    def zcreate(root = None, triad = None ):

        constructor = Triad.constructors(triad)
        return constructor(root)


    def kcreate(**chord):
        triad = chord["triad"]
        print("THIS THING RAR",chord["triad"])
        constructor = Triad.constructors(triad)
        return constructor(chord["root"])
    
    


    def __str__(self):
        return self.name

class Tetrad(Chord):
    types = [
        "Seven",
        "Six",
    ]

    def constructors(tetrad_type):
        #for triad in types:
        '''
        return globals()[triad_type+"Triad"]

        tetrads = {
            "Major": MajorTriad(root),
            "Minor": MinorTriad(root),
        }
        return tetrads.get(triad_type,"what")
        '''

        tetrad_type = tetrad_type.replace(" ", "")
        return globals()[tetrad_type + "thChord"]

    def create(name, triad, root):
        print("hey")
       #types = {
        #    "Dominant Seven": DominantSeventhChord(triad,root),
         #   "Major Seven": MajorSeventhChord(triad,root),
          #  "Diminished Seven": DiminishedSeventhChord(triad,root),
           # }
        #return types.get(name)

        constructor = Tetrad.constructors(name)
        return constructor(triad, root)



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


        #print("testsdsdfdsfsdfsdf")
        #print(Note.A.plus(24))

        #print(self.intervals)
        
        
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
        self.triad = Triad.create(triad, root)

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
        self.triad = Triad.create(triad, root)
        #print("0intervals:", self.intervals)
        #print("triad_intervals:", self.triad.intervals)
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
        self.triad = Triad.create(triad, root)
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

#########
# I need to figure out how to update the Chord.type string or whatever
#########