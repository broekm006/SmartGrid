import copy, random
from greedy import Greedy
from helper import Helper
from solution import Solution
from sort import Sort

class K_means2(object):

    def __init__(self, houses, batteries, greedy, random):
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)
        self.costs = float('Inf')
        self.counter = 0
        self.greedy = greedy
        self.random_batteries = random
        if self.random_batteries == "random":
            self.random(self.batteries)
        self.clustering(self.houses, self.batteries, self.counter)

    def random(self, batteries):
        ''' Random cluster centroids'''

        for battery in batteries:
            battery.x = random.randint(0, 50)
            battery.y = random.randint(0, 50)

    def clustering(self, houses, batteries, counter):
        '''Use K-means to cluster and assign houses to batteries '''
        # count interations
        counter += 1

        while(True):
            # capacitated clustering
            greedy = Greedy(houses, batteries, self.greedy)
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

                # new center
                battery.x = mean_x
                battery.y = mean_y

            # Stops when costs haven't changed
            if costs > self.costs:
                break

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

    def csv_output(self):
        ''' Create .CSV file for K Means '''
        with open("resultaten/K_means.csv", mode = 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["costs", "upperbound", "lowerbound"])

            for result in self.results:
                csv_writer.writerow(result)
