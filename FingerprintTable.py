from Chord import *
from Fingerprint import *
from Scale import Scale
from FingerprintTree import FingerprintTree
#import time

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
        #add_chords()
        for chord in Chord.all():
            
            #if fingerprint exists, get current fingerprint to modify
            if self.fingerprint(chord.stamp):
                fingerprint = self.fingerprints[chord.stamp]
                fingerprint.add_chord(chord)

            #else create new fingerprint
            else:
                self.fingerprints[chord.stamp] = Fingerprint(chord.stamp)
                self.fingerprints[chord.stamp].add_chord(chord)

        #add_scales
        for scale in Scale.all():
            #if fingerprint exists, get current fingerprint to modify
            print(scale.stamp)
            if self.fingerprint(scale.stamp):
                fingerprint = self.fingerprints[scale.stamp]
                fingerprint.add_scale(scale)

            #else create new fingerprint
            else:
                self.fingerprints[scale.stamp] = Fingerprint(scale.stamp)
                self.fingerprints[scale.stamp].add_scale(scale)


        #add_tree()
        #build_stamp_list()
        stamp_list = []
        for stamp in self.fingerprints:

            #build stamp_list()  could I just list-ify the dictionary keys, would that be easier or faster?
            

            stamp = stamp.split(",")
            #replace sharps with single-char equivalents
            stamp = FingerprintTree.replace_sharps(stamp)

            if stamp not in stamp_list:
                stamp_list.append(stamp)
        #add_tree() again (scope)
        self.tree = FingerprintTree(stamp_list)





ft = FingerprintTable()

print(ft.fingerprints["A,B,E"].chords)

from Note import Note
chord = Chord.create(triad = "Major", root = Note.A)

print(Fingerprint(chord.stamp).stamp)
    
            

print(len(ft.fingerprints))
print([chord.name for chord in ft.fingerprints["A,C#,F"].chords])
print(ft.fingerprint("A,C#,F"))



sfs = ft.tree.stamps_at_suffix("G,B,C#,E")
print("\n All Stamps at G,B,C#,E: ", sfs)






## A Major Scale
sfs = ft.tree.stamps_at_suffix("A,B,C#,D,E,F#,G#")
print("\n \n All Stamps at A,B,C#,D,E,F#,G#: ", sfs)

fingerprint = ft.fingerprints["A,B,C#,D,E,F#,G#"]

#print chords
print("\n Chords:")
for chord in fingerprint.chords:
    print(chord)

#print scales
print("\n Scales")
for scale in fingerprint.scales:
    print(scale)








#### get all stamps that are superstrings of suffix
superstrings = ft.tree.superstrings("E,G,C#")
print("\n \n \n All Super Strings of C#,E,G :", superstrings)


#if table.fingerprint("A,C,E"):


'''
for stamp, fingerprint in ft.fingerprints.items():
    print("\n Chords for notes:", fingerprint.stamp)
    for chord in fingerprint.chords:
        print("\n \t ", chord.name)
        print("\n \t ", chord.notes)
'''