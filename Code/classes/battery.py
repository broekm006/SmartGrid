
class Battery(object):

    def __init__ (self, x, y, max_volt, current_usage):
        self.x = x
        self.y = y
        self.max_volt = max_volt
        self.current_usage = current_usage

    def check_volt(self):
        available = self.max_volt - self.current_usage
        
    def __str__(self):
        return str(self.x) + str(self.y) + str(self.max_volt)
