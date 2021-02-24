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
        print("------------------------------------------------------")
        print(name + " @Level" + str(level))
        print()
        df = eval("df_" + name + "[df_" + name + "[\"level\"]==" + str(level) + "]")
        df = df.drop("level", 1)

        #I create lists without repetitions of the parameters used for training/testing
        alphaValues = np.sort(df['alpha'].unique())
        betaValues = np.sort(df['beta'].unique())
        lambdaValues = np.sort(df['lambda'].unique())

        # Took the first n_rows values in order of accuracy
        df_top = df[df['p@100'].isin(list(df['p@100'].nlargest(n_rows)))].sort_values(by="p@100", ascending=False).reset_index(drop=True)
        df_bot = df[df['p@100'].isin(list(df['p@100'].nsmallest(n_rows)))].sort_values(by="p@100",ascending=True).reset_index(drop=True)

        print("Best Values: ")
        print(df_top)
        print()
        print("Worse Values: ")
        print(df_bot)
        print()

        # List to store the most frequent values for the hyper-parameter
        top_values = []
        bot_values = []
        for col in cols:
            # Count the occurrences of the different values in the top
            top_value = df_top[col].value_counts().idxmax()
            bot_value = df_bot[col].value_counts().idxmin()
            top_occ = df_top[col].value_counts().max()
            bot_occ = df_bot[col].value_counts().min()
            # If one occurrence is not frequent (tie) we take the first value (so with an higher accuracy)
            if top_occ == 1:
                top_value = df_top[col][0]
            if bot_occ == 1:
                bot_value = df_bot[col][0]
            top_values.append(top_value)
            bot_values.append(bot_value)

        top_values = np.asarray(top_values)
        bot_values = np.asarray(bot_values)
        diff = top_values - bot_values
        for i in range(len(cols)):
            if diff[i] > 0: print(cols[i] + " gives the best results when it is higher ")
            elif diff[i] < 0: print(cols[i] + " gives the best results when it is lower")
            else:  print(cols[i] + " does not influence in the results ")
        print()

        #TODO: check per controllare che non si ripetino i valori
        indexAlpha, = np.where(alphaValues == top_values[0])
        indexBeta, = np.where(betaValues == top_values[1])
        indexLambda, = np.where(lambdaValues == top_values[2])

        if indexAlpha == 0:
            operatorAlpha = "low"
            print("The best Alpha value is " + str(top_values[0]) + ", i.e. the lowest among those available")
            new_alpha = [top_values[0], top_values[0]/10, top_values[0]/100]
        elif indexAlpha == 1:
            operatorBeta = "medium"
            print("The best Alpha value is " + str(top_values[0]) + ", that is the average value among those available")
            new_alpha = [top_values[0], top_values[0] * 10, top_values[0] / 10]
        else:
            operatorLambda = "high"
            print("The best Alpha value is " + str(top_values[0]) + ", i.e. the highest among those available")
            new_alpha = [top_values[0], top_values[0] * 10, top_values[0] * 100]

        if indexBeta == 0:
            operatorBeta = "low"
            print("The best Beta value is " + str(top_values[1]) + ", i.e. the lowest among those available")
            new_beta = [top_values[1], top_values[1]/10, top_values[1]/100]
        elif indexBeta == 1:
            operatorBeta = "medium"
            print("The best Beta value is " + str(top_values[1]) + ", that is the average value among those available")
            new_beta = [top_values[1], top_values[1]/10, top_values[1]*10]
        else:
            operatorLambda = "high"
            print("The best Beta value is " + str(top_values[1]) + ", i.e. the highest among those available")
            new_beta = [top_values[1], top_values[1]*10, top_values[1]*100]

        if indexLambda == 0:
            operatorLambda = "low"
            print("The best Lambda value is " + str(top_values[2]) + ", i.e. the lowest among those available")
            new_lambda = [top_values[2], top_values[2]/2, top_values[2]/4]
        elif indexLambda == 1:
            operatorLambda = "medium"
            print("The best Lambda value is " + str(top_values[2]) + ", that is the average value among those available")
            new_lambda = [top_values[2], top_values[2]/2, top_values[2]*2]
        else:
            operatorLambda = "high"
            print("The best Lambda value is " + str(top_values[2]) + ", i.e. the highest among those available")
            new_lambda = [top_values[2], top_values[2] * 2, top_values[2] * 4]

        print()
        print("New alpha values: \n", new_alpha)
        print("New beta values: \n", new_beta)
        print("New lambda values: \n", new_lambda)

