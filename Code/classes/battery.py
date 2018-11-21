
class Battery(object):

    def __init__(self, id, x, y, max_amp):
        self.id = id
        self.x = x
        self.y = y
        self.max_amp = max_amp
        self.connected = []
        self.current_usage = 0
        self.distance = 0
        self.cost = 5000 # kan later worden meegegeven

    def check_amp(self):
        return self.max_amp - self.current_usage

    def add(self, house_output):
        self.current_usage += house_output

    def remove(self, house_id, house_output):
        self.connected.remove(house_id)
        self.current_usage -= house_output

    def connect(self, house_id):
        self.connected.append(house_id)

    def __str__(self):
        return "id: " + str(self.id) + " X: " + str(self.x) + " Y: " + str(self.y) + " Max Amp: " + str(self.max_amp) + " List: " + str(self.connected)
