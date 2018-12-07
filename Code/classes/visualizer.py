import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('../classes')

from house import House
from battery import Battery


class Visualizer():

    def __init__(self, houses, batteries):
        self.write_csv(houses, batteries)
        create_visualisation("houses.csv", "batteries.csv")

    def cssv(self, name, results):
        with open("resultaten/" + name + ".csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["costs", "number"])

            for result in results:
                csv_writer.writerow(result)

    def write_csv(self, houses, batteries):

        with open("houses.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["type", "id", "x", "y", "connected_bat"])
            for house in houses:
                house_list = []
                house_list.append("house")
                house_list.append(house.id)
                house_list.append(house.x)
                house_list.append(house.y)
                if house.connected != False:
                    house_list.append(house.connected.id)
                else:
                    house_list.append("not connected")
                # for battery in batteries:
                #
                #     try:
                #         if house.connected.id == battery.id:
                #             house_list.append(battery.x)
                #             house_list.append(battery.y)
                #     except:
                #         house_list.append("not connected")
                #         house_list.append("not connected")

                csv_writer.writerow(house_list)

            for battery in batteries:
                battery_list = []
                battery_list.append("battery")
                battery_list.append(battery.id)
                battery_list.append(battery.x)
                battery_list.append(battery.y)
                battery_list.append(battery.id)

                csv_writer.writerow(battery_list)


        with open("batteries.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["battery_id", "battery_x", "battery_y"])
            for battery in batteries:
                battery_list = []
                battery_list.append(battery.id)
                battery_list.append(battery.x)
                battery_list.append(battery.y)

                csv_writer.writerow(battery_list)

    def csv_HillClimber(self, results, titel):
        with open("resultaten/" + titel + ".csv", mode = 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["costs"])

            for result in results:
                csv_writer.writerow(result)

    def make_my_day():
        readCsv = pd.read_csv("resultaten/Simulated_annealing.csv")
        sns.set_color_codes("dark")

        plot = sns.barplot(x="number", y="costs", data=readCsv, palette="RdBu")
        plot.set_title("Simulated_annealing barplot graph")
        plot.set(xlabel='X as', ylabel='Y as')
        #plot.set_xticks(np.arange(1,500, step=10))

        plt.show()

    def make_my_day2():
        readCsv = pd.read_csv("resultaten/cheat.csv")
        sns.set_color_codes("dark")

        plot = sns.barplot(x="algorithm", y="costs", data=readCsv, order=["Lowerbound", "Output", "Distance" ,"Priority", "Output+HC", "Distance+HC", "Priority+HC", "Output+SA", "Distance+SA", "Priority+SA", "Upperbound"], palette="GnBu_d")
        plot.set_title("Algorithm Analyse")
        plot.set(xlabel='Algoritmes', ylabel='Kosten')
        #plot.set_xticks(np.arange(1,500, step=10))

        plt.show()

def create_visualisation(houses_csv, batteries_csv):
    df = pd.read_csv(houses_csv)

    #sns.set()
    #sns.set_context("notebook", font_scale=0.6)
    sns.set_color_codes("dark")
    #sns.palplot(sns.color_palette())
    plot = sns.scatterplot(x="x", y="y", hue="connected_bat", data=df, ci=None, style="type", palette=["C0", "C1", "C2", "C3", "C4"])

    plot.set_title("Wijk 1: after K-Means")

    #plot.set_title("Wijk 1: after K-Means")
    plot.set_title("Wijk 1: houses connected to nearest battery without restrictions.")
    plot.legend_.remove()
    plot.set(xlabel='X coordinates', ylabel='Y coordinates')

    #plot.set_xticks(list(range(51)))
    #plot.set_yticks(list(range(51)))
    plt.show()
