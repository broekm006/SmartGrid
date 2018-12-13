import sys
import argparse

sys.path.append('Code')
from load import Load
from frequency_visualizer import Frequency_visualizer
from grid_visualizer import Grid_visualizer

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber_update import Hill_climber
from hill_climber_BC import Hill_climber_BC
from k_means2 import K_means2
from random_connect import Random_connect
#from simulated_annealing import Simulated_annealing

sys.path.append('Code/classes')
from helper import Helper


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='main.py', usage='%(prog)s [-h] [-a [greedy, k_means]] [-b [hill_climber, simulated_annealing, brute_force]] [-i [iterations]] [-v [Y]]')
    parser.add_argument('-a', '--algorithm', type=str, choices=['greedy','k_means'], required=True)
    parser.add_argument('-b', '--secondary_algorithm', choices=['hill_climber','simulated_annealing', 'brute_force'], type=str, required=True)
    parser.add_argument('-i','--iterations', type=int, help='Enter the number of times you wish to run the selected algorithm', required=False)
    parser.add_argument('-v','--visualizer', choices=['True','False'], type=str, help='Enter True if you want to see a visual representation of the algorithm', required=False)

    #parser.print_help()


    args = parser.parse_args()

    print(args.algorithm)
    print(args.secondary_algorithm)
    print(args.iterations)
    print(args.visualizer)

def what_to_run(self, type):
    ''' Kijkt welke variant van greedy'''

    if algo == "greedy":
        self.output()
    elif algo == "k_means":
        self.distance()
    else:
        print("Error running algorithm")


    #load = Load("wijk1", "wijk1")

    # Default Bounds
    # Helper.bounds(Helper, load.batteries, load.houses)

    # Greedy
    #greedy = Greedy(load.houses, load.batteries, "priority") # "output", "distance", "priority"

    # random
    # random = Random_connect(load.houses, load.batteries)

    # Hill CLimber
    #hill_climber = Hill_climber(greedy.houses, greedy.batteries, 10, 10)

    # Hill Climber Best Choice
    # hill_climber_BC = Hill_climber_BC(greedy.houses, greedy.batteries, 100)

    # Simulated Annealing
    #sim = Simulated_annealing(greedy.houses, greedy.batteries, 100)

    # K Means
    # k_means = K_means2(hill_climber_BC.houses, hill_climber_BC.batteries, "distance", "") # "random" or "" for innitial battery location


    # Bounds + Costs
    # Helper.bounds(Helper, greedy.batteries, greedy.houses)
    # Helper.costs(Helper, greedy.batteries, greedy.houses)
    # Helper.battery_info(Helper, k_means.batteries)
    # Helper.sort_houses(Helper, greedy.houses)

    # Grid visualisatie, specify houses, batteries and visual type
    #grid_visualisatie = Grid_visualizer(greedy.houses, greedy.batteries, "gridview")

    # visualizer.csv_HillClimber(sim.multi_results, "MultiSA_PRIORITY_WIJK1") # HillClimber_BC1 / HillClimber_random1
=======
    # frequency visualisatie, meegeven resultaten, type visualisatie en titel
    frequency_table = Frequency_visualizer(hill_climber.multi_results, "result_frequency_table", "100 iterations HC") # HillClimber_BC1 / HillClimber_random1
