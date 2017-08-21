from Chord import *
from Fingerprint import *
import time

class FingerprintTable():
    chords = None
    scales = None

    fingerprints = {}

    ####### Returns whether or not stamp exists as a key in the fingerprints dictionary
    def fingerprint(self, stamp):
        return self.fingerprints.get(stamp, None) is not None



    def __init__(self):
        #self.chords = []

        #change to generator for sure
        chords = Chord.all()

        for chord in chords:
            
            #if fingerprint exists, get current fingerprint to modify
            if self.fingerprint(chord.stamp):
                fingerprint = self.fingerprints[chord.stamp]
                fingerprint.add_chord(chord)

            #else create new fingerprint
            else:
                self.fingerprints[chord.stamp] = Fingerprint(chord.stamp)
                self.fingerprints[chord.stamp].add_chord(chord)




ft = FingerprintTable()

print(ft.fingerprints["A,B,E"].chords)

from Note import Note
chord = Chord.create(triad = "Major", root = Note.A)

print(Fingerprint(chord.stamp).stamp)
    
            

print(len(ft.fingerprints))
print([chord.name for chord in ft.fingerprints["A,C#,F"].chords])
print(ft.fingerprint("A,C#,F"))


#if table.fingerprint("A,C,E"):


'''
for stamp, fingerprint in ft.fingerprints.items():
    print("\n Chords for notes:", fingerprint.stamp)
    for chord in fingerprint.chords:
        print("\n \t ", chord.name)
        print("\n \t ", chord.notes)
'''