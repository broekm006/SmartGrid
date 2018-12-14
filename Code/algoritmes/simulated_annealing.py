import random, copy
from solution import Solution
<<<<<<< HEAD
# from visualizer import Visualizer
=======
from frequency_visualizer import Frequency_visualizer
>>>>>>> 93b363af56e4b91f77635d7c8947de2681429cd3

class Simulated_annealing(object):

    def __init__(self, houses, batteries, number_of_runs):
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)
        self.n = number_of_runs
        self.results = []
        self.results2 = []

        self.multi_results = []
        self.simulatie_V2()

    def simulatie_V2(self):
        ''' Use Simulated Annealing to make changes to the existing solution '''
        for count in range(self.n):
            temp_batteries = copy.deepcopy(self.batteries)
            temp_houses = copy.deepcopy(self.houses)

            counter = 0
            temp_batteries = sorted(temp_batteries, key=lambda battery: battery.id)

            # temperature function to determine the number of times the algorithm runs --> 10060 times with 0.0000000000000000000000000000000000000000000001
            T = 1.0
            T_min = 0.0000000000000000000000000000000000000000000001
            alpha = 0.9

            # while temp is higher than minimal temp.
            while T > T_min:
                i = 1
                # loop throug algorithm for number_of_times
                for i in range(self.n):
                    random_battery = random.choice(temp_batteries)
                    random_battery2 = random.choice(temp_batteries)

                    # make sure 2 different batteries are chosen
                    while random_battery == random_battery2:
                        random_battery2 = random.choice(temp_batteries)

                    #choose 2 random houses from the batteries
                    random_house_in_battery = random.choice(random_battery.connected)
                    random_house_in_battery2 = random.choice(random_battery2.connected)

                    #remove "lowest id + update current_usage"
                    temp_batteries[random_battery.id].remove(random_house_in_battery)
                    temp_batteries[random_battery2.id].remove(random_house_in_battery2)

                    max = temp_batteries[random_battery.id].max_amp
                    currents1 = temp_batteries[random_battery.id].current_usage
                    currents2 = temp_batteries[random_battery2.id].current_usage

                    # calculate distance
                    solution = Solution(temp_houses, temp_batteries)
                    solution.distance_calc(random_house_in_battery, random_battery)

                    old_distance = solution.distance_calc(random_house_in_battery, random_battery)
                    old_distance2 = solution.distance_calc(random_house_in_battery2, random_battery2)

                    new_distance = solution.distance_calc(random_house_in_battery, random_battery2)
                    new_distance2 = solution.distance_calc(random_house_in_battery2, random_battery)

                    if  max - (currents1 + random_house_in_battery2.amp) > 0 and max - (currents2 + random_house_in_battery.amp) > 0:
                        #add removed house to other battery_id
                        if old_distance + old_distance2 > new_distance + new_distance2:
                            temp_batteries[random_battery.id].add(random_house_in_battery2)
                            temp_batteries[random_battery2.id].add(random_house_in_battery)
                            random_house_in_battery.connect(temp_batteries[random_battery2.id])
                            random_house_in_battery2.connect(temp_batteries[random_battery.id])

                        else:
                            #undo remove because the switch does not work (battery overload)
                            temp_batteries[random_battery.id].add(random_house_in_battery)
                            temp_batteries[random_battery2.id].add(random_house_in_battery2)

                    else:
                        #undo remove because the switch does not work (battery overload)
                        temp_batteries[random_battery.id].add(random_house_in_battery)
                        temp_batteries[random_battery2.id].add(random_house_in_battery2)

                    # add room for negative distance
                    if T > 0.1:
                        new_distance - 15
                        new_distance2 - 15
                    elif T < 0.00001:
                        new_distance - 10
                        new_distance2 - 10
                    elif T < 0.000000001:
                        new_distance - 5
                        new_distance2 - 5
                    elif T < 0.0000000000000001:
                        new_distance - 2
                        new_distance2 - 2
                    counter += 1
                    i += 1
                T = T*alpha

                # replace houses in self.houses with swapped houses
                temp_houses = sorted(temp_houses, key=lambda house: house.id)
                temp_houses[random_house_in_battery.id] = random_house_in_battery
                temp_houses[random_house_in_battery2.id] = random_house_in_battery2

                # Save solution & append costs to self.results
                solution = Solution(temp_houses, temp_batteries)
                self.results.append([counter, solution.calculate_costs(counter)])
                self.results2.append(solution.calculate_costs(counter))

            # EINDE HILL CLIMBER
            eind_oplossing = Solution(temp_houses, temp_batteries)
            self.multi_results.append([count, eind_oplossing.calculate_costs(count)])
            Frequency_visualizer.write_csv(Frequency_visualizer, self.results2, "Simulated_annealing")
