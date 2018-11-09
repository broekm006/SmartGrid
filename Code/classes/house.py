

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
        return "X:" + str(self.x) + " Y:" + str(self.y) + " AMP:" + str(self.amp)
