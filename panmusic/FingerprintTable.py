from Chord import *
from Fingerprint import *
import time

class FingerprintTable():
    chords = None
    scales = None

    fingerprints = {}

    def fingerprint_exists(self, note_set):
        if self.fingerprints.get(note_set, None) is None:
            return False
        else:
            return True



    def __init__(self):
        #self.chords = []

        #change to generator for sure
        chords = Chord.all()

        for chord in chords:
            
            #if fingerprint exists, get current fingerprint to modify
            if self.fingerprints.get(chord.stamp, None) is not None:
                fingerprint = self.fingerprints[chord.stamp]
                
                if chord not in fingerprint.chords:
                    fingerprint.chords.append(chord)
                


            #else create new fingerprint
            else:
                self.fingerprints[chord.stamp] = Fingerprint(chord.stamp)
                self.fingerprints[chord.stamp].chords.append(chord)




ft = FingerprintTable()

print(ft.fingerprints["A,B,E"].chords)

from Note import Note
chord = Chord.create(triad = "Major", root = Note.A)

print(Fingerprint(chord.stamp).stamp)
    
            

print(len(ft.fingerprints))

'''
for stamp, fingerprint in ft.fingerprints.items():
    print("\n Chords for notes:", fingerprint.stamp)
    for chord in fingerprint.chords:
        print("\n \t ", chord.name)
        print("\n \t ", chord.notes)
'''