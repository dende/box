import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color, linewidth=1.5)
    plt.setp(bp['whiskers'], color=color, linewidth=1.5)
    plt.setp(bp['caps'], color=color, linewidth=1.5)
    plt.setp(bp['medians'], linewidth=1.5)


def main():

    figsize = (6.4, 4.8)
    markersize = 2
    dpi = 300

    red = "#A50026"
    blue = "#313695"
    black = "#000000"

    # config = {
    #     'secr. roGFP2-Orp1': ['WT', '#19', '#131', '#69'],
    #     'secr. Grx1-roGFP2iL': ['WT', '#159', '#278', '#222']
    # }

    # config = {
    #     'secrroGFP2-Orp1': ['#19', '#69', '#131'],
    #     'secrGrx1-roGFP2iL': ['#159', '#222', '#278'],
    # }

    config = {
        'secr. roGFP2-Orp1': ["DPS", "phys", "DTT"]
    }

    wavelengths = [420, 480]

    df = pd.read_excel("210507_Ratios_trans-expr_secr_roGFP2-Orp1.xlsx", index_col=[0, 1], sheet_name="Tabelle1")  # type: pd.DataFrame

    matplotlib.rc("text", usetex=True)
    matplotlib.rc("font", family="serif")
    matplotlib.rc("font", serif="Computer Modern Roman")
    matplotlib.rc("figure", autolayout=True)

    for sensor, treatments in config.items():
        figure = plt.figure(figsize=figsize, dpi=dpi)

        ax = figure.subplots()
        ax.plot([], c=red, label='oxidized')
        ax.plot([], c=black, label='phys.')
        ax.plot([], c=blue, label='reduced')
        ax.legend()

        data = []
        bp = ax.boxplot(df.loc[(sensor, "DPS"), f"Ratio"].values, positions=[1], widths=.35)
        set_box_color(bp, red)
        bp = ax.boxplot(df.loc[(sensor, "phys."), f"Ratio"].values, positions=[2], widths=.35)
        set_box_color(bp, black)
        bp = ax.boxplot(df.loc[(sensor, "DTT"), f"Ratio"].values, positions=[3], widths=.35)
        set_box_color(bp, blue)

        ax.set_xticklabels(treatments)
        ax.set_ylabel("Ratio of 405nm / 488nm")
        ax.set_title(f"Ratios of {sensor}")
    plt.show()


if __name__ == "__main__":
    main()
