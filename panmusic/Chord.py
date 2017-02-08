from Note import *
from enum import Enum

class Chord():
    name = None
    notes = []
    triad = None

    def __init__(self, root):
        self.root = root
        self.name = "Scale"

    def generate_notes(self):
        self.notes = [self.root]
        print("starting")
        for interval in self.intervals:
            print("Added note:", self.root.plus(interval),"To chord:", self.root)
            self.notes.append(self.root.plus(interval))


    triad_types = [
        "Major",
        "Minor",
        "Suspended Second",
        "Suspended Fourth",
        "Augmented",
        "Diminished",
        "Flat Fifth"

    ]

    
    def factory(type, root):
        types = {
            Triad.MAJOR: MajorChord(root),
            Triad.MINOR: MinorChord(root),
            Triad.SUSPENDED_SECOND: SuspendedChord(root, Interval.MAJOR_SECOND),
            Triad.SUSPENDED_FOURTH: SuspendedChord(root, Interval.FOURTH),
            Triad.AUGMENTED: AugmentedChord(root),
            Triad.DIMINISHED: DiminishedChord(root),
            Triad.FLAT_FIFTH: FlatFifthChord(root)
        }
        return types.get(type)
        
    def __str__(self):
        return self.name
            
    
    #def addNote(note):
        #self.notes.append(note)
        
class Triad(Enum):
    MAJOR = 0
    MINOR = 1
    SUSPENDED_SECOND = 2
    SUSPENDED_FOURTH = 3
    AUGMENTED = 4
    DIMINISHED = 5
    FLAT_FIFTH = 6

    def from_string(string):
        types = {
            "Major": Triad.MAJOR,
            "Minor": Triad.MINOR,
            "Suspended Second": Triad.SUSPENDED_SECOND,
            "Suspended Fourth": Triad.SUSPENDED_FOURTH,
            "Augmented": Triad.AUGMENTED,
            "Diminished": Triad.DIMINISHED,
            "Flat Fifth": Triad.FLAT_FIFTH
        }
        return types.get(string)



#MAJOR.sdf =1

    def __str__(self):
        return {
            MAJOR: "Major",
            MINOR: "Minor",
            SUSPENDED_SECOND: "Suspended Second",
            SUSPENDED_FOURTH: "Suspended Fourth",
            AUGMENTED: "Augmented",
            DIMINISHED: "Diminished",
            FLAT_FIFTH: "Flat Fifth",
        }.get(self, 'Triad Not Found')


class MajorChord(Chord):
    intervals = [
        Interval.MAJOR_THIRD,
        Interval.FIFTH
    ]
    def __init__(self, root):
        self.root = root
        self.name = root.__str__() + " Major Chord"
        self.generate_notes()

        
        
        
        
class MinorChord(Chord):
    intervals = [
        Interval.MINOR_THIRD,
        Interval.FIFTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Minor Chord"
        self.root = root
        self.generate_notes()
        
class SuspendedChord(Chord):

    def __init__(self, root, interval):
        self.name = root.__str__() + " Suspended " + interval.__str__() + " Chord"
        self.susInterval = interval
        self.intervals = [
            self.susInterval,
            Interval.FIFTH
        ]
        self.root = root
        self.generate_notes()
        
class AugmentedChord(Chord):
    intervals = [
        Interval.MAJOR_THIRD,
        Interval.MINOR_SIXTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Augmented Chord"
        self.root = root
        self.generate_notes()

        
class DiminishedChord(Chord):
    intervals = [
        Interval.MINOR_THIRD,
        Interval.DIMINISHED_FIFTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Diminished Chord"
        self.root = root
        self.generate_notes()


class FlatFifthChord(Chord):
    intervals = [
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH
    ]
    def __init__(self, root):
        self.name = root.__str__() + " Flat Fifth Chord"
        self.root = root
        self.generate_notes()