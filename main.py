import sys

sys.path.append('Code')
from load import Load
from visualizer import Visualizer


sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber
from hill_climber_test import Hill_climber_test
from k_means import K_means

sys.path.append('Code/classes')
from helper import Helper


if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    Helper.bounds(Helper, load.batteries, load.houses)
    # greedy = Greedy(load.houses, load.batteries, "priority") # "output", "distance", "priority"

    k_means = K_means(load.houses, load.batteries)
    # hill_climber = Hill_climber_test(load.houses, load.batteries, 500)
    # hill_climber.best_choice()
    # hill_climber.ice_climbers()
    # #
    # # Helper.costs(Helper, hill_climber.batteries, hill_climber.houses)
    # # Helper.sort_houses(Helper, greedy.houses)
    # #
    # Visualizer(hill_climber.houses, hill_climber.batteries)
    Visualizer(k_means.houses, k_means.batteries)
