

from operator import itemgetter

class House(object):

    def __init__ (self, id, x, y, amp):
        self.id = id
        self.x = x
        self.y = y
        self.amp = amp
        self.distance = []

    def connect (self, battery):
        ''' Save connected battery '''

        self.connected = battery

    def nearest(self, batteries):
        ''' Add list of ordered batteries to self.distance'''

        self.distance += batteries

    def cable_costs(self, battery_distance):
        ''' Calculate cable costs'''
        
        self.costs = 9 * battery_distance

    def __str__(self):
        return "ID:" + str(self.id) + "X:" + str(self.x) + " Y:" + str(self.y) + " AMP:" + str(self.amp)
