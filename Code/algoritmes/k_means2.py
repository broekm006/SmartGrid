import copy
import random
from greedy import Greedy
from helper import Helper
from solution import Solution
from sort import Sort

class K_means2(object):

    def __init__(self, houses, batteries):
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

    '''
    def run(self):
        for _ in range(100):
            self.clustering()
    '''

    def clustering(self, houses, batteries, counter):
        # count interations
        counter += 1

        # capacitated clustering
        greedy = Greedy(houses, batteries, "output")
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

            # print("ID: ", battery.id)
            # print("X: ", battery.x)
            # print("Y: ", battery.y)
            # print("Usage: ", battery.current_usage)
            # # print("Connected", *cluster.connected)
            # print()

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
                print()
            print("TOTAL COSTS: ", self.costs)
            print("Count: ", counter)
