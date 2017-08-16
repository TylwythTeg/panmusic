#middleman FingerprintTable
from Chord import Chord
from Note import Note


class Node():
    fingerprint = None
    #maybe when creating a node, create the Fingerprint("A,C,F") ##maybe not
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = dict()

        if data is not None:
            self.set_string()
    
    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(label = key, data = data)
        else:
            self.children[key.label] = key
    
    def __getitem__(self, key):
        return self.children[key]

class Trie():
    def __init__(self):
        self.head = Node()
    
    def __getitem__(self, key):
        return self.head.children[key]
    
    def add(self, word):
        fp_obj = None

        if isinstance(word, Fingerprint):
            fp_obj = word
            word = word.stamp

        current_node = self.head
        word_finished = True
        
        #convert to list of note strings
        word = word.split(",")



        print(len(word))
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break
        
        # For ever new letter, create a new child node
        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1
        
        # Let's store the full word at the end node so we don't need to
        # travel back up the tree to reconstruct the word
        current_node.data = word
        #fingerprint at end node of 
        if isinstance(fp_obj, Fingerprint):
                    current_node.fingerprint = fp_obj


    def add_chords(self):
        words = ""
        for chord in Chord.all():
            new_print = Fingerprint(chord.stamp)

            ####### change this to check if in trie, and then add to trie or manipulate fingerprint connected to that node

            if trie.has_word(new_print.stamp):
                f_obj = trie.fingerprint(new_print.stamp)
                f_obj.chords.append(chord)
            else:
                new_print = Fingerprint(chord.stamp)
                new_print.chords.append(chord)
                trie.add(new_print)
            
    
    def has_word(self, word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string')
        print("here")


        #word is now list of string
        word = word.split(",")
        print("----------hey look word is ", word)
        
        # Start at the top
        current_node = self.head
        exists = True
        for letter in word:
            print("----------hey look letter is ", letter)


            for child in current_node.children:
                print( child)

            #print(current_node.children)
            if letter in current_node.children:
                print("yes")
                current_node = current_node.children[letter]
            else:
                print("no")
                exists = False
                break
        
        # Still need to check if we just reached a word like 't'
        # that isn't actually a full word in our dictionary
        if exists:
            if current_node.data == None:
                exists = False
        
        return exists

    def all_fingerprints(self):
        words = list()

        for note in Note:
            note_words_debug = list()
            print("note", note)
            prefix = note.__str__()

            prefix = prefix.split(",")
        
            # Determine end-of-prefix node
            top_node = self.head
            for letter in prefix:
                if letter in top_node.children:
                    top_node = top_node.children[letter]
                else:
                    # Prefix not in tree, go no further
                    return words
            
            # Get words under prefix
            if top_node == self.head:
                queue = [node for key, node in top_node.children.items()]
            else:
                queue = [top_node]
            
            # Perform a breadth first search under the prefix
            # A cool effect of using BFS as opposed to DFS is that BFS will return
            # a list of words ordered by increasing length
            while queue:
                current_node = queue.pop()
                if current_node.fingerprint != None:
                    # Isn't it nice to not have to go back up the tree?
                    words.append(current_node.fingerprint)
                    note_words_debug.append(current_node.fingerprint)
                
                queue = [node for key,node in current_node.children.items()] + queue
            #print(note_words_debug)''
            for fingerprint in note_words_debug:
                print("\n ", fingerprint.id)
        
        return words
    
    def start_with_prefix(self, prefix):
        """ Returns a list of all words in tree that start with prefix """
        words = list()
        if prefix == None:
            raise ValueError('Requires not-Null prefix')

        #convert to list of note strings
        prefix = prefix.split(",")
        
        # Determine end-of-prefix node
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                # Prefix not in tree, go no further
                return words
        
        # Get words under prefix
        if top_node == self.head:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]
        
        # Perform a breadth first search under the prefix
        # A cool effect of using BFS as opposed to DFS is that BFS will return
        # a list of words ordered by increasing length
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                # Isn't it nice to not have to go back up the tree?
                words.append(current_node.data)
            
            queue = [node for key,node in current_node.children.items()] + queue
        
        return words

    def fingerprints_from_prefix(self, prefix):
        """ Returns a list of all words in tree that start with prefix """
        words = list()
        if prefix == None:
            raise ValueError('Requires not-Null prefix')

        #convert to list of note strings
        prefix = prefix.split(",")
        
        # Determine end-of-prefix node
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                # Prefix not in tree, go no further
                return words
        
        # Get words under prefix
        if top_node == self.head:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]
        
        # Perform a breadth first search under the prefix
        # A cool effect of using BFS as opposed to DFS is that BFS will return
        # a list of words ordered by increasing length
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                # Isn't it nice to not have to go back up the tree?
                words.append(current_node.fingerprint)
            
            queue = [node for key,node in current_node.children.items()] + queue
        
        return words
    
    def getData(self, word):
        """ This returns the 'data' of the node identified by the given word """
        if not self.has_word(word):
            raise ValueError('{} not found in trie'.format(word))
        
        # Race to the bottom, get data
        current_node = self.head
        for letter in word.split(","):
            current_node = current_node[letter]
        
        return current_node.data

    def getNode(self, word):
        """ This returns the 'data' of the node identified by the given word """
        if not self.has_word(word):
            raise ValueError('{} not found in trie'.format(word))
        
        # Race to the bottom, get data
        current_node = self.head
        for letter in word.split(","):
            current_node = current_node[letter]
        
        return current_node

    
    def set_string(self, word):
        if not self.has_word(word):
            """ This returns the string of the node identified by the given word """
            raise ValueError('{} not found in trie'.format(word))

        note_list = self.getData("A,C,F")

        notes = ",".join(note_list)
        print(notes)
        self.string_key = notes
        #print(len(notes))

    def fingerprint(self,word):
        """ This returns the the node identified by the given word """
        if not self.has_word(word):
            raise ValueError('{} not found in trie'.format(word))


        
        # Race to the bottom, get data
        current_node = self.head
        for letter in word.split(","):
            print("letter",letter)
            current_node = current_node[letter]
        
        return current_node.fingerprint




