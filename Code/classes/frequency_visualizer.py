import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('../classes')

from house import House
from battery import Battery


class Frequency_visualizer():

    def __init__(self, results, visualtype, title):
        self.results_csv = self.write_csv(results, title)
        self.check_visual_type(visualtype)


    def write_csv(self, results, titel):
        '''Create a new .CSV file based on the results + name of the algorithm'''

        with open("resultaten/" + titel + ".csv", mode = 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["iteration", "costs"])

            for index, result in enumerate(results):
                csv_writer.writerow([index, result])

        return ("resultaten/" + titel + ".csv")


    def check_visual_type(self, visualtype):
        '''Check for visual type and call right method'''
        if visualtype == "result_frequency_table":
            self.create_frequency_visual()
        else:
            pass


    def create_frequency_visual(self):
        ''' Create frequency visualization based on the algorithm'''
        df = pd.read_csv(self.results_csv)

        sns.set(font_scale=0.5)

        plot = sns.distplot(df.costs, kde=False, bins=14)
        plot.set_title("Cost frequencies after Greedy priority sort and 1000 runs of HillClimber afterwards")
        plot.autoscale(enable=True, axis='both', tight=False)
        plot.set(xlabel='costs', ylabel='frequency')
        plot.grid(False)

        plt.show()


    def make_my_day():
        ''' Create a Bar graph for Simulated annealing'''
        readCsv = pd.read_csv("resultaten/Simulated_annealing.csv")

        sns.set_color_codes("dark")

        plot = sns.barplot(x="iteration", y="costs", data=readCsv, palette="RdBu")
        plot.set_title("Simulated_annealing barplot graph")
        plot.set(xlabel='Frequency * 1000', ylabel='Costs')
        plot.set_xticks(list(range(0,1001,100)))

        plt.show()


    def make_my_day2():
        '''Create a bar graph for the combined results  '''
        readCsv = pd.read_csv("resultaten/cheat.csv")

        sns.set_color_codes("dark")

        plot = sns.barplot(x="algorithm", y="costs", data=readCsv, order=["Lowerbound", "Output", "Distance" ,"Priority", "Output+HC", "Distance+HC", "Priority+HC", "Output+SA", "Distance+SA", "Priority+SA", "Upperbound"], palette="GnBu_d")
        plot.set_title("Algorithm Analyse")
        plot.set(xlabel='Algoritmes', ylabel='Kosten')

        plt.show()
