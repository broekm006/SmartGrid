import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_frequency_visual(results_csv):
    df = pd.read_csv(results_csv)

    sns.set()

    sns.set(font_scale=0.5)
    plot = sns.distplot(df.costs, kde=False, bins=12)

    plot.set(xlabel='costs', ylabel='frequency')



    plot.set_xticks(list(range(58400, 62600, 200)))
    plot.set_title("Cost frequencies after 100x Greedy priority sort and HillClimber afterwards")
    plot.set_yticks(list(range(0, 20, 2)))
    plt.show()

if __name__ == "__main__":
    create_frequency_visual("data.csv")
