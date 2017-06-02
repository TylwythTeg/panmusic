from enum import Enum
from Note import *

class Tuning (Enum):
    STANDARD = [Note.E, Note.A, Note.D, Note.G, Note.B, Note.E]


class Fretboard():
    tuning = Tuning.STANDARD
    max_frets = 20

    def __init__(self):
        self.strings = []
        for note in self.tuning.value:
            self.strings.append(GuitarString(note, self.max_frets))


class GuitarString():

    def __init__(self, open_note, max_frets):
        self.frets = []
        for i in range (0,max_frets+1):
            self.frets.append(open_note.plus(i))

    def __str__(self):
        return self.frets.__str__()