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

    def write_csv(self, houses, batteries):

        with open("houses.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["house_id", "house_x", "house_y", "connected_bat", "bat_x", "bat_y"])
            for house in houses:
                house_list = []
                house_list.append(house.id)
                house_list.append(house.x)
                house_list.append(house.y)
                house_list.append(house.connected.id)
                for battery in batteries:
                    if house.connected.id == battery.id:
                        house_list.append(battery.x)
                        house_list.append(battery.y)
                csv_writer.writerow(house_list)

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
    sns.set()
    sns.set_context("paper", font_scale=0.6)
    sns.set_color_codes("dark")
    plot = sns.scatterplot(x="house_x", y="house_y", hue="connected_bat", data=df)
    #plot.legend_.remove()
    plot.set(xlabel='', ylabel='')
    plot.set_xticks(list(range(51)))
    plot.set_yticks(list(range(51)))
    plt.show()
    # g = (g.map(plt.scatter, "total_bill", "tip", **kws).add_legend())
