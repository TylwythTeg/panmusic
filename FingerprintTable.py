from Chord import *
from Fingerprint import *
from Scale import Scale
from FingerprintTree import FingerprintTree
#import time

class FingerprintTable():
    chords = []
    scales = []
    tree = None

    fingerprints = {}

    ####### Returns whether or not stamp exists as a key in the fingerprints dictionary
    def fingerprint(self, stamp):
        return self.fingerprints.get(stamp, None) is not None

    ####### Returns self.fingerprints[stamp] or None if it is not found
    ####### retrieve("A,C#,E")
    def retrieve(self, stamp):
        # turn comma separated note strings into a list of note strings
        note_list = stamp.split(",")

        # these are strings so conver the strings in the list to notes
        note_list = [Note.from_string(note) for note in note_list]
        # make a hashable frozen set to retrieve from dictionary
        stamp = frozenset(note_list)


        return self.fingerprints.get(stamp, None)

    ####### Adds all fingerprints from chords, and adds those chords to those fingerprints
    def add_chords(self):
        for chord in Chord.all():
            
            #if fingerprint exists, get current fingerprint to modify
            if self.fingerprint(chord.id):
                fingerprint = self.fingerprints[chord.id]
                fingerprint.add_chord(chord)

            #else create new fingerprint
            else:
                self.fingerprints[chord.id] = Fingerprint(chord.stamp)
                self.fingerprints[chord.id].add_chord(chord)

    ####### Adds all fingerprints from scales, and adds those scales to those fingerprints
    def add_scales(self):
        for scale in Scale.all():
            #if fingerprint exists, get current fingerprint to modify
            #print(scale.stamp)
            if self.fingerprint(scale.id):
                fingerprint = self.fingerprints[scale.id]
                fingerprint.add_scale(scale)

            #else create new fingerprint
            else:
                self.fingerprints[scale.id] = Fingerprint(scale.stamp)
                self.fingerprints[scale.id].add_scale(scale)


    ####### Adds the suffix tree that we use to determine relationships and related notes
    def add_tree(self):
        # Build list from fingerprint keys (with replaced sharps)
        # Do we even need to do this? Would STree take a dictionary fine? Look into that
        stamp_list = [FingerprintTree.replace_sharps(stamp) for stamp in self.fingerprints.keys()]
        self.tree = FingerprintTree(stamp_list)



    # returns a list of fingerprint objects where their stamps are superstrings of input: fingerprint.stamp
    # NOTE: maybe take a pure stamp as well instead of a fingerprint object?
    def fingerprint_extensions(self, fingerprint):
        superstrings = self.tree.superstrings(fingerprint.stamp)
        print("\n \t superstrings", superstrings)
        fingerprints = [self.retrieve(superstring) for superstring in superstrings]
        return fingerprints


    def __init__(self):
        self.add_chords()
        self.add_scales()

        #self.add_tree()

        





ft = FingerprintTable()

print("----------",ft.retrieve("E,B,A").chords)
'''
from Note import Note
chord = Chord.create(triad = "Major", root = Note.A)

print(Fingerprint(chord.stamp).stamp)
    
            

print(len(ft.fingerprints))
print([chord.name for chord in ft.retrieve("A,C#,F").chords])
print(ft.fingerprint("A,C#,F"))



sfs = ft.tree.stamps_at_suffix("G,B,C#,E")
print("\n All Stamps at G,B,C#,E: ", sfs)






## A Major Scale
sfs = ft.tree.stamps_at_suffix("E,G,B")
print("\n \n All Stamps at E,G,B: ", sfs)

fingerprint = ft.retrieve("E,G,B,D")
print(fingerprint.stamp)

print("\n Chords:")
for chord in fingerprint.chords:
    print(chord)

#print scales
print("\n Scales")
for scale in fingerprint.scales:
    print(scale)








#### get all stamps that are superstrings of suffix
superstrings = ft.tree.superstrings("E,G,B")
print("\n \n \n All Super Strings of E,G,B :", superstrings)

fp = ft.retrieve("E,G,B")
super_prints = ft.fingerprint_extensions(fp)
for fingerprint in super_prints:
    print("\n", fingerprint.stamp)

sfs = ft.tree.stamps_at_suffix("B,A,E")
print("\n \n All Stamps at B,A,E: ", sfs)


#if table.fingerprint("A,C,E"):

'''
'''
for stamp, fingerprint in ft.fingerprints.items():
    print("\n Chords for notes:", fingerprint.stamp)
    for chord in fingerprint.chords:
        print("\n \t ", chord.name)
        print("\n \t ", chord.notes)
'''


'''
#### I just relaized FingerprintTree is not working the way i thought, because 

#### superstrings and stamps_at_suffix wont return a match from B,E,G (E Minor) to B,D,E,G (Em7)

#### So I think we should get matches from B, then eliminate anything without an E and G and etc

sfs = ft.tree.stamps_at_suffix("B")
print("\n \n All Stamps at B:", len(sfs))

'''
## Yeah I think the suffix tree is a bust
## we can use unordered sets as the fingerprint table dictionary keys
## and just check if.subbset() at O(N) time
## then we can sort on some hierarchy later