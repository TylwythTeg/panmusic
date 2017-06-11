from Note import *
from Chord import *
import collections 

major_chord = Chord.create(root = Note.A, triad = "Major")
#print("\nmajor",major_chord.inversion_intervals)


seven_chord = Chord.create(root = Note.A, triad = "Major", tetrad = "Major Seven")
#print("\nSeven",seven_chord.inversion_intervals)



#Make a class: Interval_fingerprint????? Fingerprint????
#seven_chord.fingerprint[1]

maj = Chord([Note.CSHARP, Note. A, Note. E, Note.FSHARP])
major_chord.fingerprint
maj.fingerprint


#print(major_chord.fingerprint)
#print(maj.fingerprint)

six = SixthChord("Major", Note.A)
#print(six.notes,"six",)
m7 = Chord.create(triad = "Minor", tetrad = "Dominant Seven", root = Note.FSHARP)
#print("m7 = 6?", m7.fingerprint == six.fingerprint)

if m7.notes[0] == "yadda":
	#prioritize assignments
	pass



#print("\n", six.fingerprint == maj.fingerprint)
#print("\n", maj.fingerprint == major_chord.fingerprint)


triads = Triad.create(root = Note.A, triad = "All")


#print("All Triads:",triads,"-----|")




#check fingerprints on tetrads

tetrads = Tetrad.create(root = Note.A, tetrad = "All")
#print("\n ALL TETRADS:",tetrads)

#print("\n A closer look:")

#first = True

fingerprints = {}
for tetrad in tetrads:
	if tetrad.fingerprint in fingerprints:
		#print("\n Found a match: ")
		#print("\n \t", fingerprints[tetrad.fingerprint], ":")
		uhm = fingerprints[tetrad.fingerprint]
		#print("\n \t \t ","Notes:", uhm.notes)
		#print("\n \t \t ","Triad:", uhm.triad)
		#print("\n \t \t ","Tetrad:", uhm.tetrad_type)

		#print("\n \t EQUALS", tetrad, ":")
		#print("\n \t \t ","Notes:", tetrad.notes)
		#print("\n \t \t ","Triad:", tetrad.triad)
		#print("\n \t \t ","Tetrad:", tetrad.tetrad_type)
	else:
		fingerprints[tetrad.fingerprint] = tetrad
		#print("\n", tetrad.root,tetrad.triad, tetrad.tetrad_type, tetrad.notes)


#print("\n ------------------------------------------------------")

tetrads = []
for note in Note:
	new_tetrads = Tetrad.create(root = note, tetrad = "All")
	tetrads += new_tetrads

fingerprints = {}
outlog = ""

for tetrad in tetrads:
	#if isinstance(tetrad, collections.ImmutableSequence):
		#print("SDFDSFSDFDSFSDFSDFSDFSDF")
	if tetrad.fingerprint in fingerprints:
		if isinstance(fingerprints[tetrad.fingerprint], list):
			#add to list
			fingerprints[tetrad.fingerprint].append(tetrad)
			#print("list")
		else:
			outlog += "\n Found a match: "
			outlog += "\n \t" + fingerprints[tetrad.fingerprint].__str__() + ":"

			#print("\n Found a match: ")
			#print("\n \t", fingerprints[tetrad.fingerprint], ":")
			uhm = fingerprints[tetrad.fingerprint]
			outlog += "\n \t \t Notes:" + uhm.notes.__str__()
			outlog += "\n \t \t Triad:" + uhm.triad.__str__()
			outlog += "\n \t \t Tetrad:" + uhm.tetrad_type
			#print("\n \t \t ","Notes:", uhm.notes)
			#print("\n \t \t ","Triad:", uhm.triad)
			#print("\n \t \t ","Tetrad:", uhm.tetrad_type)

			outlog += "\n \t [Equals] " + tetrad.__str__() + ":"
			outlog += "\n \t \t Notes:" + tetrad.notes.__str__()
			outlog += "\n \t \t Triad:" + tetrad.triad.__str__()
			outlog += "\n \t \t Tetrad:" + tetrad.tetrad_type
			#print("\n \t EQUALS", tetrad, ":")
			#print("\n \t \t ","Notes:", tetrad.notes)
			#print("\n \t \t ","Triad:", tetrad.triad)
			#print("\n \t \t ","Tetrad:", tetrad.tetrad_type)

			#make value of dict a list if it isn't
			fingerprints[tetrad.fingerprint] = [fingerprints[tetrad.fingerprint]]
			#add to this list
			fingerprints[tetrad.fingerprint].append(tetrad)
	else:
		fingerprints[tetrad.fingerprint] = tetrad
		#print("\n", tetrad.root,tetrad.triad, tetrad.tetrad_type, tetrad.notes)

#text_file = open("Output.txt", "w")
#text_file.write(outlog)
#text_file.close()


fingerprint_log = ""
for fingerprint in fingerprints:
	fingerprint_log += "\n Chords for notes: " + list(fingerprint).__str__()
	#tetrad = None
	if isinstance(fingerprints[fingerprint], list):	
		for tetrad in fingerprints[fingerprint]:
			fingerprint_log += "\n \t " + tetrad.__str__() + ":"
			fingerprint_log += "\n \t \t Triad: " + tetrad.triad.__str__()
			fingerprint_log += "\n \t \t Tetrad: " + tetrad.tetrad_type.__str__()
	else:
		tetrad = fingerprints[fingerprint]
		fingerprint_log += "\n \t " + tetrad.__str__() + ":"
		fingerprint_log += "\n \t \t Triad: " + tetrad.triad.__str__()
		fingerprint_log += "\n \t \t Tetrad: " + tetrad.tetrad_type.__str__()



new_file = open("tetrad_fingerprints.txt", "w")
new_file.write(fingerprint_log)
new_file.close()






#print(Chord.list("All"), "\n Length:", len(Chord.list("All")), "\n That was it")



'''

print(major_chord.intervals)
print(seven_chord.intervals)

print (Interval.MAJOR_THIRD.inversion())

print (Interval.MAJOR_SECOND.inversion())
print (Interval.MINOR_SEVENTH.inversion())
print (Interval.FOURTH.inversion())

print("------------------------")

for interval in major_chord.intervals:
	print(interval.inversion())

'''