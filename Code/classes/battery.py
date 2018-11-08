
class Battery(object):

    def __init__ (self, x, y, max_amp):
        self.x = x
        self.y = y
        self.max_amp = max_amp
        self.current_usage

    def check_volt(self):
        available = self.max_amp - self.current_usage

    # def current_use

    def __str__(self):
        return str(self.x) + str(self.y) + str(self.max_amp)
