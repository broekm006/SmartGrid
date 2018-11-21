import sys

sys.path.append('Code')
from load import Load

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber

sys.path.append('Code/classes')
from helper import Helper

if __name__ == "__main__":
    load = Load("wijk3", "wijk3")
    greedy = Greedy(load.houses, load.batteries, "output") # "output","distance", "priority"
    #Helper.costs(Helper, greedy.batteries, greedy.houses)

    hill_climber = Hill_climber(load.houses, load.batteries, 3)
    hill_climber.ice_climbers()
