import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("hillclimber_1000.csv")

# sns.set(font_scale=0.5)

plot = sns.distplot(df["costs"], kde=False, bins=10)
# plot.autoscale(enable=True, axis='both', tight=False)

# plot = sns.distplot(df["distance"], kde=False, bins=10, label="Greedy Distance")
# # plot.autoscale(enable=True, axis='both', tight=False)
#
# plot = sns.distplot(df["priority"], kde=False, bins=10, label="Greedy Priority")
# # plot.autoscale(enable=True, axis='both', tight=False)
#
# plt.plot([63151, 63151], [0, 400], label="Greedy Output")

plt.ylim(0, 300)
plt.xlim(57500, 61000)


plot.set_title("Cost frequencies HillClimber after Priority sort (1000 runs)", fontsize=10)
# plot.autoscale(enable=True, axis='both', tight=False)
plot.set_xlabel('costs', fontsize=10)
plot.set_ylabel('frequency', fontsize=10)
plot.tick_params(labelsize=10)
# plot.grid(False)

plt.legend()
plt.show()
