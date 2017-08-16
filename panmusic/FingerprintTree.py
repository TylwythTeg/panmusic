from STree import STree
from Chord import Chord

class FingerprintTree():

    @staticmethod
    def replace_sharps(string):
        normalized = ""
        for note in string:
            normalized += FingerprintTree.normalize_note(note)
        return normalized

    @staticmethod
    def normalize_note(note):
        normalizations = {
            "A": "A",
            "A#": "S",### A Sharp = S
            "B": "B",
            "C": "C",
            "C#": "T",### C Sharp = T
            "D": "D",
            "D#": "U",### D Sharp = U
            "E": "E",
            "F": "F",
            "F#": "V",### F Sharp = V
            "G": "G",
            "G#": "W",### G SHarp = W
        }
        return normalizations.get(note)

    def __init__(self):

        stamp_list = []
        #####Chord Fingerprints
        for chord in Chord.all():
            stamp = chord.stamp
            #get a list of the note strings
            stamp = stamp.split(",")
            #replace sharps with single-char equivalents
            stamp = FingerprintTree.replace_sharps(stamp)


            if stamp not in stamp_list:
                stamp_list.append(stamp)

        self.tree = STree(stamp_list)



    def is_terminal(self, char):
        valid_chars = {
            "A": False,
            "S": False,### A Sharp = S
            "B": False,
            "C": False,
            "T": False,### C Sharp = T
            "D": False,
            "U": False,### D Sharp = U
            "E": False,
            "F": False,
            "V": False,### F Sharp = V
            "G": False,
            "W": False,### G SHarp = W
        }
        return valid_chars.get(char, True)

    #####function assumes you are supplying notes to find where in the string this full text is fingerprint stamp is located
    ## TODO: will need to do one that takes a suffix and returns all full indexes of the superstrings (fingerprints) that the suffix is in (for extensions)
    def get_full_index(self, y):
        """Returns a tuple of the starting index and ending index of the substring y in the string used for
        building the Suffix tree.

        :param y: String
        :return: Index of the starting position of string y in the string used for building the Suffix tree
                 -1 if y is not a substring.


        """
        tree = self.tree
        node = tree.root
        while True:
            edge = tree._edgeLabel(node, node.parent)
            #check
            if edge.startswith(y):
                return (node.idx, self.get_outdex(node.idx))

            i = 0
            while(i < len(edge) and edge[i] == y[0]):
                y = y[1:]
                i += 1
            node = node._get_transition_link(y[0])
            if not node:
                return -1 

    
    def get_outdex(self, index):

        #no footprint would be more than 12 characters in length, and we just want to scan a small part
        word = self.tree.word[index:index + 12]

        i = 0
        for char in word:
            if self.is_terminal(char):
                break
            i += 1

        outdex = index + i
        return outdex
    ######## FingerprintTree.py methods ########








ft = FingerprintTree()

print(ft.get_full_index("ATE"))