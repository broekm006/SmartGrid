

class House(object):

    def __init__ (self, id, x, y, amp):
        self.id = id
        self.x = x
        self.y = y
        self.amp = amp
        self.connected = []

    def connect (self, battery_id):
        self.connected.append(battery_id)

    def __str__(self):
<<<<<<< HEAD
        return str(self.id) + str(self.x) + str(self.y) + str(self.amp)
=======
        return "X:" + str(self.x) + " Y:" + str(self.y) + " AMP:" + str(self.amp)
>>>>>>> 377722b227824ae81871075ef3e4621f1d7f3fc2
