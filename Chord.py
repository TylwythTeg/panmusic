from Note import *
from enum import Enum


class Chord():
    name = None
    notes = []
    root = None
    tetrad = None
    triad = None



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


    ##############dict converters needs new class#############
    ########## panmusic.Dict.from()
    def as_dict(self):
        #check if or set before


        chord_dict = {}

        chord_dict["root"] = self.root.__str__()
        chord_dict["notes"] = list(map(str,self.notes))
        chord_dict["intervals"] = list(map(str, self.intervals))
        chord_dict["interval_dict"] = self.interval_dict()
        chord_dict["name"] = self.name


        #chord_dict["intervals"] = list(map(int, scale.intervals))

        #print("\n \n \n ", chord_dict)
       # print("sdfsdfsd",self.interval_dict())
        #print("!!!",list(map(str, self.intervals)))
        #print("\n \n \t ", chord_dict)

        return chord_dict

    # key: note string, value: interval #
    # for matching a note to an interval in regards to the scale#
    def interval_dict(self):
        notes = map(str, self.notes[1:])
        intervals =  map (str, self.intervals)

        dictionary = dict(zip(notes, intervals ))
        #print(" \n \n \t \t EFEFEFEF ", self.name, dictionary)
        return dictionary






    #############
    @classmethod
    def all(cls):
        #triads = Triad.create(root = "All", triad = "All")
        triads = Triad.list()
        tetrads = Tetrad.create(root = "All", tetrad = "All")


        return triads + tetrads
    #############


    ############### new stamp ##################
    def set_stamp(self):
        #### TODO: If custom chord, we need to order this series first
        ##
        #
        self.set_id()

        
        notes = self.notes

        #convert to list of values (0-11) and sort
        notes = [note.value for note in notes]
        notes = sorted(notes)

        #convert to list of strings representing notes in order from A-G#
        notes = [str(Note(note)) for note in notes]


        #convert list of strings into one string separated by comma such as "B,E,G"
        self.stamp = ",".join(notes)


    def set_id(self):
        self.id = frozenset(self.notes)

    ############### new stamp ##################


    ############# notes to chord, pass in list of strings string. pick one chord. prioritize by root #############
    ############# but default to the first element (call enharmonic() for rest) #############
    def from_notes(notes):


        notes = [Note.from_string(note) for note in notes]
        note_list = notes
        notes = frozenset(notes)

        chords = Chord.fingerprints[notes]

        chord_match = chords[0]


        for chord in chords:
            if chord.root == note_list[0]:
                return chord


        #if notes in Chord.fingerprints:
        return chord_match

    def enharmonics(self):
        chords = Chord.fingerprints[self.fingerprint]

        #remove self chord
        enharmonics = []
        for chord in chords:
            if chord != self:
                enharmonics.append(chord)
        return enharmonics





    def __init__(self, notes , root = None):
        self.notes = []

        for note in notes:
            self.notes.append(note)

        if root is not None:
            self.root = root
        
        self.set_stamp()
        self.set_id()

    def generate_notes(self):
        self.notes = [self.root]
        for interval in self.intervals:
            self.notes.append(self.root + interval)

    @classmethod
    def create(cls, root = None, triad = None, tetrad = None ):

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



############## Triads ##############
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


    @classmethod
    def constructors(cls, triad_type):
        triad_type = triad_type.replace(" ", "")
        return globals()[triad_type + "Triad"]

    @classmethod
    def generate_triad(cls, triad, root):
        constructor = Triad.constructors(triad)
        return constructor(root)

    #all for note, not all for all notes
    def generate_all(root):
        triads = []
        for chord in Triad.types:
            new_triad = Triad.generate_triad(chord, root)
            triads.append(new_triad)
        return triads


    #def list(**kwargs):
    #    if "scale" in kwargs:

    @classmethod
    def list(cls, root = None, triad = None):
        #Boolean check if no arguments passed
        def all():
            return root is None and triad is None

        #generate all triads from note
        def from_note(root):
            triads = []
            for chord in Triad.types:
                new_triad = Triad.generate_triad(chord, root)
                triads.append(new_triad)
            return triads

        #generate all triads of type X for every note
        def from_triad(triad):
            triads = []
            for note in Note:
                new_triad = Triad.generate_triad(triad, note)
                triads.append(new_triad)
            return triads

        #Absolutely all triads, all notes
        def generate_all():
            triads = []
            for note in Note:
                triads += from_note(note)
            return triads



        #say you give pass my_scale.notes. This function will give you triads for this scale
        #def from_notes(notes):
        #    for note in notes:



        if all():
            return generate_all()


        if root is None:
            return from_triad(triad)

        if triad is None:
            return from_note(root)

        #print("\n ------Why the fuck did I make it here then??????")
        #print("\n ------Why the fuck did I make it here then??????")
        #print("\n ------Why the fuck did I make it here then??????")
        #print("\n ------Why the fuck did I make it here then??????")





    @classmethod
    def create(cls, root = None, triad = None ):
        def none():
            return root is None or triad is None

        if none():
            print("\n ----@@@You should use create to create singular objects?")
            #maybe return an empty chord, raise an error idk
            #maybe random chord
            #if one or the other is supplied, maybe route to lists?
            return None

        return Triad.generate_triad(triad, root)




    def __str__(self):
        return self.name




