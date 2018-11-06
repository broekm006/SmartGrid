
class Battery(object):

    def __init__ (self, x, y, max_volt):
        self.x = x
        self.y = y
        self.max_volt = max_volt


    def __str__(self):
        return str(self.x) + str(self.y) + str(self.max_volt)
