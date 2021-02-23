# Importazioni - Si importa tutto per sicurezza

# Importazioni per analisi dei dati attraverso Tabelle e Grafici
import os
import pandas as pd
import numpy as np


def load_dataset():
    dataset = pd.read_csv("ResultsPostProcessing/table_" + str(nbits) + "bits.csv")
    return dataset

nbits = 16
dataset_names = ["CIFAR", "20News", "TMC", "Snippets"]
supervised_levels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
cols = ["alpha", "beta", "lambda"]

data = load_dataset()

df_20News = data[data["dataset"] == "20News"]
df_TMC = data[data["dataset"] == "TMC"]
df_Snippets = data[data["dataset"] == "Snippets"]
df_CIFAR = data[data["dataset"] == "CIFAR-10"]

n_rows = 3

# loop over all the levels and datasets
for name in dataset_names:
    for level in supervised_levels:
        print("Doing " + name + " @Level " + str(level))
        df = eval("df_" + name + "[df_" + name + "[\"level\"]==" + str(level) + "]")
        df = df.drop("level", 1)
        # Took the first n_rows values in order of accuracy
        df = df[df['p@100'].isin(list(df['p@100'].nlargest(n_rows)))].sort_values(by="p@100", ascending=False).reset_index(drop=True)
        print(df)

        # List to store the most frequent values for the hyper-parameter
        top_values = []
        for col in cols:
            # Count the occurrences of the different values in the top
            top_value = df[col].value_counts().idxmax()
            top_occ = df[col].value_counts().max()
            # If one occurrence is not frequent (tie) we take the first value (so with an higher accuracy)
            if top_occ == 1:
                top_value = df[col][0]
            top_values.append(top_value)
        print(top_values)


