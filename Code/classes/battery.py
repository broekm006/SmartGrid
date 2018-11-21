from house import House

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
        ''' Check available space'''

        return self.max_amp - self.current_usage

    def add(self, house):
        ''' add house to current_usage & connected list '''
        self.current_usage += house.amp
        self.connected.append(house)

    def remove_hill(self, house_id, house_output):
        self.connected.remove(house_id)
        self.current_usage -= house_output

    def connect(self, house_id):
        self.connected.append(house_id)

    def remove(self, removed_house):
        ''' remove from current_usage & connected list '''
        self.current_usage -= removed_house.amp
        self.connected.remove(removed_house)

    def __str__(self):
        return "id: " + str(self.id) + " X: " + str(self.x) + " Y: " + str(self.y) + " Max Amp: " + str(self.max_amp) + " List: " + str(self.connected)
