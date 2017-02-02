from Note import *
from enum import Enum

class Chord():
    name = None
    notes = []
    triad = None
    
    def factory(type, root, sus_interval=None):
        types = {
            Triad.MAJOR: MajorChord(root),
            Triad.MINOR: MinorChord(root),
            Triad.MINOR: SuspendedChord(root,sus_interval),
            Triad.MINOR: AugmentedChord(root),
            Triad.MINOR: DiminishedChord(root),
            Triad.MINOR: FlatFifthChord(root)
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

class MajorChord(Chord):
    
    def __init__(self, root):
        self.root = root
        self.name = root.__str__() + " Major Chord"
        self.addNotes()
        #print(self.notes)    
        
    def addNotes(self):
        self.notes = []
        self.notes.append(self.root)
        self.notes.append(self.root.plus(Interval.MAJOR_THIRD))
        self.notes.append(self.root.plus(Interval.FIFTH))
        
        
        
        
class MinorChord(Chord):   
    def __init__(self, root):
        self.root = root
        self.name = root.__str__() + " Minor Chord"
        self.addNotes()
        
    def addNotes(self):
        self.notes = []
        self.notes.append(self.root)
        self.notes.append(self.root.plus(Interval.MINOR_THIRD))
        self.notes.append(self.root.plus(Interval.FIFTH))
        
class SuspendedChord(Chord):   
    def __init__(self, root, interval):
        self.root = root
        self.name = root.__str__() + " Suspended " + interval.__str__() + " Chord"
        self.susInterval = interval
        self.addNotes()
        
    def addNotes(self):
        self.notes = []
        self.notes.append(self.root)
        self.notes.append(self.root.plus(self.susInterval))
        self.notes.append(self.root.plus(Interval.FIFTH))
        
class AugmentedChord(Chord):   
    def __init__(self, root):
        self.root = root
        self.name = root.__str__() + " Augmented Chord"
        self.addNotes()
        
    def addNotes(self):
        self.notes = []
        self.notes.append(self.root)
        self.notes.append(self.root.plus(Interval.MAJOR_THIRD))
        self.notes.append(self.root.plus(Interval.MINOR_SIXTH))
        
class DiminishedChord(Chord):   
    def __init__(self, root):
        self.root = root
        self.name = root.__str__() + " Diminished Chord"
        self.addNotes()
        
    def addNotes(self):
        self.notes = []
        self.notes.append(self.root)
        self.notes.append(self.root.plus(Interval.MINOR_THIRD))
        self.notes.append(self.root.plus(Interval.DIMINISHED_FIFTH))

class FlatFifthChord(Chord):   
    def __init__(self, root):
        self.root = root
        self.name = root.__str__() + " Flat Fifth Chord"
        self.addNotes()
        
    def addNotes(self):
        self.notes = []
        self.notes.append(self.root)
        self.notes.append(self.root.plus(Interval.MAJOR_THIRD))
        self.notes.append(self.root.plus(Interval.DIMINISHED_FIFTH))