class MajorTriad(Triad):
    intervals = [
        Interval.MAJOR_THIRD,
        Interval.FIFTH
    ]
    def __init__(self, root):
        #print("root", self.root)
        self.root = root
        self.type = "Major"
        self.name = root.__str__() + " " + self.type
        self.generate_notes()
        self.set_stamp()


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
        self.set_stamp()

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
        self.set_stamp()

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
        self.set_stamp()

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
        self.set_stamp()


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
        self.set_stamp()


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
        self.set_stamp()


############## Tetrads ##############
class Tetrad(Chord):
    types = [
        "Dominant Seven",
        "Major Seven",
        "Diminished Seven",
        "Six"
    ]

    @classmethod
    def constructors(cls, tetrad_type):
        tetrad_type = tetrad_type.replace(" ", "")
        return globals()[tetrad_type + "thChord"]

    @classmethod
    def generate_tetrad(cls, tetrad, triad, root):
        constructor = Tetrad.constructors(tetrad)
        return constructor(triad, root)


    #generate all tetrads for root note given
    @classmethod
    def generate_all(cls, root):
        tetrads = []



        for triad in Triad.types:
            for tetrad in Tetrad.types:
                new_tetrad = Tetrad.create(root = root, triad = triad, tetrad = tetrad)

                #filter out tetrad.type with "Error" (meaning chord shouldn't exist based on combination)
                if "Error" not in new_tetrad.type:
                    #filter out because Six and diminished doesn't exist?
                    if tetrad == "Six" and triad != "Diminished":
                        tetrads.append(new_tetrad)
                    elif tetrad != "Six":
                        tetrads.append(new_tetrad)
        return tetrads

    @classmethod
    def create(cls, tetrad = None, triad = None, root = None):
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

    def set_type(self, triad):
        types = {
            "Minor": "Minor Major Six",
            "Major": "Six",
        }
        self.type = types.get(triad, "Six " + triad)


    def __init__(self, triad, root):


        self.set_type(triad)

        self.name = root.__str__() + " " + self.type
        self.root = root
        self.tetrad_type = "Sixth"

        self.triad = Triad.create(
            triad = triad,
            root = root)

        self.intervals = self.triad.intervals + self.sixth_interval

        self.generate_notes()
        self.set_stamp()



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
        self.set_stamp()

class MajorSeventhChord(SeventhChord):
    seventh_interval = [
    Interval.MAJOR_SEVENTH
    ]


    def set_type(self, triad):
        types = {
            "Minor": triad + " " + "Major Seven",
            "Augmented": triad + " " + "Major Seven",
            "Diminished": triad + " " + "Major Seven",
            "Suspended Two": "Major Seven " + triad,
            "Suspended Four": "Major Seven " + triad,
        }
        self.type = types.get(triad, "Major Seven")

    def __init__(self, triad, root):

        self.set_type(triad)

        self.name = root.__str__() + " " + self.type
        self.root = root
        self.tetrad_type = "Major Seventh"
        self.triad = Triad.create(
                    triad = triad,
                    root = root
                    )
        self.intervals = self.triad.intervals + self.seventh_interval

        self.generate_notes()
        self.set_stamp()

class DiminishedSeventhChord(SeventhChord):
    seventh_interval = [
    Interval.MAJOR_SIXTH
    ]

    def set_type(self, triad):
        types = {
            "Diminished": "Diminished Seven",
        }
        self.type = types.get(triad, "Error Diminished 7")

    def __init__(self, triad, root):
        self.set_type(triad)
        self.name = root.__str__() + " " + self.type
        self.root = root
        self.tetrad_type = "Diminished Seventh"
        self.triad = Triad.create(
                    triad = triad,
                    root = root
                    )
        self.intervals = self.triad.intervals + self.seventh_interval

        self.generate_notes()
        self.set_stamp()



