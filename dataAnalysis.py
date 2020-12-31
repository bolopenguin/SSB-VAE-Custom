#Importazioni - Si importa tutto per sicurezza

#Importazioni per analisi dei dati attraverso Tabelle e Grafici
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Importazione Librerie per grafica
from IPython.display import HTML  #For Gui
from tkinter import *             #Per Grafica
from tkinter.ttk import Combobox  #Combobox

#Importazione Librerie di Utility
import webbrowser                 #Per aprire i link
import codecs
import time
import datetime #Per utilizzare date ed orari
import requests #Per poter salvare i file di github
from os import getcwd #Per modellare il path
from pathlib import Path #Per poter verificare se un file esiste


pathfileResult = './Results/collectionAnalized/table_'
pathfile20News = './Results/popolation/20news_'
pathfileSnippets = './Results/popolation/snippets_'
pathfileTMC = './Results/popolation/tmc_'
pathfileCifar = './Results/popolation/cifar_'
estensioneResult = '_bits.csv'
estensionePopolation = 'bits_Population.csv'
estensioneCSV = '.csv'
algortihm = 'SSB_VAE'
dataset20News = '20news'
datasetCifar ='cifar'
datasetSnippets = 'snippets'
datasetTMC = 'tmc'

alphaRange = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000]
betaValue = [1000, 10000, 100000, 1000000, 1000000, 100000000, 1000000000, 10000000000, 100000000000]
lambdaValue = [0.000244, 0.015625, 0.06250]


def dataAnalysis(nbits):
    
    #Open the post training data collection table
    fileResult = pathfileResult + nbits + estensioneResult
    totalTable = pd.read_csv(fileResult, sep = ',', error_bad_lines=False)

    #Create the output file of analysis
    #Da decidere se fare 4 file (uno per dataset) e nel caso cambiare path e tabella oppure unico come ora
    header = ['dataset','level','algorithm','best alpha','average of best alpha','best beta','average of best beta','best lambda','average of best lambda','best alpha-beta','average of best alpha-beta','best alpha-lambda','average of best alpha-lambda','best beta-lambda','average of best beta-lambda','best alpha-beta-lambda','average of best alpha-beta-lambda']
    analysisTable = pd.DataFrame(columns=header)

    
    
    #1 Riga miglior Tripletta per ogni level per ogni dataset
    #2 
    #3
    
    
    #Output of population
    file20News = pathfile20News + nbits + estensionePopolation
    table20News = pd.read_csv(file20News, sep = ',', error_bad_lines=False)  
    
    fileSnippets = pathfileSnippets + nbits + estensionePopolation
    tableSnippets = pd.read_csv(fileSnippets, sep = ',', error_bad_lines=False)
    
    fileCifar = pathfileCifar + nbits + estensionePopolation
    table20News = pd.read_csv(fileCifar, sep = ',', error_bad_lines=False)  

    fileTMC = pathfileTMC + nbits + estensionePopolation
    tableTMC = pd.read_csv(fileTMC, sep = ',', error_bad_lines=False) 






    


    #The data is collected
    dataset = totalTable['dataset'].unique()
    print(dataset)
    alphaTotalTable = totalTable['alpha'].unique()
    print(alphaTotalTable)
    betaTotalTable = totalTable['beta'].unique()
    print(betaTotalTable)
    lambdaTotalTable = totalTable['lambda'].unique()
    print(lambdaTotalTable)
    
    #datePart = datetime.datetime.now().strftime("%Y_%m_%d")
    #filenameOutput = ".analysis/analysisTable" + datePart  + estensioneCSV
    #analysisTable.to_csv(filenameOutput,index=False,header=True)


    
dataAnalysis()


