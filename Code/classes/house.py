

from operator import itemgetter

class House(object):

    def __init__ (self, id, x, y, amp):
        self.id = id
        self.x = x
        self.y = y
        self.amp = amp
        self.connected = []
        self.distance = []

    def connect (self, battery_id):
        self.connected.append(battery_id)

    def nearest(self, batteries):
        ''' Add list of ordered batteries to self.distance'''
        
        self.distance += batteries

    def getKey(distance):
        return distance[0]

    def __str__(self):
        return "ID:" + str(self.id) + "X:" + str(self.x) + " Y:" + str(self.y) + " AMP:" + str(self.amp)
