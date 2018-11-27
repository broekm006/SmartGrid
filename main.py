import sys

sys.path.append('Code')
from load import Load
from visualizer import Visualizer


sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber

sys.path.append('Code/classes')
from helper import Helper


if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    Helper.bounds(Helper, load.batteries, load.houses)
    greedy = Greedy(load.houses, load.batteries, "output") # "output","distance", "priority"


    hill_climber = Hill_climber(load.houses, load.batteries, 500)
    hill_climber.ice_climbers()

    Helper.costs(Helper, hill_climber.batteries, hill_climber.houses)
    Helper.sort_houses(Helper, greedy.houses)

    Visualizer(hill_climber.houses, hill_climber.batteries)
