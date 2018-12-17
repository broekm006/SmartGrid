import sys
import argparse

sys.path.append('Code')
from load import Load
from frequency_visualizer import Frequency_visualizer
from grid_visualizer import Grid_visualizer

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber
from hill_climber_BC import Hill_climber_BC
from k_means2 import K_means2
from random_connect import Random_connect
from test_merge import Cluster_merge
from simulated_annealing import Simulated_annealing

sys.path.append('Code/classes')
from helper import Helper

def what_to_run(self, wijk, algo, sec_algo, NoT, vis):
    ''' Kijkt welke variant van greedy'''
    wijk = "wijk" + wijk
    load = Load(wijk, wijk)

    if algo == "random":
        random = Random_connect(load.houses, load.batteries)
    elif algo == "greedy_output":
        greedy = Greedy(load.houses, load.batteries, "output")
    elif algo == "greedy_distance":
        greedy = Greedy(load.houses, load.batteries, "distance")
    elif algo == "greedy_priority":
        greedy = Greedy(load.houses, load.batteries, "priority")
    elif algo == "k_means_output":
        k_means = K_means2(load.houses, load.batteries, "output", "", NoT)
    elif algo == "k_means_distance":
        k_means = K_means2(load.houses, load.batteries, "distance", "", NoT)
    elif algo == "k_means_priority":
        k_means = K_means2(load.houses, load.batteries, "priority", "", NoT)

    else:
        print("Error running algorithm")

    if sec_algo == "hill_climber" and algo == "greedy_output" or sec_algo == "hill_climber" and algo == "greedy_distance" or sec_algo == "hill_climber"  and algo == "greedy_priority":
        hill_climber = Hill_climber(greedy.houses, greedy.batteries, 1000, NoT)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(hill_climber.houses, hill_climber.batteries, "gridview")
    elif sec_algo == "hill_climber" and algo == "k_means_output" or sec_algo == "hill_climber" and algo == "k_means_distance" or sec_algo == "hill_climber" and algo == "k_means_priority":
        hill_climber = Hill_climber(k_means.houses, k_means.batteries, 1000, NoT)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(hill_climber.houses, hill_climber.batteries, "gridview")
    elif sec_algo == "hill_climber_BC" and algo == "greedy_output" or sec_algo == "hill_climber_BC" and algo == "greedy_distance" or sec_algo == "hill_climber_BC" and algo == "greedy_priority":
        hill_climber_BC = Hill_climber_BC(greedy.houses, greedy.batteries, NoT)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(hill_climber_BC.houses, hill_climber_BC.batteries, "gridview")
    elif sec_algo == "hill_climber_BC" and algo == "k_means_output" or sec_algo == "hill_climber_BC" and algo == "k_means_distance" or sec_algo == "hill_climber_BC" and algo == "k_means_priority":
        hill_climber_BC = Hill_climber_BC(k_means.houses, k_means.batteries, NoT)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(hill_climber_BC.houses, hill_climber_BC.batteries, "gridview")
    elif sec_algo == "simulated_annealing" and algo == "greedy_output" or sec_algo == "simulated_annealing" and algo == "greedy_distance" or sec_algo == "simulated_annealing" and algo == "greedy_priority":
        sim = Simulated_annealing(greedy.houses, greedy.batteries, NoT)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(sim.houses, sim.batteries, "gridview")
    elif sec_algo == "simulated_annealing" and algo == "k_means_output" or sec_algo == "simulated_annealing" and algo == "k_means_distance" or sec_algo == "simulated_annealing" and algo == "k_means_priority":
        sim = Simulated_annealing(k_means.houses, k_means.batteries, NoT)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(sim.houses, sim.batteries, "gridview")



    else:
        print("Error running secondary algorithm")

    #Frequency_visualizer.bar_sim()

# moet algoritme elke keer opnieuw runnen voor main of 1 maal runnen *n > anders worden algo keer op keer opnieuw geloopt

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(prog='main.py', usage='%(prog)s [-h] [-a [greedy_output, greedy_distance, greedy_priority, k_means_output, k_means_distance, k_means_priority]] [-b [hill_climber, simulated_annealing, brute_force]] [-i [iterations]] [-v [Y]]')
    # parser.add_argument('-w', '--wijk', type=str, choices=['1', '2', '3'], required=True)
    # parser.add_argument('-a', '--algorithm', type=str, choices=['greedy_output', 'greedy_distance', 'greedy_priority','k_means_output', 'k_means_distance', 'k_means_priority'], required=True)
    # parser.add_argument('-b', '--secondary_algorithm', choices=['hill_climber','hill_climber_BC','simulated_annealing'], type=str, required=False, default="simulated_annealing")
    # parser.add_argument('-i','--iterations', type=int, help='Enter the number of times you wish to run the selected algorithm', required=False, default=1)
    # parser.add_argument('-v','--visualizer', choices=['True','False'], type=str, help='Enter True if you want to see a visual representation of the algorithm', required=False, default='False')
    #
    # #parser.print_help()
    # args = parser.parse_args()
    #
    # print(args.wijk)
    # print(args.algorithm)
    # print(args.secondary_algorithm)
    # print(args.iterations)
    # print(args.visualizer)
    # what_to_run(what_to_run, args.wijk, args.algorithm, args.secondary_algorithm, args.iterations, args.visualizer)

# algo == type of algorithm
# sec_algo == type of iterative algorithm to combine with initial algorithm
# NoT == Number of Times to run the algorithm(s)
# vis == Whether we run a visual or not

# add default values for ^ to make it work

    load = Load("wijk1", "wijk1")

    # Default Bounds
    # Helper.bounds(Helper, load.batteries, load.houses)

    # Greedy
    # greedy = Greedy(load.houses, load.batteries, "priority") # "output", "distance", "priority"

    # random
    # random = Random_connect(load.houses, load.batteries)

    # Hill CLimber
    # hill_climber = Hill_climber(greedy.houses, greedy.batteries, 1, 10)


    # Hill Climber Best Choice
    # hill_climber_BC = Hill_climber_BC(greedy.houses, greedy.batteries, 10)

    # Simulated Annealing
    # sim = Simulated_annealing(greedy.houses, greedy.batteries, 1)

    # K Means
    # k_means = K_means2(load.houses, load.batteries, "priority", "") # "random" or "" for innitial battery location

    #
    splitter = Cluster_merge(load.houses)
    sim = Simulated_annealing(splitter.houses, splitter.batteries, 1)

    # Bounds + Costs
    # Helper.bounds(Helper, k_means.batteries, k_means.houses)
    # Helper.costs(Helper, greedy.batteries, greedy.houses)
    # Helper.battery_info(Helper, k_means.batteries)
    # Helper.sort_houses(Helper, greedy.houses)

    # Grid visualisatie, specify houses, batteries and visual type
    # grid_visualisatie = Grid_visualizer(k_means.houses, k_means.batteries, "gridview")

    # visualizer.csv_HillClimber(sim.multi_results, "MultiSA_PRIORITY_WIJK1") # HillClimber_BC1 / HillClimber_random1

    # frequency visualisatie, meegeven resultaten, type visualisatie en titel
    #frequency_table = Frequency_visualizer(hill_climber.multi_results, "result_frequency_table", "100 iterations HC") # HillClimber_BC1 / HillClimber_random1
