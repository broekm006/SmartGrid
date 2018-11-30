# cluster houses and place battery in the middle
# in progress
# caminess

import sys
sys.path.append('Code/algoritmes')
from sort import Sort
from swap import Swap
from helper import Helper
import copy

sys.path.append('Code/classes')
from visualizer import Visualizer



class K_means(object):

    def __init__(self, houses, batteries):
        self.houses = houses
        self.batteries = batteries
        self.cluster()

    def cluster(self):

        # connect all houses to first battery
        for house in self.houses:
            for battery in self.batteries:

                if house.connection == False:
                    house.connect(battery)
                    battery.add(house)

        while True:

            # make copy for  comparison
            current_houselist = copy.deepcopy(self.houses)

            # connect battery to nearest house
            for house in self.houses:
                for battery in self.batteries:

                    # check distances
                    current_distance = abs(house.connected.y - house.y) + abs(house.connected.x - house.x)
                    checking_distance = abs(battery.y - house.y) + abs(battery.x - house.x)

                    # if checking distance is smaller than current distance replace battery
                    if checking_distance < current_distance:
                        house.connect(battery)
                        print("House " + str(house.id) + " connected to Battery " + str(battery.id) + ".")

                        # remove house from old battery
                        for old_battery in self.batteries:
                            if house in old_battery.connected:
                                old_battery.remove(house)

                        # battery lijst moet weer leeg bij nieuwe iteratie, niet eindeloos oppenden?
                        battery.add(house)

            if current_houselist == self.houses:
                print("break")
                break

            batterynumber = 0

            for battery in self.batteries:

                print("The battery is: "+ str(batterynumber))
                print(*battery.connected)

                # create list with x and y coordinates of connected houses
                houses_x = []
                houses_y = []

                # add values
                for house in battery.connected:
                    houses_x.append(house.x)
                    houses_y.append(house.y)

                print(houses_x)
                print(houses_y)

                print(sum(houses_x), len(houses_x))
                print(sum(houses_y), len(houses_y))

                # calculate middle
                average_x = round(sum(houses_x)/len(houses_x))
                average_y = round(sum(houses_y)/len(houses_y))

                print(average_x)
                print(average_y)

                # move battery
                battery.x = average_x
                battery.y = average_y

                batterynumber += 1

        #     print("ID: " + str(house.id))
        #     print("X: " + str(house.x))
        #     print("Y: " + str(house.y))
        #     print("Connected battery: " + str(house.connected.id))
        #
        # Visualizer(self.houses, self.batteries)
