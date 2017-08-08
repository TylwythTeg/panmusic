

class Fingerprint():
    id = None
    chords = []
    scales = []

    #pass a chord or scale
    def __init__(self, musical_object):
        self.id = musical_object.fingerprint

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)







