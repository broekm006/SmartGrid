
class Battery(object):

    def __init__(self, id, x, y, max_amp):
        self.id = id
        self.x = x
        self.y = y
        self.max_amp = max_amp
        self.connected = []
        self.current_usage = 0

    def check_amp(self):
        return self.max_amp - self.current_usage

    def add(self, house_output):
        self.current_usage += house_output

    def connect(self, house_id):
        self.connected.append(house_id)

    def __str__(self):
        return str(self.id) + str(self.x) + str(self.y) + str(self.max_amp) + str(self.connected)
