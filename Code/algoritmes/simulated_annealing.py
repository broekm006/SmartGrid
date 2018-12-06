# voeg loop toe op basis temperatuur
# hoge temp == mag over max_amp heen
# lage temp == zorg dat het weer past
# vind argument voor ^
# http://katrinaeg.com/simulated-annealing.html

import random
from solution import Solution

class Simulated_annealing(object):

    def __init__(self, houses, batteries, number_of_times):
        self.houses = houses
        self.batteries = batteries
        self.number_of_times = number_of_times

    # def simulatie(self):
    #     counter = 0
    #     self.batteries = sorted(self.batteries, key=lambda battery: battery.id)
    #
    #     T = 1.0
    #     T_min = 0.00001
    #     alpha = 0.9
    #
    #     while T > T_min:
    #         i = 1
    #         # loop throug algorithm for number_of_times
    #         #for i in range(self.number_of_times):
    #         while i <= 10:
    #             if T > 0.01:
    #
    #                 random_battery = random.choice(self.batteries)
    #                 random_battery2 = random.choice(self.batteries)
    #
    #                 # make sure 2 different batteries are chosen
    #                 while random_battery == random_battery2:
    #                     random_battery2 = random.choice(self.batteries)
    #
    #                 #choose 2 random houses from the batteries
    #                 random_house_in_battery = random.choice(random_battery.connected)
    #                 random_house_in_battery2 = random.choice(random_battery2.connected)
    #
    #                 #remove "lowest id + update current_usage"
    #                 self.batteries[random_battery.id].remove(random_house_in_battery)
    #                 self.batteries[random_battery2.id].remove(random_house_in_battery2)
    #
    #                 max = self.batteries[random_battery.id].max_amp
    #                 currents1 = self.batteries[random_battery.id].current_usage
    #                 currents2 = self.batteries[random_battery2.id].current_usage
    #
    #                 # calculate distance
    #                 solution = Solution(self.houses, self.batteries)
    #                 solution.distance_calc(random_house_in_battery, random_battery)
    #
    #                 old_distance = solution.distance_calc(random_house_in_battery, random_battery)
    #                 old_distance2 = solution.distance_calc(random_house_in_battery2, random_battery2)
    #
    #                 new_distance = solution.distance_calc(random_house_in_battery, random_battery2)
    #                 new_distance2 = solution.distance_calc(random_house_in_battery2, random_battery)
    #
    #                 #print("total:  ", old_distance + old_distance2)
    #                 #print("total2: ", new_distance + new_distance2)
    #                 # check if swap is possible
    #
    #                 #print (old_distance, old_distance2)
    #                 #print (new_distance, new_distance2)
    #                 max += 100
    #
    #                 if  max - (currents1 + random_house_in_battery2.amp) > 0 and max - (currents2 + random_house_in_battery.amp) > 0:
    #                     #add removed house to other battery_id
    #                     if old_distance + old_distance2 < new_distance + new_distance2:
    #                         self.batteries[random_battery.id].add(random_house_in_battery2)
    #                         self.batteries[random_battery2.id].add(random_house_in_battery)
    #
    #                     else:
    #                         #undo remove because the switch does not work (battery overload)
    #                         self.batteries[random_battery.id].add(random_house_in_battery)
    #                         self.batteries[random_battery2.id].add(random_house_in_battery2)
    #
    #                 else:
    #                     #undo remove because the switch does not work (battery overload)
    #                     self.batteries[random_battery.id].add(random_house_in_battery)
    #                     self.batteries[random_battery2.id].add(random_house_in_battery2)
    #
    #
    #             elif T < 0.01:
    #                 lowest, second = float('inf'), float('inf')
    #
    #                 # get lowest & second lowest battery
    #                 for battery in self.batteries:
    #                     if battery.current_usage <= lowest:
    #                         lowest, second = battery.current_usage, lowest
    #                         battery_id1 = battery
    #                     elif battery.current_usage < second:
    #                         second = battery.current_usage
    #                         battery_id2 = battery
    #
    #                 # make sure 2 different batteries are chosen
    #                 while battery_id1 == battery_id2:
    #                     battery_id2 = random.choice(self.batteries)
    #
    #                 max = self.batteries[battery_id1.id].max_amp
    #                 currents1 = self.batteries[battery_id1.id].current_usage
    #                 currents2 = self.batteries[battery_id2.id].current_usage
    #
    #                 random_house_in_battery2 = random.choice(battery_id2.connected)
    #
    #                 #remove "lowest id + update current_usage"
    #                 self.batteries[battery_id2.id].remove(random_house_in_battery2)
    #
    #                 old_distance2 = solution.distance_calc(random_house_in_battery2, random_battery2)
    #
    #                 new_distance2 = solution.distance_calc(random_house_in_battery2, random_battery)
    #
    #                 #add removed house to other battery_id
    #                 if True:
    #                         self.batteries[battery_id1.id].add(random_house_in_battery2)
    #                 else:
    #                     #undo remove because the switch does not work (battery overload)
    #                     self.batteries[battery_id2.id].add(random_house_in_battery2)
    #
    #             counter += 1
    #             i += 1
    #         T = T*alpha
    #
    #     # check connected id vs amp available > to fix
    #     current_usage = 0
    #     print(counter)
    #     for battery in self.batteries:
    #         print()
    #         print("ID:" + str(battery.id))
    #         print("Current usage: " + str(battery.current_usage))
    #         print("Available: " + str(battery.check_amp()))
    #
    #         # listy is only here to get a visual representation of the connected house ID's
    #         # before it was: print("Connected ID's" + str(battery.connected))
    #
    #         listy = []
    #         for item in battery.connected:
    #             listy.append(item.id)
    #         print("Connected ID's" + str(listy))
    #
    #         current_usage += battery.current_usage
    #         print()
    #     print("Total battery usage: " + str(current_usage))
    #
    #     #print("total distance1: ", solution.total_distance())
    #     #print(counter)
    #
    # # switch alleen wanneer ruimte is + afstand acceptabel is in temperatuur
    # def anneal(self, houses, batteries, sol):
    #     old_cost = cost(random.choice(battery_id2.connected), random.choice(self.batteries))
    #     T = 1.0
    #     T_min = 0.00001
    #     alpha = 0.9
    #     while T > T_min:
    #         i = 1
    #         while i <= 100:
    #             new_sol = neighbor(sol)
    #             new_cost = cost(new_sol)
    #             ap = acceptance_probability(old_cost, new_cost, T)
    #             if ap > random():
    #                 sol = new_sol
    #                 old_cost = new_cost
    #             i += 1
    #         T = T*alpha

    def simulatie_V2(self):
        counter = 0
        self.batteries = sorted(self.batteries, key=lambda battery: battery.id)

        T = 1.0
        T_min = 0.00001
        alpha = 0.9

        while T > T_min:
            i = 1
            # loop throug algorithm for number_of_times
            #for i in range(self.number_of_times):
            while i <= 10:
                random_battery = random.choice(self.batteries)
                random_battery2 = random.choice(self.batteries)

                # make sure 2 different batteries are chosen
                while random_battery == random_battery2:
                    random_battery2 = random.choice(self.batteries)

                #choose 2 random houses from the batteries
                random_house_in_battery = random.choice(random_battery.connected)
                random_house_in_battery2 = random.choice(random_battery2.connected)

                #remove "lowest id + update current_usage"
                self.batteries[random_battery.id].remove(random_house_in_battery)
                self.batteries[random_battery2.id].remove(random_house_in_battery2)

                max = self.batteries[random_battery.id].max_amp
                currents1 = self.batteries[random_battery.id].current_usage
                currents2 = self.batteries[random_battery2.id].current_usage

                # calculate distance
                solution = Solution(self.houses, self.batteries)
                solution.distance_calc(random_house_in_battery, random_battery)

                old_distance = solution.distance_calc(random_house_in_battery, random_battery)
                old_distance2 = solution.distance_calc(random_house_in_battery2, random_battery2)

                new_distance = solution.distance_calc(random_house_in_battery, random_battery2)
                new_distance2 = solution.distance_calc(random_house_in_battery2, random_battery)

                #print("total:  ", old_distance + old_distance2)
                #print("total2: ", new_distance + new_distance2)
                # check if swap is possible

                #print (old_distance, old_distance2)
                #print (new_distance, new_distance2)
                #max += 100



                if  max - (currents1 + random_house_in_battery2.amp) > 0 and max - (currents2 + random_house_in_battery.amp) > 0:
                    #add removed house to other battery_id
                    if old_distance + old_distance2 < new_distance + new_distance2:
                        self.batteries[random_battery.id].add(random_house_in_battery2)
                        self.batteries[random_battery2.id].add(random_house_in_battery)
                        random_house_in_battery.connect(self.batteries[random_battery2.id])
                        random_house_in_battery2.connect(self.batteries[random_battery.id])

                    else:
                        #undo remove because the switch does not work (battery overload)
                        self.batteries[random_battery.id].add(random_house_in_battery)
                        self.batteries[random_battery2.id].add(random_house_in_battery2)

                else:
                    #undo remove because the switch does not work (battery overload)
                    self.batteries[random_battery.id].add(random_house_in_battery)
                    self.batteries[random_battery2.id].add(random_house_in_battery2)


                if T > 0.1:
                    new_distance - 15
                    new_distance2 - 15
                elif T < 0.1:
                    new_distance - 10
                    new_distance2 - 10
                elif T < 0.01:
                    new_distance - 5
                    new_distance2 - 5
                elif T < 0.001:
                    new_distance - 2
                    new_distance2 - 2
                counter += 1
                i += 1
            T = T*alpha

        # check connected id vs amp available > to fix
        current_usage = 0
        print(counter)
        for battery in self.batteries:
            print()
            print("ID:" + str(battery.id))
            print("Current usage: " + str(battery.current_usage))
            print("Available: " + str(battery.check_amp()))

            # listy is only here to get a visual representation of the connected house ID's
            # before it was: print("Connected ID's" + str(battery.connected))

            listy = []
            for item in battery.connected:
                listy.append(item.id)
            print("Connected ID's" + str(listy))

            current_usage += battery.current_usage
            print()
        print("Total battery usage: " + str(current_usage))

        #print("total distance1: ", solution.total_distance())
        #print(counter)
