import sys, copy
sys.path.append('Code/algoritmes')

from sort import Sort
from swap import Swap
from helper import Helper

class Greedy(object):

    def __init__(self, houses, batteries, variant):
        self.houses = houses
        self.batteries = batteries
        self.variant = self.type(variant)

    def type(self, type):
        ''' Checks which version of greedy will be used'''

        if type == "output":
            self.output()
        elif type == "distance":
            self.distance()
        elif type == "priority":
            self.pv()
        else:
            print("Greedy type error")


    def output(self):
        ''' Connect house to nearest battery with available capacity'''

        self.houses = Sort.max_output(Sort, self.houses)

        for house in self.houses:
            for battery in self.batteries:
                battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)

            self.batteries = sorted(self.batteries, key=lambda battery: battery.distance)

            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    house.connect(battery)

                    # update battery usage and connected list
                    battery.add(house)

                    # cable costs
                    battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)
                    house.cable_costs(battery.distance)

                    break;

        # HILL CLIMBER SWAP
        Swap.swap_hill_climber(Swap, self.houses, self.batteries)


    def distance(self):
        ''' Connect house to nearest battery with available capacity'''

        for battery in self.batteries:

            # sorts houses based on distance to current battery
            self.houses = Sort.distance(Sort, self.houses, battery)

            # connect battery to nearest house that isn't connected
            for house in self.houses:
                if battery.check_amp() > house.amp and not house.connection:

                    # distance
                    distance = abs(battery.y - house.y) + abs(battery.x - house.x)

                    # Update battery usage & cable costs
                    battery.add(house)
                    house.connect(battery)
                    house.cable_costs(distance)

        # HILL CLIMBER SWAP
        Swap.swap_hill_climber(Swap, self.houses, self.batteries)


    def pv(self):
        ''' Connect house to nearest battery with available capacity'''

        # sorts houses based on priority value
        self.houses = Sort.priority_value(Sort, self.houses, self.batteries)
        for house in self.houses:

            # sorts batteries based on distance from current house --> kan nog apart
            for battery in self.batteries:
                battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)

            self.batteries = sorted(self.batteries, key=lambda battery: battery.distance)

            # connect house to nearest available battery
            for battery in self.batteries:
                if battery.check_amp() > house.amp:

                    # Update connections, current usage & cable costs
                    house.connect(battery)
                    battery.add(house)
                    house.cable_costs(battery.distance)
                    break;

        # HILL CLIMBER SWAP
        Swap.swap_hill_climber(Swap, self.houses, self.batteries)
