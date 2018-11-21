class Solution(object):

    def __init__(self, houses, batteries):
        self.houses = houses
        self.batteries = batteries
        self.house_connected = {} #{battery.id : [house.id]}

        for battery in self.batteries:
            self.house_connected.setdefault(battery.id,[])

    #def add_to_connected(self, list):
    #    self.house_connected[self.batteries.id] = list

    # calculate distance between battery / house
    def distance_calc(self, house, battery):
        return abs(battery.y - house.y) + abs(battery.x - house.x)

    # calculate total distance for every house in battery
    def total_distance(self):
        total = 0
        for battery in self.batteries:
            for house in self.houses:
                if house.id in self.house_connected:
                    total += self.distance_calc(house.id, battery.id)
        return total
