

from operator import itemgetter

class House(object):

    def __init__ (self, id, x, y, amp):
        self.id = id
        self.x = x
        self.y = y
        self.amp = amp
        self.connected = []

    def connect (self, battery_id):
        self.connected.append(battery_id)

    def distance (self, batteries):
        unsorted = []
        for battery in batteries:
            distance = abs(battery.y - self.y) + abs(battery.x - self.x)
            unsorted.append([distance, battery.id])

        return sorted(unsorted, key = itemgetter(0))

    def getKey(distance):
        return distance[0]
    def __str__(self):
        return "ID:" + str(self.id) + "X:" + str(self.x) + " Y:" + str(self.y) + " AMP:" + str(self.amp)
