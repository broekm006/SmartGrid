import sys
sys.path.append('Code/algoritmes')
from sort import Sort
from swap import Swap
from helper import Helper
import copy

class Random_connect(object):

    def __init__(self, houses, batteries):
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)
        self.connect()

    def connect(self):
        ''' Connect house to random battery with available capacity'''

        for house in self.houses:
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    house.connect(battery)

                    # update battery usage and connected list
                    battery.add(house)

                    # cable costs
                    battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)
                    house.cable_costs(battery.distance)

                    break;

        Swap.swap_hill_climber(Swap, self.houses, self.batteries)

        #BRUTE FORCE SWAP
        # Swap.check(Swap, self.houses, self.batteries)
