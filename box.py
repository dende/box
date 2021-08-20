import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

figsize = (6.4, 4.8)
markersize = 2
dpi = 200

config = {
    'secr. roGFP2-Orp1': ['WT', '#19', '#131', '#69'],
    'secr. Grx1-roGFP2iL': ['WT', '#159', '#278', '#222']
}

df = pd.read_excel("Pp_roGFP2_Data_evaluation.xlsx", index_col=[0,1], sheet_name="RatiosLines")  # type: pd.DataFrame

matplotlib.rc("text", usetex=True)
matplotlib.rc("font", family="serif")
matplotlib.rc("font", serif="Computer Modern Roman")
matplotlib.rc("figure", autolayout=True)

for sensor, lines in config.items():
    figure = plt.figure(figsize=figsize, dpi=dpi)

    data = []
    for line in lines:
        data.append(df.loc[(sensor, line), "Ratio"].values)

    ax = figure.subplots()

    bp = ax.boxplot(data)
    ax.set_xticklabels([s.replace("#", "\#") for s in lines])

    ax.set_ylabel("ratio (405nm/488nm)")

plt.show()
