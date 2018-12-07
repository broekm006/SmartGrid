import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import sys
sys.path.append('Code/classes')

from house import House
from battery import Battery


class Visualizer():

    def __init__(self, houses, batteries):
        self.write_csv(houses, batteries)
        create_visualisation("houses.csv", "batteries.csv")

    def cssv(self, name, results):
        with open("resultaten/" + name + ".csv", "a") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["costs"])

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
