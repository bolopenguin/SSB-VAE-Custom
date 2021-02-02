import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

nbits = 16

def load_dataset():
    dataset = pd.read_csv("ResultsPostProcessing/table_"+str(nbits)+"bits.csv")
    return dataset

data = load_dataset()

df_20News=data[data["dataset"] == "20News"]
df_TMC=data[data["dataset"] == "TMC"]
df_Snippets=data[data["dataset"] == "Snippets"]
df_CIFAR=data[data["dataset"] == "CIFAR-10"]

dataset_names = ["CIFAR","20News", "TMC", "Snippets"]
supervised_levels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

path_image= "ResultsPostProcessing/Images/"

for name in dataset_names:
    for level in supervised_levels:
        print("Doing "+name+" @Level" + str(level))
        df = eval("df_"+name+"[df_"+name+"[\"level\"]=="+str(level)+"]")
        df = df.drop("level", 1)

        size = np.array(200 * (df['p@100']))
        g = sns.pairplot(df, hue="p@100", kind="scatter", diag_kind="hist",plot_kws={"s": size, 'alpha':0.4})
        #plt.show()
        g.savefig(path_image + name + "-" + str(level) + "Level.png")
        plt.close('all')
