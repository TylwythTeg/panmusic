from STree import STree
from Chord import Chord

class FingerprintTree(STree):

    @staticmethod
    def replace_sharps(string):
        normalized = ""
        for note in string:
            normalized += FingerprintTree.normalize_note(note)
        return normalized
    
    @staticmethod
    def sharpify_string(string, add_comma = False):
        sharpified = ""
        for note in string:
            sharpified += FingerprintTree.sharpify_note(note)
            if add_comma:
                sharpified += ","
        return sharpified

    @staticmethod
    def normalize_note(note):
        normalizations = {
            "A": "A",
            "A#": "S",### A Sharp = S
            "S": "S",
            "B": "B",
            "C": "C",
            "C#": "T",### C Sharp = T
            "T": "T",
            "D": "D",
            "D#": "U",### D Sharp = U
            "U": "U",
            "E": "E",
            "F": "F",
            "F#": "V",### F Sharp = V
            "V": "V",
            "G": "G",
            "G#": "W",### G SHarp = W
            "W": "W",
        }
        return normalizations.get(note)

    @staticmethod
    def sharpify_note(note):
        sharpifications = {
            "A": "A",
            "S": "A#",### A Sharp = S
            "B": "B",
            "C": "C",
            "T": "C#",### C Sharp = T
            "C#": "C#",
            "D": "D",
            "U": "D#",### D Sharp = U
            "D#": "D#",
            "E": "E",
            "F": "F",
            "V": "F#",### F Sharp = V
            "F#": "F#",
            "G": "G",
            "W": "G#",### G SHarp = W
            "G#": "G#"
        }
        return sharpifications.get(note)

    #### Used for sorting purposes
    @staticmethod
    def get_value(char):
            values = {
            "A" : 0,
            "A#": 1,
            "S": 1,
            "B": 2,
            "C": 3,
            "C#": 4,
            "T": 4,
            "D": 5,
            "D#": 6,
            "U": 6,
            "E": 7,
            "F": 8,
            "F#": 9,
            "V": 9,
            "G": 10,
            "G#": 11,
            "W": 11,
            }
            return values.get(char)

    def __init__(self):

        stamp_list = []
        #####Chord Fingerprints
        wow = False
        for chord in Chord.all():
            if chord.name == "E Minor Major Six":
                print("wow")
                wow = True
            #print(chord.notes, chord.name)
            stamp = chord.stamp
            #get a list of the note strings
            stamp = stamp.split(",")
            #replace sharps with single-char equivalents
            stamp = FingerprintTree.replace_sharps(stamp)


            if stamp not in stamp_list:
                if wow:
                    print("yesss")
                    wow = False
                stamp_list.append(stamp)

        #self.tree = STree(stamp_list)
        super().__init__(stamp_list)



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

    #takes raw comma'd stamp ie "A,C#,E"
    def superstrings(self, public_stamp):

        stamp = public_stamp.split(",")
        stamp = self.replace_sharps(stamp)
        ##now we have the normalized "ATE" stamp
        ##we should sort it so that people can check notes out of order
        print(stamp)
        stamp = "".join(sorted(stamp, key = FingerprintTree.get_value))
        print(stamp)


        superstrings = []
        for superstring in self.get_superstrings(stamp):
            superstring = ",".join(superstring)
            superstring = superstring.split(",")
            superstring = self.sharpify_string(superstring, add_comma = True)
            #-1 to remove the comma that the above adds to the last element
            superstrings.append(superstring[:-1])


        return superstrings

    #### takes the raw normalized stamp ie "ATE"
    #### for internal purposes
    def get_superstrings(self, y):
        stamps = self.stamps_from_suffix(y)

        ### Remove the element that is the string we're getting a superstring for
        superstrings = []
        for string in stamps:
            if string != y:
                superstrings.append(string)
        return superstrings

    ####public facing get all stamps from this suffix
    def stamps_at_suffix(self, public_stamp):
        stamp = public_stamp.split(",")
        stamp = self.replace_sharps(stamp)

        ##now we have the normalized "ATE" stamp
        ##we should sort it so that people can check notes out of order
        stamp = "".join(sorted(stamp, key = FingerprintTree.get_value))

        stamps = []
        for superstring in self.stamps_from_suffix(stamp):
            superstring = ",".join(superstring)
            superstring = superstring.split(",")
            superstring = self.sharpify_string(superstring, add_comma = True)
            #-1 to remove the comma that the above adds to the last element
            stamps.append(superstring[:-1])


        return stamps



        return self.stamps_from_suffix(stamp)
    
    ### internal function that takes raw stamp ("ATE") and gets all valid stamps that live there
    def stamps_from_suffix(self, y):
        #y = FingerprintTree.replace_sharps(y)
        y_input = y
        #node = self.tree.root
        node = self.root
        while True:
            edge = self._edgeLabel(node, node.parent)
            if edge.startswith(y):
                break
            else:
                i = 0
                while(i < len(edge) and edge[i] == y[0]):
                    y = y[1:]
                    i += 1
            node = node._get_transition_link(y[0])
            if not node:
                return []
        leaves = node._get_leaves()
        return [self.full_stamp_from_index(n.idx) for n in leaves]

    
    #input an index to fing the full string for that index
    def coordinates_from_index(self,index):        
        start = self.get_beginning(index)
        end = self.get_end(index)
 
        return (start, end)
    #get the string at coordinates
    def stamp_from_coordinates(self, coords):
        return self.word[coords[0] : coords[1]]

    def full_stamp_from_index(self, index):
        coords = self.coordinates_from_index(index)
        stamp = self.stamp_from_coordinates(coords)
        return stamp

    def get_beginning(self, index):
        #no footprint would be more than 12 characters in length, and we just want to scan a small part
        word = self.word[index - 12 : index]
        #reverse it so we can trawl it backwards
        word = word[::-1]

        i = 0
        for char in word:
            if self.is_terminal(char):
                break
            i += 1

        beginning = index - i
        return beginning

    def get_end(self, index):

        #no footprint would be more than 12 characters in length, and we just want to scan a small part
        word = self.word[index:index + 12]

        i = 0
        for char in word:
            if self.is_terminal(char):
                break
            i += 1

        end = index + i
        return end









ft = FingerprintTree()

#### get all the stamps that have suffix
sfs = ft.stamps_at_suffix("G,B,C#,E")
print("\n All Stamps at C,E,G: ", sfs)

#### get all stamps that are superstrings of suffix
superstrings = ft.superstrings("A")
print("\n \n \n All Super Strings of C#,E,G :", superstrings)

