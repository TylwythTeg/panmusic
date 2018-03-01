from enum import Enum
from Note import Note

class Tuning (Enum):
    STANDARD = [Note.E, Note.A, Note.D, Note.G, Note.B, Note.E]
    DROP_D = [Note.D, Note.A, Note.D, Note.G, Note.B, Note.E]
    DROP_C = [Note.C, Note.G, Note.C, Note.F, Note.A, Note.D]

    ## One-off custom
    CUSTOM = [Note.D, Note.A, Note.D, Note.FSHARP, Note.B, Note.D]



class Fretboard():
    object = "fretboard"
    tuning = Tuning.STANDARD

    #tuning = Tuning.CUSTOM
    max_frets = 12

    def __init__(self):
        self.strings = []
        for note in self.tuning.value:
            self.strings.append(GuitarString(note, self.max_frets))

        self.strings_reversed = list(reversed(self.strings))


class GuitarString():

    def __init__(self, open_note, max_frets):
        self.object = "guitar_string"
        self.root = open_note.__str__()
        self.notes = []
        for i in range (0, max_frets + 1):
            self.notes.append(open_note.plus(i).__str__())

    def __str__(self):
        return self.notes.__str__()

#Fretboard to JSON should reverse the tunings
#Or do it in javascript level makes more sense?

print(Fretboard())

fretboard = Fretboard()

for string in fretboard.strings:
    print("\n new string")
    for note in string.notes:
        print(note)