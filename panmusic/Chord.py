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
        apples = self.root
        for interval in self.intervals:
            self.notes.append(self.root.plus(interval))
    
    def create(type, root, triad = "None"):
        types = {
            "Major": MajorTriad(root),
            "Minor": MinorTriad(root),
            "Suspended Two": SuspendedTriad(root, Interval.MAJOR_SECOND),
            "Suspended Four": SuspendedTriad(root, Interval.FOURTH),
            "Augmented": AugmentedTriad(root),
            "Diminished": DiminishedTriad(root),
            "Flat Five": FlatFifthTriad(root),

            "Dominant Seven": DominantSeventhChord(Triad.create(triad, root)),
            "Major Seven": MajorSeventhChord(Triad.create(triad,root)),
            "Diminished Seven": DiminishedSeventhChord(Triad.create(triad,root))
        }

        

        return types.get(type)
        
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

    def create(triad, root):
        types = {
            "Major": MajorTriad(root),
            "Minor": MinorTriad(root),
            "Suspended Two": SuspendedTriad(root, Interval.MAJOR_SECOND),
            "Suspended Four": SuspendedTriad(root, Interval.FOURTH),
            "Augmented": AugmentedTriad(root),
            "Diminished": DiminishedTriad(root),
            "Flat Five": FlatFifthTriad(root)
            }
        return types.get(triad)


    def __str__(self):
        return self.type

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


        print("testsdsdfdsfsdfsdf")
        print(Note.A.plus(24))
        
        
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


class FlatFifthTriad(Triad):
    intervals = [
        Interval.MAJOR_THIRD,
        Interval.DIMINISHED_FIFTH
    ]
    def __init__(self, root):
        self.type = "Flat Five"
        self.name = root.__str__() + " " + self.type
        self.root = root
        self.generate_notes()
  


class SeventhChord(Chord):
    pass

class DominantSeventhChord(SeventhChord):
    intervals = [
    Interval.MINOR_SEVENTH
    ]

    def __init__(self, triad):

        if triad.type == "Diminished":
            self.type = "Half Diminished Seven"
        elif triad.type == "Augmented":
            self.type = triad.type + " Seven"
        elif triad.type == "Flat Five":
            self.type = "Seven Flat Five"
        else:
            self.type = "Seven"

        self.triad = triad
        self.name = triad.root.__str__() + " " + self.type
        self.root = triad.root

        self.intervals = triad.intervals + self.intervals

        self.generate_notes()

class MajorSeventhChord(SeventhChord):
    intervals = [
    Interval.MAJOR_SEVENTH
    ]

    def __init__(self, triad):
        if triad.type in ("Minor", "Augmented", "Diminished"):
            self.type = triad.type + " " + "Major Seven"
        elif triad.type in ("Suspended Second", "Suspended Fourth"):
            self.type = "Major Seven " + triad.type
        else:
            self.type = "Major Seven"

        self.triad = triad
        self.name = triad.root.__str__() + " " + self.type
        self.root = triad.root
        self.intervals = triad.intervals + self.intervals

        self.generate_notes()

class DiminishedSeventhChord(SeventhChord):
    intervals = [
    Interval.MAJOR_SIXTH
    ]

    def __init__(self, triad):
        if triad.type in ("Diminished"):
            self.type = "Diminished Seven"
        else:
            self.type = "Error Diminished 7"

        self.traid = triad
        self.name = triad.root.__str__() + " " + self.type
        self.root = triad.root
        self.intervals = triad.intervals + self.intervals

        self.generate_notes()

