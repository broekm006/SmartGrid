import random
import sys
sys.path.append('Code/classes')

from house import House
from battery import Battery

class Load():

    def __init__(self, huis, batterij):
        self.house = self.load_houses(f"data/Huizen&Batterijen/{huis}_huizen.csv")
        self.battery = self.load_batteries(f"data/Huizen&Batterijen/{batterij}_batterijen.txt")


    def load_houses(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            innitial_houses = []
            self.houses = []

            for i in content:
                i = i.strip()
                innitial_houses.append(i.split(","))

            # load houses into list (id, x, y, max_amp)
            for i, house in enumerate(innitial_houses[1:]):
                self.houses.append(House(i, int(house[0]), int(house[1]), float(house[2])))


    def load_batteries(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            innitial_batteries = []
            self.batteries = []

            for i in content:

                i = i.replace("\t", " ")
                i = i.replace(",", "")
                i = i.replace("[", "")
                i = i.replace("]", "")

                i = i.strip('\n')
                innitial_batteries.append(i.split())

            for i, battery in enumerate(innitial_batteries[1:]):
                self.batteries.append(Battery(i, int(battery[0]), int(battery[1]), float(battery[2])))


    def distance(self, house, batteries):
        '''Calculate distance between given house and each battery'''

        for battery in batteries:
            battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)

        return batteries

    def connect_houses(self):

        # Sort houses by max output
        self.houses = sorted(self.houses, key=lambda house: house.amp, reverse=True)

        # sort batteries based on distance to house
        for house in self.houses:

            # Get distance from current house to each battery
            self.batteries = self.distance(house, self.batteries)

            # Sort batteries based on distance to current house
            self.batteries = sorted(self.batteries, key=lambda battery: battery.distance)

            # adds sorted list to house.distance (house.distance == self.batteries)
            house.nearest(self.batteries)

            ''''
            # TEST: volgorde batterijen per huis

            print("House ID: " str(house.id))
            for battery in house.distance:
                print(battery.id)
            '''

            # Connect house to nearest battery with enough available capacity
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    battery.connect(house.id)
                    house.connect(battery)

                    # Update battery usage & calculate cable costs
                    battery.add(house.amp)
                    house.cable_costs(battery.distance)



                    '''
                    TEST: cable_costs (battery_distance * 9)
                    print(house.connected)
                    print(battery.distance)
                    print(house.costs)
                    '''


                    '''
                    # TEST: afstand batterij - huis + gekozen batterij

                    print("HOUSE ID: " + str(house.id))
                    print("House coördinates: " + str(house.x) + "," + str(house.y))
                    print("Battery ID: " + str(battery.id))
                    print("Battery coördinates: " + str(battery.x) + "," + str(battery.y))
                    print("Distance house-battery: " + str(battery.distance))
                    print()
                    '''

                    break
        counter = 0
        for house in self.houses:
            while not house.isconnected:
                lowest, second = float('inf'), float('inf')

                self.batteries = sorted(self.batteries, key=lambda battery: battery.id, reverse=True)

                # get lowest & second lowest battery
                for battery in self.batteries:
                    if battery.current_usage <= lowest:
                        lowest, second = battery.current_usage, lowest
                        battery_id1 = battery.id
                        print("1", battery_id1, battery.current_usage)
                    elif battery.current_usage < second:
                        second = battery.current_usage
                        battery_id2 = battery.id
                        print("2", battery_id2, battery.current_usage)

                # choose random id from battery-house list
                random1 = random.choice(self.batteries[battery_id1].connected)
                random2 = random.choice(self.batteries[battery_id2].connected)

                # look for the amp of the randomly selected house
                for house in self.houses:
                    if house.id == random1:
                        random1_amp = house.amp
                        #print(house.amp)

                    if house.id == random2:
                        random2_amp = house.amp
                        #print(house.amp)

                #remove "lowest id + update current_usage"
                self.batteries[battery_id1].remove(random1)
                self.batteries[battery_id1].current_usage -= random1_amp

                self.batteries[battery_id2].remove(random2)
                self.batteries[battery_id2].current_usage -= random2_amp

                max = self.batteries[battery_id1].max_amp
                currents1 = self.batteries[battery_id1].current_usage
                currents2 = self.batteries[battery_id2].current_usage

                if  max - (currents1 + random2_amp) > 0 and max - (currents2 + random1_amp) > 0:
                    #add removed house to other battery_id
                    self.batteries[battery_id1].connect(random2)
                    #self.batteries[battery_id1].add(random2_amp)
                    self.batteries[battery_id1].current_usage += random2_amp


                    self.batteries[battery_id2].connect(random1)
                    #self.batteries[battery_id2].add(random1_amp)
                    self.batteries[battery_id2].current_usage += random1_amp

                else:
                    #undo remove because the switch does not work (battery overload)
                    self.batteries[battery_id1].connect(random1)
                    #self.batteries[battery_id1].add(random1_amp)
                    self.batteries[battery_id1].current_usage += random1_amp


                    self.batteries[battery_id2].connect(random2)
                    #self.batteries[battery_id2].add(random2_amp)
                    self.batteries[battery_id2].current_usage += random2_amp

                #calculate new amp
                low_max = self.batteries[battery_id1].current_usage
                high_max = self.batteries[battery_id2].current_usage

                # check if left_over house fits in lowest value battery
                if  low_max <= self.batteries[battery_id1].max_amp - house.amp:
                    self.batteries[battery_id1].connect(house.id)
                    self.batteries[battery_id1].add(house.amp)
                    #print("LOW", low_max - house.amp)
                    house.isconnected = True

                # check if left_over house fits in second lowest value battery
                elif high_max <= self.batteries[battery_id2].max_amp - house.amp:
                    self.batteries[battery_id2].connect(house.id)
                    self.batteries[battery_id2].add(house.amp)
                    #print("high", high_max - house.amp)
                    house.isconnected = True

                counter += 1
                '''
                #print statements to test
                print("house1 amp:", random1_amp)
                print("house2 amp:", random2_amp)
                print(house.amp)
                print("battery1 cap:", random2_amp + lowest - random1_amp)
                print("battery2 cap:", random1_amp + second - random2_amp)
                print("room left battery1:", low_max, ">id<", battery_id1)
                print("room left battery2:", self.batteries[battery_id2].max_amp - (random1_amp + second - random2_amp), ">id<", battery_id2)
                '''
                #!# voeg check house . costs error > zou goed moeten zijn nadat functie is gerunt
                #!# voeg check to op basis van max_amp per battery zodat deze niet kan worden overschreven.


        # TEST: alle batterijen aangesloten?
        # Batterijen totaal = 7 535
        # Huizen totaal = 7 500

                print()
                print(counter)
                current_usage = 0
                for battery in self.batteries:
                    print()
                    print("ID:" + str(battery.id))
                    print("Current usage: " + str(battery.current_usage))
                    print("Available: " + str(battery.check_amp()))
                    print("Connected ID's" + str(battery.connected))
                    current_usage += battery.current_usage
                    print()

                print("Total battery usage: " + str(current_usage))


        '''
        # TEST: overzicht huizen gesorteert op basis van kosten

        # Sort houses by costs
        self.houses = sorted(self.houses, key=lambda house: house.costs, reverse=True)

        for house in self.houses:
            print("ID: " + str(house.id))
            print("House output: " + str(house.amp))
            print("Costs: " + str(house.costs))
            print()
        '''


    def costs(self):
        # Battery battery battery costs
        battery_costs = 0
        for battery in self.batteries:
            battery_costs += battery.cost

        # Cable cable costs
        cable_costs = 0
        for house in self.houses:
            cable_costs += house.costs
            # print(cable_costs)

        # Total costs
        total_costs = battery_costs + cable_costs

        '''
        # TEST: costs

        print("Battery costs: " + str(battery_costs))
        print("Cable costs: " + str(cable_costs))
        print("Total costs: " + str(total_costs))
        '''

if __name__ == "__main__":
    load = Load("wijk2", "wijk2")
    load.connect_houses()
    load.costs()
