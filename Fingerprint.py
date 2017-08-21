from Chord import *
from Note import *

class Fingerprint():

    def add_chord(self,chord):
        if chord not in self.chords:
            self.chords.append(chord)



    def __init__(self, stamp):
        self.chords = []
        if isinstance(stamp, Chord):
            self.id = stamp.fingerprint
            self.stamp = stamp.stamp
        else:
            self.stamp = stamp
            #stamp to list
            note_list = stamp.split(",")

            # these are strings so conver the strings in the list to notes
            note_list = [Note.from_string(note) for note in note_list]
            self.id = frozenset(note_list)

        self.sorted_string()

    def __eq__(self, other):

        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

    #return string of notes as "A,C#,E"
    #If the only thing creating Fingerprint Objects is FingerprintTable or Fingerprint Tree, they both sort the string 
    def sorted_string(self):
        #get list of notes in fingerprint
        notes = list(self.id)

        #convert to list of values (0-11) for sorting
        notes = [note.value for note in notes]

        notes = sorted(notes)

        #print(notes)

        #convert to list of strings representing notes in order from A-G#
        notes = [str(Note(note)) for note in notes]

        #print(notes)

        #convert list of strings into one string separated by comma such as "B,E,G"
        notes = ",".join(notes)

        #print(notes)

        return notes