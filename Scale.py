from Note import Note
from Chord import *

class Scale():
    notes = []
    triads = {}
    name = "Scale"
    
    #def factory()
    
    def addTriads(self):
        for note in self.notes:
            print ("\nChords for",note)
            self.triads[note] = self.build_triads_for_note(note)
            
            
        print("\nTest:")
        for triad in self.triads[Note.E]:
            print(triad)
            
    def build_triads_for_note(self, root):
        triads_for_note = []
        """chords = {
            Triad.MAJOR: MajorChord(root),
            Triad.MINOR: MinorChord(root),
            Triad.SUSPENDED_SECOND: SuspendedChord(root, Interval.MAJOR_SECOND),
            Triad.SUSPENDED_FOURTH: MinorChord(root),
            Triad.MINOR: MinorChord(root),
            Triad.MINOR: MinorChord(root),
            Triad.MINOR: MinorChord(root),
        }"""

        for triad in Triad:
            chord = Chord.factory(triad,root)
            if self.hasNotes(chord.notes):
                triads_for_note.append(chord)
        #if self.hasNotes()

        """if self.has_triad(root, Triad.MAJOR):
            triads_for_note.append(MajorChord(root))
        if self.has_triad(root, Triad.MINOR):
            triads_for_note.append(MinorChord(root))
        if self.has_triad(root, Triad.SUSPENDED_SECOND):
            triads_for_note.append(SuspendedChord(root, Interval.MAJOR_SECOND))
        if self.has_triad(root, Triad.SUSPENDED_FOURTH):
            triads_for_note.append(SuspendedChord(root, Interval.FOURTH))
        if self.has_triad(root, Triad.AUGMENTED):
            triads_for_note.append(AugmentedChord(root))
        if self.has_triad(root, Triad.DIMINISHED):
            triads_for_note.append(DiminishedChord(root))
        if self.has_triad(root, Triad.FLAT_FIFTH):
            triads_for_note.append(FlatFifthChord(root))"""
        
        for triad in triads_for_note:
            print(triad)
        return triads_for_note
            
        
    def has_triad(self, root, triad):
        #triads = {
            #Triad.MAJOR: return self.hasNotes(MajorChord(root).notes)

        #}
        if triad == Triad.MAJOR:
            return self.hasNotes(MajorChord(root).notes)
        if triad == Triad.MINOR:
            return self.hasNotes(MinorChord(root).notes)
        if triad == Triad.SUSPENDED_SECOND:
            return self.hasNotes(SuspendedChord(root,Interval.MAJOR_SECOND).notes)
        if triad == Triad.SUSPENDED_FOURTH:
            return self.hasNotes(SuspendedChord(root,Interval.FOURTH).notes)
        if triad == Triad.AUGMENTED:
            return self.hasNotes(AugmentedChord(root).notes)
        if triad == Triad.DIMINISHED:
            return self.hasNotes(DiminishedChord(root).notes)
        if triad == Triad.FLAT_FIFTH:
            return self.hasNotes(FlatFifthChord(root).notes)
        return False

    def __str__(self):
        return self.name
   

    def hasNotes(self, notes):
        for note in notes:
            if not self.hasNote(note):
                return False
        return True
                
            
    def hasNote(self, note):
        for scale_note in self.notes:
            if note == scale_note:
                return True
        return False
    
    
    
    
    
    
    


class PhrygianScale(Scale):

    intervals = {
        Interval.MINOR_SECOND,
        Interval.MINOR_THIRD,
        Interval.FOURTH,
        Interval.FIFTH,
        Interval.MINOR_SIXTH,
        Interval.MINOR_SEVENTH
    }
    def __init__(self, root):
        self.root = root
        self.name = root.__str__() + " Phrygian Scale"
        self.addNotes()
        self.triads = {}
        self.addTriads()
        
        
    def addNotes(self):
        self.notes = [self.root]
        for interval in self.intervals:
            self.notes.append(self.root.plus(interval))

        
        
scl = PhrygianScale(Note.E)
print(scl)
#print(scl.hasTriad(Note.F, Triad.FLAT_FIFTH))

#for note in scl.notes:
#    print("CHORDS FOR NOTE: " + note.__str__())
#    print(scl.triads[note])
#print(scl.triads)
#print(scl.notes)

#print(scl.hasNotes(MajorChord(Note.F).notes))
#print(MajorChord(Note.F).notes)
#print(MajorChord(Note.F).notes)
#print(MajorChord(Note.F).notes)

#chr = MajorChord(Note.F)
#print(chr.notes)
#print(MajorChord(Note.F).notes)
#print(MajorChord(Note.F).notes)

#chrs = MajorChord(Note.F)
#print(chrs.notes)
#MajorChord(Note.F)
#chr = MajorChord(Note.F)
#print(chr.notes)


#print("sdf")
#hat = Chord.factory(Triad.MAJOR, Note.E)
#print(hat.notes)
                
    