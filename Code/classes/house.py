

class House(object):

    def __init__ (self, x, y, volt):
        self.x = x
        self.y = y
        self.volt = volt

    def __str__(self):
        return str(self.x) + str(self.y) + str(self.volt)
