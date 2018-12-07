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

    # Hill Climber
    def hc_solution(self):
        # ID > len resultst
        # list connected house / battery
        # costs > functie call
        #
        # self.results.append([self.batteries, self.houses])
        pass


    # K Means
    def km_solution(self):
        pass

    # Simulated Annealing
    def sa_solution(self):
        pass

    # Greedy
    def gr_solution(self):
        pass

    # Brute Force
    def br_solution(self):
        pass
    # calculate total distance for every house in battery
    def total_distance(self):
        total = 0
        for battery in self.batteries:
            for house in self.houses:
                if house.id in self.house_connected:
                    total += self.distance_calc(house.id, battery.id)
        return total

    def sort_houses(self, houses):
        sorted_houses = sorted(houses, key=lambda house: house.costs)

        #Expensive
        print("CHEAPEST & MOST EXPENSIVE HOUSE")
        print()
        battery = sorted_houses[0].connected
        print("House ID: ", sorted_houses[0].id)
        print("Output:   ", sorted_houses[0].amp)
        print("Battery:  ", battery.id)
        print("Costs:    ", sorted_houses[0].costs)
        print("Distance: ", sorted_houses[0].distance_to_battery)
        print()

        #Cheapest
        battery2 = sorted_houses[0].connected
        print("House ID: ", sorted_houses[-1].id)
        print("Output:   ", sorted_houses[-1].amp)
        print("Battery:  ", battery2.id)
        print("Costs:    ", sorted_houses[-1].costs)
        print("Distance: ", sorted_houses[-1].distance_to_battery)
        print()
        print()

    def calculate_costs(self):
        ''' Calculate total costs'''

        battery_costs = 0
        for battery in self.batteries:
            battery_costs += battery.cost

        # # Cable cable costs
        # cable_costs = 0
        # for house in houses:
        #     cable_costs += house.costs

        cable_costs = 0
        for house in self.houses:
            try:
                battery = house.connected
                house.distance_to_battery = abs(battery.y - house.y) + abs(battery.x - house.x)
                house.costs = house.distance_to_battery * 9
                cable_costs += house.costs
            except:
                print("Huis niet verbonden")
                pass

        # Total costs
        total_costs = battery_costs + cable_costs

        # TEST: costs
        print("COSTS")
        print()
        print("Battery costs: " + str(battery_costs))
        print("Cable costs: " + str(cable_costs))
        print("Total costs: " + str(total_costs))
        print()
        print()

        return total_costs

    def houses_costs(self, batteries, houses):
        cable_costs = 0
        for house in houses:
            cable_costs += house.costs

        return cable_costs

    def bounds(self, batteries, houses):
        ''' Upper- and lowerbounds for costs for given houses & batteries'''

        # solution class + update house.priority_list
        initial_solution = Solution(houses, batteries)
        Sort.priority_value(Sort, houses, batteries)

        lower = 0
        upper = 0
        for house in houses:
            b_close = house.priority_list[0]
            lower += initial_solution.distance_calc(house, b_close)

            b_far = house.priority_list[4]
            upper += initial_solution.distance_calc(house, b_far)

        lowerbound = lower * 9 + (batteries[0].cost * len(batteries))
        upperbound = upper * 9 + (batteries[0].cost * len(batteries))

        print("LOWERBOUND: " , lowerbound)
        print("UPPERBOUND: " , upperbound)
        print()
        print()
