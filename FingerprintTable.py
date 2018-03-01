from Chord import *
from Fingerprint import *
from Scale import Scale
from FingerprintTree import FingerprintTree
#import time

class FingerprintTable():
    chords = []
    scales = []

    fingerprints = {}

    ####### Returns whether or not stamp exists as a key in the fingerprints dictionary
    def fingerprint(self, stamp):
        return self.fingerprints.get(stamp, None) is not None

    ####### Returns self.fingerprints[stamp] or None if it is not found
    ####### Useage:
    #######     retrieve("A,C#,E")
    #######     retrieve(frozenset(Note.A, Note.CSHARP, Note.E))
    def retrieve(self, stamp):
        if isinstance(stamp, frozenset):
            return self.fingerprints.get(stamp, None)


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


    
    ### from fingerprint object, get a list of fingerprint extensions from a fingerprint
    def fingerprint_extensions(self, fingerprint):
        extensions = []
        for obj in self.fingerprints:
            if fingerprint.id.issubset(obj) and fingerprint.id != obj:
                extensions.append(self.retrieve(obj))
        return extensions


    def __init__(self):
        self.add_chords()
        self.add_scales()

        





ft = FingerprintTable()

print("----------",ft.retrieve("E,B,A").chords)

g = ft.retrieve("F#,A,C#")
print("----------RETRIEVE G,B,D EXTENSIONS----------")

print("Length: ",len(ft.fingerprint_extensions(g)))

for fingerprint in ft.fingerprint_extensions(g):
    print("\nFingerprint: ", fingerprint.stamp)

    print("\n \tChords:")
    for chord in fingerprint.chords:
        print("\n \t \t",chord.name)
    print("\n \tScales:")
    for scale in fingerprint.scales:
        print("\n \t \t",scale.name)
    

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