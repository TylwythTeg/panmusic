from enum import Enum

class Note(Enum):
    A = 0
    ASHARP = 1
    B = 2
    C = 3
    CSHARP = 4
    D = 5
    DSHARP = 6
    E = 7
    F = 8
    FSHARP = 9
    G = 10
    GSHARP = 11


    def __str__(self):
        choices = {
            Note.A: "A",
            Note.ASHARP: "A#",
            Note.B: "B",
            Note.C: "C",
            Note.CSHARP: "C#",
            Note.D: "D",
            Note.DSHARP: "D#",
            Note.E: "E",
            Note.F: "F",
            Note.FSHARP: "F#",
            Note.G: "G",
            Note.GSHARP: "G#"
        }
        return choices.get(self, 'Note Not Found')

    def from_string(str):
        choices = {
            "A": Note.A,
            "A#": Note.ASHARP,
            "ASharp": Note.ASHARP,
            "B": Note.B,
            "C": Note.C,
            "C#": Note.CSHARP,
            "CSharp": Note.CSHARP,
            "D": Note.D,
            "D#": Note.DSHARP,
            "DSharp": Note.DSHARP,
            "E": Note.E,
            "F": Note.F,
            "F#": Note.FSHARP,
            "FSharp": Note.FSHARP,
            "G": Note.G,
            "G#": Note.GSHARP,
            "GSharp": Note.GSHARP,
        }
        return choices.get(str, 'Note Not Found')

    def __repr__(self):
        return self.__str__()
        
    
    
    def plus(self, amount):
        if isinstance(amount, Interval):
            amount = amount.value
        while self.value + amount >= 12:
            amount -= 12
        amount += self.value
        return Note(amount)
            
    def is_in_scale(self, scale):
        for note in scale.notes:
            if self == note:
                return true
        return false
    
class Interval(Enum):
    UNISON = 0
    MINOR_SECOND = 1
    MAJOR_SECOND = 2
    MINOR_THIRD = 3
    MAJOR_THIRD = 4
    FOURTH = 5
    DIMINISHED_FIFTH = 6
    FIFTH = 7
    MINOR_SIXTH = 8
    MAJOR_SIXTH = 9
    MINOR_SEVENTH = 10
    MAJOR_SEVENTH = 11
    
    def __str__(self):
        choices = {
            Interval.UNISON: "Unison",
            Interval.MINOR_SECOND: "Minor Second",
            Interval.MAJOR_SECOND: "Second",
            Interval.MINOR_THIRD: "Minor Third",
            Interval.MAJOR_THIRD: "Major Third",
            Interval.FOURTH: "Fourth",
            Interval.DIMINISHED_FIFTH: "Diminished Fifth",
            Interval.FIFTH: "Fifth",
            Interval.MINOR_SIXTH: "Minor Sixth",
            Interval.MAJOR_SIXTH: "Sixth",
            Interval.MINOR_SEVENTH: "Dominant Seventh",
            Interval.MAJOR_SEVENTH: "Major Seventh",
        }
        return choices.get(self, 'Interval Not Found')
        
    def sharp(self):
        return self.value + 1
    
    def flat(self):
        return self.value - 1
    

    
        
    

