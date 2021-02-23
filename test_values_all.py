import numpy as np
import sys
from optparse import OptionParser
from test_models_20news import test20news
from test_models_TMC import testtmc
from test_models_cifar import testcifar
from test_models_snippets import testsnippets
from utils import obtain_parameters

op = OptionParser()
op.add_option("-M", "--model", type=int, default=3, help="model type (1,2,3)")
op.add_option("-p", "--ps", type=float, default=1.0, help="supervision level (float[0.1,1.0])")
op.add_option("-a", "--alpha", type=float, default=0.0, help="alpha value")
op.add_option("-b", "--beta", type=float, default=0.003906, help="beta value")
op.add_option("-l", "--lambda_", type=float, default=0.0, help="lambda value")
op.add_option("-r", "--repetitions", type=int, default=2, help="repetitions")
op.add_option("-s", "--reseed", type=int, default=0, help="if >0 reseed numpy for each repetition")
op.add_option("-v", "--addvalidation", type=int, default=1, help="if >0 add the validation set to the train set")
op.add_option("-c", "--nbits", type=int, default=16, help="number of bits")
op.add_option("-d", "--ds", type="string", default="20news", help="Dataset to train: 20news, cifar, tmc, snippets")

(opts, args) = op.parse_args()
nbits = opts.nbits
ps = float(opts.ps)
df = str(opts.ds).lower()
alphaVal, betaVal, lambdaVal = obtain_parameters(ps, df, nbits)

header = "test"+df
for alpha in alphaVal:
    for beta in betaVal:
        for lambda_ in lambdaVal:
            print("TESTING "+df.upper())
            print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)

            ofile="\"./Results/ResultsTraning/SSBVAE_"+df.upper()+"-"+str(nbits)+"BITS-"+str(alpha)+"ALPHA-"+str(beta)+"BETA-"+str(lambda_)+"LAMBDA.csv\""
            tail = "(model="+str(opts.model)+", ps=ps, addvalidation=1, alpha="+str(alpha)+", beta="+str(beta)+", lambda_="+str(lambda_)+\
                   ", repetitions=2, nbits="+str(nbits)+",ofilename="+ofile+")"
            func = header + tail
            eval(func)





