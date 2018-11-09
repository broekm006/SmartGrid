import sys, os
sys.path.append('../classes')

from house import House
from battery import Battery

class Load():

    def __init__(self, huis, batterij):
        self.house = self.load_houses(f"../../data/Huizen&Batterijen/{huis}_huizen.csv")
        self.battery = self.load_batteries(f"../../data/Huizen&Batterijen/{batterij}_batterijen.txt")

    def load_houses(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            self.houses = []

            for i in content:
                i = i.strip()
                houses.append(i.split(","))

            # load houses into list (x, y, max_amp)
            for house in houses[1:]:
                house = House(int(house[0]), int(house[1]), float(house[2]))
                print(house)

            print()
            print()

    def load_batteries(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            self.batteries = []

            for i in content:

                i = i.replace("\t", " ")
                i = i.replace(",", "")
                i = i.replace("[", "")
                i = i.replace("]", "")

                i = i.strip('\n')
                batteries.append(i.split())

                for battery in batteries[1:]:
                    battery = Battery(int(battery[0]), int(battery[1]), float(battery[2]))
                    print(battery)

if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    # connect & keep track of current battery usage
    for battery in self.batteries:
        for house in self.houses:
            battery.current_usage += house.amp


    #test2