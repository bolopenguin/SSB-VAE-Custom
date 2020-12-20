import numpy as np
import sys
from optparse import OptionParser

from utils import obtain_parameters
from test_models_20news import test20news
from test_models_cifar import testcifar
from test_models_snippets import testsnippets
from test_models_TMC import testtmc

op = OptionParser()
op.add_option("-p", "--ps", type=float, default=1.0, help="supervision level (float[0.1,1.0])")
op.add_option("-d", "--ds", type="string", default="20news", help="Dataset to train: 20news, cifar, tmc, snippets")
(opts, args) = op.parse_args()
ps = float(opts.ps)
dataset = str(opts.ds).lower()

# alphaVal, betaVal, lambdaVal = obtain_parameters(ps, dataset)
alphaVal, betaVal, lambdaVal = obtain_parameters()
alphaVal = np.array(alphaVal).astype(np.float)
betaVal = np.array(betaVal).astype(np.float)
lambdaVal = np.array(lambdaVal).astype(np.float)

nbits= 16

for alpha in alphaVal:
    for beta in betaVal:
        for lambda_ in lambdaVal:

            if(dataset == "20news"):
                print("TESTING 20NEWS")
                print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)
                test20news(model=3, ps=ps, addvalidation=1, alpha=alpha, beta=beta, lambda_=lambda_, repetitions=2, nbits=nbits,
                           ofilename='./Results/SSBVAE_20NEWS-'+ str(nbits) +'BITS-' + str(alpha) +'ALPHA-'+ str(beta)+'BETA-'+ str(lambda_) +'LAMBDA.csv')

            elif(dataset == "cifar"):
                print("TESTING CIFAR")
                print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)
                testcifar(model=3, ps=ps, addvalidation=1, alpha=alpha, beta=beta, lambda_=lambda_, repetitions=2, nbits=nbits,
                           ofilename='./Results/SSBVAE_CIFAR-'+ str(nbits) +'BITS-' + str(alpha) +'ALPHA-'+ str(beta)+'BETA-'+ str(lambda_) +'LAMBDA.csv')

            elif(dataset=="snippets"):
                print("TESTING SNIPPETS")
                print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)
                testsnippets(model=3, ps=ps, addvalidation=1, alpha=alpha, beta=beta, lambda_=lambda_, repetitions=2, nbits=nbits,
                           ofilename='./Results/SSBVAE_SNIPPETS-'+ str(nbits) +'BITS-' + str(alpha) +'ALPHA-'+ str(beta)+'BETA-'+ str(lambda_) +'LAMBDA.csv')

            elif(dataset=="tmc"):
                print("TESTING TMC")
                print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)
                testtmc(model=3, ps=ps, addvalidation=1, alpha=alpha, beta=beta, lambda_=lambda_, repetitions=2, nbits=nbits,
                           ofilename='./Results/SSBVAE_TMC-'+ str(nbits) +'BITS-' + str(alpha) +'ALPHA-'+ str(beta)+'BETA-'+ str(lambda_) +'LAMBDA.csv')
            else:
                raise ValueError('ERROR: WRONG DATASET NAME')


