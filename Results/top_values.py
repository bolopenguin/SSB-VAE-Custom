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

data = load_dataset()

df_20News = data[data["dataset"] == "20News"]
df_TMC = data[data["dataset"] == "TMC"]
df_Snippets = data[data["dataset"] == "Snippets"]
df_CIFAR = data[data["dataset"] == "CIFAR-10"]

n_rows = 5

for name in dataset_names:
    for level in supervised_levels:
        print("Doing " + name + " @Level" + str(level))
        df = eval("df_" + name + "[df_" + name + "[\"level\"]==" + str(level) + "]")
        df = df.drop("level", 1)

        df = df[df['p@100'].isin(list(df['p@100'].nlargest(n_rows)))].sort_values(by="p@100", ascending=False).reset_index(drop=True)
        print(df)

        #alpha = df["alpha"].sum()/n_rows
        #beta = df['beta'].sum()/n_rows
        #lambda_ = df['lambda'].sum()/n_rows

        #print(alpha, beta, lambda_)

