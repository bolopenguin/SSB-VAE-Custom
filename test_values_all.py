import numpy as np
import sys
from optparse import OptionParser
from test_models_20news import test20news
from test_models_TMC import testtmc
from test_models_cifar import testcifar
from test_models_snippets import testsnippets
from utils import obtain_parameters

op = OptionParser()
op.add_option("-p", "--ps", type=float, default=1.0, help="supervision level (float[0.1,1.0])")
op.add_option("-d", "--ds", type="string", default="20news", help="Dataset to train: 20news, cifar, tmc, snippets")
(opts, args) = op.parse_args()
ps = float(opts.ps)
dataset = str(opts.ds).lower()

# alphaVal, betaVal, lambdaVal = obtain_parameters(ps, dataset)
alphaVal, betaVal, lambdaVal = obtain_parameters()
nbits= 16

header = "test"+dataset

for alpha in alphaVal:
    for beta in betaVal:
        for lambda_ in lambdaVal:
            print("TESTING "+dataset.upper())
            print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)

            ofile="\"./Results/SSBVAE_"+dataset.upper()+"-"+str(nbits)+"BITS-"+str(alpha)+"ALPHA-"+str(beta)+"BETA-"+str(lambda_)+"LAMBDA.csv\""
            tail = "(model=3, ps=ps, addvalidation=1, alpha="+str(alpha)+", beta="+str(beta)+", lambda_="+str(lambda_)+\
                   ", repetitions=2, nbits="+str(nbits)+",ofilename="+ofile+")"
            func = header + tail
            eval(func)





