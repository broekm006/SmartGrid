import random, csv, copy
from solution import Solution

class Hill_climber(object):

    def __init__(self, houses, batteries, number_of_times, number_of_runs):
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)
        self.number_of_times = number_of_times
        self.n = number_of_runs
        self.results = []
        self.multi_results = []
        self.hill_climbers()

    def hill_climbers(self):

        for count in range(self.n):
            temp_batteries = copy.deepcopy(self.batteries)
            temp_houses = copy.deepcopy(self.houses)

            counter = 0
            temp_batteries = sorted(temp_batteries, key=lambda battery: battery.id)
            # loop throug algorithm for number_of_times
            for i in range(self.number_of_times):
                random_battery = random.choice(temp_batteries)
                random_battery2 = random.choice(temp_batteries)

                # make sure 2 different batteries are chosen
                while random_battery == random_battery2:
                    random_battery2 = random.choice(temp_batteries)

                # choose 2 random houses from the batteries
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

<<<<<<< HEAD
=======
                # calc old distance
>>>>>>> 93b363af56e4b91f77635d7c8947de2681429cd3
                old_distance = solution.distance_calc(random_house_in_battery, random_battery)
                old_distance2 = solution.distance_calc(random_house_in_battery2, random_battery2)

                # calc new distance
                new_distance = solution.distance_calc(random_house_in_battery, random_battery2)
                new_distance2 = solution.distance_calc(random_house_in_battery2, random_battery)

                # check if swap is possible
                if  max - (currents1 + random_house_in_battery2.amp) > 0 and max - (currents2 + random_house_in_battery.amp) > 0:
                    #add removed house to other battery_id
                    if old_distance + old_distance2 > new_distance + new_distance2:
                        temp_batteries[random_battery.id].add(random_house_in_battery2)
                        temp_batteries[random_battery2.id].add(random_house_in_battery)
                        random_house_in_battery.connect(temp_batteries[random_battery2.id])
                        random_house_in_battery2.connect(temp_batteries[random_battery.id])

                        temp_houses[random_house_in_battery.id] = random_house_in_battery
                        temp_houses[random_house_in_battery2.id] = random_house_in_battery2

                    else:
                        #undo remove because the switch does not work (battery overload)
                        temp_batteries[random_battery.id].add(random_house_in_battery)
                        temp_batteries[random_battery2.id].add(random_house_in_battery2)

                else:
                    #undo remove because the switch does not work (battery overload)
                    temp_batteries[random_battery.id].add(random_house_in_battery)
                    temp_batteries[random_battery2.id].add(random_house_in_battery2)

                # Save solution & append costs to self.results
                solution = Solution(temp_houses, temp_batteries)
                self.results.append([solution.calculate_costs(i)])

                counter += 1

            # End HILL CLIMBER
            eind_oplossing = Solution(temp_houses, temp_batteries)
            self.multi_results.append(eind_oplossing.calculate_costs(count))
