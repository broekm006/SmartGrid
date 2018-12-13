from operator import itemgetter
# from battery import Battery

class House(object):

    def __init__ (self, id, x, y, amp):
        self.id = id
        self.x = x
        self.y = y
        self.amp = amp
        self.distance_to_battery = 0
        self.costs = 0
        self.priority_list = []
        self.connected = False
        self.connection = False
        # priority list for sort.priority_value


    def connect (self, battery):
        ''' Save connected battery '''
        self.connected = battery
        self.connection = True


    def cable_costs(self, battery_distance):
        ''' Calculate cable costs'''
        self.costs = 9 * battery_distance


    def distance(self, battery):
        self.distance_to_battery = abs(battery.y - self.y) + abs(battery.x - self.x)


    def __str__(self):
        return "ID:" + str(self.id) + "X:" + str(self.x) + " Y:" + str(self.y) + " AMP:" + str(self.amp)

        
