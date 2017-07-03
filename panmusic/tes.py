from Note import *
from Chord import *
from Scale import *
from Fretboard import Fretboard


def print_triads(triads):
    for triad in triads:
        print("\n Triad:", triad.root, triad.type)
        #print("\n \t", triad.root, triad.type)
    print("Triad Size:", len(triads))

def print_fretboard(fretboard):
    for string in fretboard.strings:
        print("String:", string)







#all triads, everywhere
triads = Triad.list()

print_triads(triads)



#all triads for Note: A
triads = Triad.list(root = Note.A)

print_triads(triads)

#all triads for type: Major
triads = Triad.list(triad = "Major")

print_triads(triads)



board = Fretboard()
print(board)


print_fretboard(board)

t = Chord.create(root = Note.E, triad = "Minor")

t.as_dict()

##print(Scale.fingerprints)

'''

#tetrad protoyping

#all tetrads, everywhere
tetrads = Tetrad.list()

#all tetrads for Note: A
tetrads = Tetrad.list(root = Note.A)

#all tetrads for triad type: Major
tetrads = Tetrad.list(triad = "Major")

#all tetrads that are dominant seven
tetrads = Tetrad.list(tetrad = "Dominant Seven")

#All tetrads that are dominant Seven and Major (E7, F7, F#7, G7, etc)
tetrads = Tetrad.list(tetrad = "Dominant Seven", triad = "Major")

#All tetrads that are dominant seven and and have root: A (A7, Am7, A7sus2, A7sus4, Aø7)
tetrads = Tetrad.list(tetrad = "Dominant Seven", note = Note.A)

#All tetrads with root: A that are a triad type of: Minor (Am7, Am6, A minor major 7)
tetrads = Tetrad.list(root = Note.A, triad = "Minor")

'''

