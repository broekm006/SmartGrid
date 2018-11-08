

class House(object):

    def __init__ (self, x, y, amp):
        self.x = x
        self.y = y
        self.amp = amp

    def __str__(self):
        return str(self.x) + str(self.y) + str(self.amp)
