class Solution(object):

    def __init__(self, houses, batteries):
        self.houses = houses
        self.batteries = batteries
        self.house_connected = {} #{battery.id : [house.id]}

        for battery in self.battaries:
            self.house_connected.setdefault(battery.id,[])

    #def add_to_connected(self, list):
    #    self.house_connected[self.batteries.id] = list

    # calculate distance between battery / house
    def distance_calc(self, house_id, battery_id):
        for battery in self.batteries:
            if battery.id == battery_id:
                for house in self.houses:
                    if house.id == house_id:
                        return abs(battery.y - house.y) + abs(battery.x - house.x)

    # calculate total distance for every house in battery
    def total_distance(self):
        total = 0
        for battery in self.batteries:
            for house in self.houses:
                if house.id in self.house_connected:
                    total += self.distance_calc(house.id, battery.id)
        return total
