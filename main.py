import sys

sys.path.append('Code')
from load import Load
from visualizer import Visualizer

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber
from hill_climber_BC import Hill_climber_BC
from k_means2 import K_means2
from random_connect import Random_connect

sys.path.append('Code/classes')
from helper import Helper


if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    # Helper.bounds(Helper, load.batteries, load.houses)
    greedy = Greedy(load.houses, load.batteries, "distance") # "output", "distance", "priority"
    hill_climber = Hill_climber(greedy.houses, greedy.batteries, 1000)
    # random = Random_connect(load.houses, load.batteries)

    # hill_climber_BC = Hill_climber_BC(greedy.houses, greedy.batteries)
    # k_means = K_means2(hill_climber_BC.houses, hill_climber_BC.batteries, "distance", "") # "random" or "" for innitial battery location
    # hill_climber_BC = Hill_climber_BC(k_means.houses, k_means.batteries)
    # hill_climber = Hill_climber_BC(random.houses, random.batteries)


    # Helper.bounds(Helper, greedy.batteries, greedy.houses)
    # Helper.costs(Helper, greedy.batteries, greedy.houses)
    # Helper.battery_info(Helper, k_means.batteries)
    # Helper.bounds(Helper, hill_climber_BC.batteries, hill_climber_BC.houses)
    # Helper.costs(Helper, hill_climber_BC.batteries, hill_climber_BC.houses)
    # Helper.sort_houses(Helper, greedy.houses)

    visualizer = Visualizer(hill_climber.houses, hill_climber.batteries)

    # HillClimber visualisatie
    visualizer.csv_HillClimber(hill_climber.results, "HillClimber_random1") # HillClimber_BC1 / HillClimber_random1
