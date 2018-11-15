

from operator import itemgetter

class House(object):

    def __init__ (self, id, x, y, amp):
        self.id = id
        self.x = x
        self.y = y
        self.amp = amp
        self.battery = 0
        self.connected = False

    def connect (self, battery):
        ''' Save connected battery '''

        self.battery = battery
        self.connected = True

    def distance (self, batteries):
        ''' Calculate distance from house to each battery'''

        distances = []
        for battery in batteries:
            distance = abs(battery.y - self.y) + abs(battery.x - self.x)
            distances.append(distance)

        self.b1_distance = int(distances[0])
        self.b2_distance = int(distances[1])
        self.b3_distance = int(distances[2])
        self.b4_distance = int(distances[3])
        self.b5_distance = int(distances[4])

    def cable_costs(self, battery_distance):
        ''' Calculate cable costs'''

        self.costs = 9 * battery_distance

    def __str__(self):
        return "ID:" + str(self.id) + "X:" + str(self.x) + " Y:" + str(self.y) + " AMP:" + str(self.amp)
