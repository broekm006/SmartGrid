

from operator import itemgetter

class House(object):

    def __init__ (self, id, x, y, amp):
        self.id = id
        self.x = x
        self.y = y
        self.amp = amp
        self.battery = 0
        self.connected = False
        self.costs = 0
        self.keuze = 100

        # self.nearest = []

    def connect (self, battery):
        ''' Save connected battery '''

        self.battery = battery
        self.connected = True


    def cable_costs(self, battery_distance):
        ''' Calculate cable costs'''

        self.costs = 9 * battery_distance

    def prioritize(self, batteries):
        self.priority_list = batteries

    def priority_value(self, first_distance, second_distance):

        self.pv = second_distance - first_distance

    def voorkeur():
        for i, battery in enumerate(self.priority_list):
            if self.battery == battery:
                break
        self.keuze = int(i)

    def __str__(self):
        return "ID:" + str(self.id) + "X:" + str(self.x) + " Y:" + str(self.y) + " AMP:" + str(self.amp)
