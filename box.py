import pandas as pd
import matplotlib.pyplot as plt

config = {
    'secr. roGFP2-Orp1': ['WT', '#19', '#131', '#69'],
    'secr. Grx1-roGFP2iL': ['WT', '#159', '#278', '#222']
}

df = pd.read_excel("Pp_roGFP2_Data_evaluation.xlsx", index_col=[0,1], sheet_name="RatiosLines")  # type: pd.DataFrame


for sensor, lines in config.items():
    data = []
    for line in lines:
        data.append(df.loc[(sensor, line), "Ratio"].values)

    fig = plt.figure(figsize=(10, 7))

    bp = plt.boxplot(data)

    plt.show()