class Fingerprint():
    def __init__(self, stamp):
        self.stamp = stamp
        self.chords = []
        self.extensions = {}
            #####chord.neighbors = {}
        self.neighbors = {}

        ##frozen set of note is is currently id, not stamp so
        #get list of note strings
        print(stamp)
        self.id = stamp.split(",")

        #convert list of note strings to list of Notes
        self.id = [Note.from_string(note) for note in self.id]

        #make the frozenset of notes
        self.id = frozenset(self.id)

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, str):
            return self.id == other
        return self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)


    def __str__(self):
        return "\--------------------Fingerprint Object: " + self.id.__str__() + " " + self.chords.__str__()

    def print_chords(self):
        for chord in self.chords:
            print("\n Chord:", chord.name)







    def set_extension(self, fingerprint):
        length = len(fingerprint.id)

        
        if self.extensions.get(length, None) is None:
            self.extensions[length] = [fingerprint]
        else:
           self.extensions[length].append(fingerprint)



    def set_neighbor(self, fingerprint):
        print("\n \n \n Setting neighbor for", self.id, ":", fingerprint.id)




        new_note = fingerprint.id.difference(self.id)
        print("\n \t New Note:", new_note)
        #set fingerprint as neighbor if notes in fingerprint have one more note than the chord, dict where key is the new_note, and value is a fingerprint

        if len(fingerprint.id) == (len(self.id) + 1):
            #neighbors are one step away
            if self.neighbors.get(new_note, None) is None:
                self.neighbors[new_note] = fingerprint
            #else:
            #    self.neighbors[new_note].append(fingerprint)



        for added_note, neighbor in self.neighbors.items():
            print("\n \t \t Added note:", added_note, "Neighbor:", neighbor.id)



