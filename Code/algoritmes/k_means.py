<<<<<<< HEAD
import copy
import random
from greedy import Greedy
from helper import Helper
from solution import Solution
from sort import Sort
=======
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


>>>>>>> 65d2120339e638fa8f4eaf908de42c492642069b

class K_means(object):

    def __init__(self, houses, batteries):
<<<<<<< HEAD
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)
        self.costs = float('Inf')
        self.counter = 0
        # self.random(self.batteries)
        self.clustering(self.houses, self.batteries, self.counter)

    def random(self, batteries):
        ''' Random cluster centroids'''

        for battery in batteries:
            battery.x = random.randint(0, 50)
            battery.y = random.randint(0, 50)


    def clustering(self, houses, batteries, counter):
        # count interations
        counter += 1

        # capacitated clustering
        greedy = Greedy(houses, batteries, "priority")
        houses = copy.deepcopy(greedy.houses)
        batteries = copy.deepcopy(greedy.batteries)

        for battery in batteries:
            houses = Sort.distance(Sort, houses, battery)

        # calculate  cable costs
        costs = Helper.houses_costs(Helper, batteries, houses)
        costs += 5 * 5000   #NOG VERANDEREN
        print(costs)

        # for each cluster, new centre = means of all points x
        for battery in batteries:
            x = 0
            y = 0
            counter = 0

            for house in battery.connected:
                x += house.x
                y += house.y
                counter += 1

            # average
            mean_x = round(x / counter)
            mean_y = round(y / counter)

            # new centre
            battery.x = mean_x
            battery.y = mean_y

            print("ID: ", battery.id)
            print("X: ", battery.x)
            print("Y: ", battery.y)
            print("Usage: ", battery.current_usage)
            # print("Connected", *cluster.connected)
            print()

        # Stops when costs haven't changed
        if costs < self.costs:
            self.costs = costs

            # disconnect
            for battery in batteries:
                battery.connected = []
                battery.current_usage = 0

            for house in houses:
                house.connected = False
                house.connection = False
                house.costs = 0

            # --> Solution
            self.batteries = batteries
            self.houses = houses

            # try again
            self.clustering(houses, batteries, counter)
        else:
            print("EINDRESULTAAT")
            for battery in self.batteries:
                print("ID: ", battery.id)
                print("X: ", battery.x)
                print("Y: ", battery.y)
                print("Amount:", len(battery.connected))
                print("Usage: ", battery.current_usage)
            print("TOTAL COSTS: ", self.costs)
            print("Count: ", counter)
=======
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

                        # battery lijst moet weer leeg bij nieuwe iteratie, niet eindeloos oppenden?
                        battery.add(house)

                        # remove house from old battery
                        for old_battery in self.batteries:
                            if house in old_battery.connected:
                                old_battery.remove(house)

                print(house.connected)

            if current_houselist == self.houses:
                print("break")
                break

            batterynumber = 0

            for battery in self.batteries:

                batterynumber += 1
                print("The battery is: "+ str(batterynumber))

                # create list with x and y coordinates of connected houses
                houses_x = []
                houses_y = []

                # add values
                for house in battery.connected:
                    houses_x.append(house.x)
                    houses_y.append(house.y)

                print (houses_x)
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



            print("ID: " + str(house.id))
            print("X: " + str(house.x))
            print("Y: " + str(house.y))
            print("Connected battery: " + str(house.connected.id))

        Visualizer(self.houses, self.batteries)
>>>>>>> 65d2120339e638fa8f4eaf908de42c492642069b
