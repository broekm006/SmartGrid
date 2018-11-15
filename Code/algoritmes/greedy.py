import sys
sys.path.append('Code/algoritmes')
from sort import Sort

class Greedy(object):

    def __init__(self, houses, batteries, type):
        self.houses = houses
        self.batteries = batteries
        self.type = self.type(type)

    # welke variant van greedy?
    def type(self, type):

        if type == "output":
            self.output()
        elif type == "distance":
            self.distance()
        elif type == "priority":
            self.pv()
        else:
            print("Greedy type error")

    # MAX_OUTPUT
    def output(self):
        ''' Connect house to nearest battery with available capacity'''

        self.houses = Sort.max_output(Sort, self.houses)

        for house in self.houses:
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    battery.connect(house.id)
                    house.connect(battery)
                    house.connected = True

                    # update battery usage
                    battery.add(house.amp)

                    # cable costs
                    battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)
                    house.cable_costs(battery.distance)

                    break;


    # DISTANCE
    def distance(self):
        ''' Connect house to nearest battery with available capacity'''

        for battery in self.batteries:
            # sorts houses based on distance to current battery
            self.houses = Sort.distance(Sort, self.houses, battery)

            # connect battery to nearest house that isn't connected
            for house in self.houses:
                if battery.check_amp() > house.amp and not house.connected:
                    battery.connect(house.id)
                    house.connect(battery)
                    house.connected = True

                    # distance
                    distance = abs(battery.y - house.y) + abs(battery.x - house.x)

                    # Update battery usage & calculate cable costs
                    battery.add(house.amp)
                    house.cable_costs(distance)


    # PRIORITY VALUE
    def pv(self):

        # sorts houses based on priority value
        self.houses = Sort.priority_value(Sort, self.houses, self.batteries)

        for house in self.houses:

            # sorts batteries based on distance from current house --> kan nog apart
            for battery in self.batteries:
                battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)
            self.batteries = sorted(self.batteries, key=lambda battery: battery.distance)

            # connect house to nearest available battery
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    battery.connect(house.id)
                    house.connect(battery)
                    house.connected = True

                    # Update battery usage & calculate cable costs
                    battery.add(house.amp)
                    house.cable_costs(battery.distance)
                    break;