if __name__ == '__main__':
    trie = Trie()
    trie.add_chords()
    #####populate tree of fingerprints (and empty nodes)
    







    print ("'A,C,F' in trie: ", trie.has_word('A,C,F'))
    print (trie.start_with_prefix('A'))
    print (trie.start_with_prefix('to'))


    print(trie.start_with_prefix('A,C,F'))
    print("data", trie.getData('A,C,F'))


    trie.set_string('A,C,F')
    print ("'A,C,F' in trie: ", trie.has_word('A,C,F'))

    print("%%%%%%%%%%%%%%--------------sdsdf", trie.fingerprint('A,C,F').chords[0].name,trie.getData("A,C,F") )
    trie.fingerprint('A,C,F').print_chords()

    print("\n \n \n \n The A starters", len(trie.start_with_prefix("A")))


    sum = 0
    for note in Note:
        sum += len(trie.start_with_prefix(note.__str__()))
        print("\n \n \n \n \t \t \t \t The", note , "starters", len(trie.start_with_prefix(note.__str__())))
    print("total", sum)



    print(trie.fingerprint("A,C#,E").chords)


    print ("", trie.fingerprint('A,C#,F').chords)


    print ("!!!!!!!!!!!!!!!!!!!!!!!!", trie.start_with_prefix('A,C,E'))


    for item in trie.start_with_prefix("A,C,E"):
        print("sdfsdfseeeee")
        item = ",".join(item)
        fingerprint = trie.fingerprint(item)
        print("SDFSFFSDFSDF",fingerprint.chords)

    print ("!!!!!!!!!!!!!!!!!!!!!!!!", list(map(str,trie.fingerprints_from_prefix('A,C,E'))))

    ############Structuring Chord.extensions ###################################################

    #### def Trie.extensions(self,fingerprint)
    



       
        

    ############################################################################################




   
    





    def set_all_extensions():
        all_fingerprints = trie.all_fingerprints()
        print(len(all_fingerprints))

        #get all fingerprints in the trie and set neighbors and extensions
        for fingerprint in all_fingerprints:
            extended_fingerprints = trie.fingerprints_from_prefix(fingerprint.stamp)
            #####chord = fingerprint.chords[0]
            #previous_fingerprint is the one getting the extensions
            #previous_fingerprint = fingerprint
            
            

            #####chord.extensions = {}
            #fingerprint.extensions = {}
            #####chord.neighbors = {}
            #fingerprint.neighbors = {}

            for extension in extended_fingerprints:
                ####### right now prefix returns the prefix itself
                ####### until I fix that let's just weed out the prefix by checking if the lenfths are the same
                if len(extension.id) == len(fingerprint.id):
                    #print(extension.id, "===================================", fingerprint.id)
                    continue
                #set_extension(fingerprint, extension)        
                #set_neighbor(fingerprint, extension)

                fingerprint.set_extension(extension)
                fingerprint.set_neighbor(extension)



    set_all_extensions()


    trie.all_fingerprints()




    #### Trie debug
    '''
    fingerprint = trie.fingerprint("A,C,E")


    extended_fingerprints = trie.fingerprints_from_prefix(fingerprint.stamp)
    chord = fingerprint.chords[0]
    
    for key, fingerprints in fingerprint.extensions.items():
        print("Size:", key)

        for ffp in fingerprints:
            print("Chord:", ffp.chords[0].name)
            print(ffp.neighbors)




    #fingerprint = trie.fingerprint("C,E,G")
    for changed_note, fingerprints in fingerprint.neighbors.items():
        print("===Changed Note: \n", changed_note)

        for fingerprint in fingerprints:
            print("Chord:", fingerprint.chords[0].name)


    print(len(trie.all_fingerprints()))



    for fingerprint in trie.all_fingerprints():
        print("\n Fingerprint:",fingerprint.id)

        for changed_note, neighbor in fingerprint.neighbors.items():
            for fingerprint in fingerprints:
                print("\n \t Added Note:", changed_note)
                print("\n \t \t Chord:", fingerprint.chords[0].name, "Notes:", fingerprint.id)




    
    fingerprint = trie.fingerprint("C,E,G")
    print(fingerprint.neighbors)
    print(fingerprint.extensions)
    for added_note, fingerprints in fingerprint.neighbors.items():
        print("Added Note: \n", added_note)

        for fingerprint in fingerprints:
            print(fingerprint.id)
            print("Chord:", fingerprint.chords[0].name)


    print(len(trie.all_fingerprints()))
    '''
