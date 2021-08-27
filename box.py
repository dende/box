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

    config = {
        'secrroGFP2-Orp1': ['#19', '#69', '#131'],
        'secrGrx1-roGFP2iL': ['#159', '#222', '#278'],
    }

    wavelengths = [420, 480]
    treatments = ["phys", "DPS", "DTT"]

    df = pd.read_excel("roGFP2_stable_lines_ratios_calibration_CLSM.xlsx", index_col=[0, 1, 2], sheet_name="Tabelle1")  # type: pd.DataFrame

    matplotlib.rc("text", usetex=True)
    matplotlib.rc("font", family="serif")
    matplotlib.rc("font", serif="Computer Modern Roman")
    matplotlib.rc("figure", autolayout=True)

    for sensor, lines in config.items():
        figure = plt.figure(figsize=figsize, dpi=dpi)

        ax = figure.subplots()
        ax.plot([], c=red, label='oxidized')
        ax.plot([], c=black, label='phys.')
        ax.plot([], c=blue, label='reduced')
        ax.legend()

        line_basepos = 1
        for line in lines:
            data = []

            bp = ax.boxplot(df.loc[(sensor, line, "DPS" ), f"Ratio"].values, widths=0.18, positions=[line_basepos - 0.2])
            set_box_color(bp, red)
            bp = ax.boxplot(df.loc[(sensor, line, "phys"), f"Ratio"].values, widths=0.18, positions=[line_basepos])
            set_box_color(bp, black)
            bp = ax.boxplot(df.loc[(sensor, line, "DTT" ), f"Ratio"].values, widths=0.18, positions=[line_basepos + 0.2])
            set_box_color(bp, blue)

            ax.boxplot(data)
            ax.set_xticks([1,3,5])

            ax.set_xticklabels([s.replace("#", r"\#") for s in lines])
            ax.set_ylabel("Ratio of 405nm / 488nm")
            ax.set_title(f"Ratios of {sensor}")
            line_basepos = line_basepos + 2
    plt.show()



if __name__ == "__main__":
    main()
