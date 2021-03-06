import copy, random
from greedy import Greedy
from helper import Helper
from solution import Solution
from sort import Sort

class K_means2(object):

    def __init__(self, houses, batteries, greedy, random):
        self.houses = houses
        self.batteries = batteries
        self.costs = float('Inf')
        self.counter = 0
        self.greedy = greedy
        self.random_batteries = random
        self.solutions = []
        if self.random_batteries == "random":
            self.random(self.batteries)
        self.clustering(self.houses, self.batteries, self.counter)

    def random(self, batteries):
        ''' Random cluster centroids'''

        for battery in batteries:
            battery.x = random.randint(0, 50)
            battery.y = random.randint(0, 50)

    def clustering(self, houses, batteries, counter):
        ''' Use K-means to cluster and assign houses to batteries '''

        # count clustering iterations
        counter += 1

        # capacitated clustering
        greedy = Greedy(houses, batteries, self.greedy)
        houses = copy.deepcopy(greedy.houses)
        batteries = copy.deepcopy(greedy.batteries)

        # Save solution
        solution = Solution(copy.deepcopy(houses), copy.deepcopy(batteries))
        self.solutions.append(solution)

        for battery in batteries:
            houses = Sort.distance(Sort, houses, battery)

        # calculate cable costs
        cable_costs = Helper.houses_costs(Helper, batteries, houses)
        battery_costs = 0
        for battery in batteries:
            battery_costs += battery.cost
        costs = cable_costs + battery_costs

        # for each cluster, new centre = means of all connected houses coördinates
        for battery in batteries:
            x = 0
            y = 0
            count  = 0

            for house in battery.connected:
                x += house.x
                y += house.y
                count += 1

            # Avoid dividing by zero battery is not connected to any house (HAC)
            if count != 0:
                # average
                mean_x = round(x / count)
                mean_y = round(y / count)

                # new centre
                battery.x = mean_x
                battery.y = mean_y

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
            pass

    def results(self):
        ''' Print result and new upper- and lowerbound after K-means'''

        print()
        print("UPPER & LOWERBOUNDS AFTER K-MEANS:")
        k_means_solution = Solution(self.houses, self.batteries)
        costs = k_means_solution.calculate_costs2()
        k_means_solution.bounds(self.batteries, self.houses)

        print()
        print("TOTAL COSTS AFTER K-MEANS: ", costs)


    def csv_output(self):
        ''' Create .CSV file for K Means '''
        with open("resultaten/K_means.csv", mode = 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["costs", "upperbound", "lowerbound"])

            for result in self.results:
                csv_writer.writerow(result)
