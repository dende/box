import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)


def main():

    figsize = (6.4, 4.8)
    markersize = 2
    dpi = 200

    config = {
        'secr. roGFP2-Orp1': ['WT', '#19', '#131', '#69'],
        'secr. Grx1-roGFP2iL': ['WT', '#159', '#278', '#222']
    }

    wavelengths = [420, 480]

    df = pd.read_excel("Pp_roGFP2_Data_evaluation.xlsx", index_col=[0,1], sheet_name="Radiant efficiency")  # type: pd.DataFrame

    matplotlib.rc("text", usetex=True)
    matplotlib.rc("font", family="serif")
    matplotlib.rc("font", serif="Computer Modern Roman")
    matplotlib.rc("figure", autolayout=True)

    for sensor, lines in config.items():

        for wavelength in wavelengths:
            data = []
            figure = plt.figure(figsize=figsize, dpi=dpi)

            ax = figure.subplots()

            for line in lines:
                data.append(df.loc[(sensor, line), f"Avg Radiant Efficiency  at {wavelength} nm"].values)

            ax.boxplot(data)
            ax.set_xticklabels([s.replace("#", "\#") for s in lines])
            ax.set_ylabel("Radiant Efficiency [p/s/cm²/sr] / [µW/cm²]")
            ax.set_title(f"Radiant Efficience of {sensor} lines at {wavelength} nm")
    plt.show()



if __name__ == "__main__":
    main()
