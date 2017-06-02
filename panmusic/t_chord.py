from Note import *
from Chord import *

major_chord = Chord.create(root = Note.A, triad = "Major")
print("major",major_chord.inversion_intervals)


seven_chord = Chord.create(root = Note.A, triad = "Major", tetrad = "Major Seven")
print("Seven",seven_chord.inversion_intervals)




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