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

            print(houses)
            print()
            print()
    def load_batteries(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            batterys = []

            for i in content:
                i = i.strip('\n\t')
                batterys.append(i.split("   "))

            print(batterys)

if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    #test
