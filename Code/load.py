from house import House
from battery import Battery

class Load():

    def __init__(self, huis, batterij):
        self.huis = self.load_houses(f"Huizen&Batterijen/{huis}_huizen.csv")
        self.huis = self.load_batteries(f"Huizen&Batterijen/{batterij}_batterijen.txt")

    def load_houses(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            houses = []

            for i in content:
                i = i.strip()
                houses.append(i.split(","))

            # load houses into list (x, y, max_volt)
            for house in houses:
                house = House(house[0], house[1], house[2])

            print(houses)
            print()
            print()

    def load_batteries(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            batterys = []

            for i in content:
                i = i.strip('\n')
                i = i.split("\t")
                batterys.append(i.strip())

            print(batterys)

if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    #test2
