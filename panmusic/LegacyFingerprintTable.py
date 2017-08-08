from Chord import *
import time

class FingerprintTable():
    chords = None
    scales = None

    fingerprints = []

    def fingerprint_exists(self, note_set):
        if self.fingerprints.get(note_set, None) is None:
            return False
        else:
            return True



    def __init__(self):
        self.chords = []

        #change to generator for sure
        chords = Chord.all()

        for chord in chords:
            #if fingerprint exists, get current fingerprint to modify
            chord_fingerprint = Fingerprint(chord)

            print("---Our Chord---",frozenset(chord.notes))

            if chord_fingerprint in self.fingerprints:
                print("ever???????????????")
                print("first---",chord_fingerprint.id)
                index = self.fingerprints.index(chord_fingerprint)
                print("index",index)
                chord_fingerprint = self.fingerprints[index]
                if (chord not in chord_fingerprint.chords) and (chord.fingerprint == chord_fingerprint.id):
                    print("WE FOUND IT TRUE ADD THIS CHORD")
                    chord_fingerprint.chords.append(chord)
                print("-------------",chord_fingerprint.id)
                #if chord not in chord_fingerprint.chords:
                    #chord_fingerprint.chords.append(chord)
                for chord in chord_fingerprint.chords:
                    print(chord)

                #it's this equivalency
                


            #else create new fingerprint
            else:
                print("didnt exist before")
                print(chord.name)
                self.fingerprints.append(chord_fingerprint)


                

            time.sleep(.25)

            


            
            '''
            if frozenset(chord.notes) == chord_fingerprint.id:
                print("chord exists in footprint", chord_fingerprint.id , " and we should now add it to the list")
                print(chord_fingerprint.id)
                chord_fingerprint.chords.append(chord)
            else:
                print("no")
            '''
            #self.chords.append(chord)

            #if chord_fingerprint.id == chord.fingerprint:
            #    chord_fingerprint.chords.append(chord)

        #print(len(self.fingerprints))
            

