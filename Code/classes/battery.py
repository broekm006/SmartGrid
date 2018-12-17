import math
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
        self.variance = 0
        self.cost = 5000

    def check_amp(self):
        ''' Check available space'''
        return self.max_amp - self.current_usage


    def add(self, housed):
        ''' add house to current_usage & connected list '''
        self.current_usage += housed.amp
        self.connected.append(housed)


    def remove(self, removed_house):
        ''' remove from current_usage & connected list '''
        self.current_usage -= removed_house.amp
        self.connected.remove(removed_house)

    def calculate_variance(self):

        # calculate mean distance from battery to connected houses
        # https://stackoverflow.com/questions/8102515/selecting-an-appropriate-similarity-metric-assessing-the-validity-of-a-k-means
        # https://www.mathsisfun.com/data/standard-deviation.html
        distances = []
        for house in self.connected:
            house.distance(self)
            distances.append(house.distance_to_battery)
        mean = sum(distances)/len(distances)

        # calculate the Variance
        differences = []
        for distance in distances:
            difference = math.pow((distance - mean), 2)
            differences.append(difference)

        self.variance = sum(differences)/len(differences)

    def __str__(self):
        return "id: " + str(self.id) + " X: " + str(self.x) + " Y: " + str(self.y) + " Max Amp: " + str(self.max_amp) + " List: " + str(self.connected)
