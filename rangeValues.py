import numpy as np
import sys
from optparse import OptionParser

from utils import obtain_parameters
from test_models_20news import test20news
from test_models_cifar import testCifar
from test_models_snippets import testSnippets
from test_models_TMC import testTMC

op = OptionParser()
op.add_option("-p", "--ps", type=float, default=1.0, help="supervision level (float[0.1,1.0])")
(opts, args) = op.parse_args()
ps = float(opts.ps)

alphaVal, betaVal, lambdaVal = obtain_parameters()
nbits= 16

for alpha in alphaVal:
    for beta in betaVal:
        for lambda_ in lambdaVal:

            print("TESTING 20NEWS")
            print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)
            test20news(model=3, ps=ps, addvalidation=1, alpha=alpha, beta=beta, lambda_=lambda_, repetitions=5, nbits=nbits,
                       ofilename='SSBVAE_20NEWS-'+ str(nbits) +'BITS-' + str(alpha) +'ALPHA-'+ str(beta)+'BETA-'+ str(lambda_) +'LAMBDA.csv')

            # print("TESTING CIFAR")
            # print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)
            # testCifar(model=3, ps=ps, addvalidation=1, alpha=alpha, beta=beta, lambda_=lambda_, repetitions=5, nbits=nbits,
            #            ofilename='SSBVAE_CIFAR-'+ str(nbits) +'BITS-' + str(alpha) +'ALPHA-'+ str(beta)+'BETA-'+ str(lambda_) +'LAMBDA.csv')

            print("TESTING SNIPPETS")
            print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)
            testSnippets(model=3, ps=ps, addvalidation=1, alpha=alpha, beta=beta, lambda_=lambda_, repetitions=5, nbits=nbits,
                       ofilename='SSBVAE_SNIPPETS-'+ str(nbits) +'BITS-' + str(alpha) +'ALPHA-'+ str(beta)+'BETA-'+ str(lambda_) +'LAMBDA.csv')

            print("TESTING TMC")
            print("Alpha: ", alpha, " Beta: ", beta, " Lambda :", lambda_)
            testTMC(model=3, ps=ps, addvalidation=1, alpha=alpha, beta=beta, lambda_=lambda_, repetitions=5, nbits=nbits,
                       ofilename='SSBVAE_TMC-'+ str(nbits) +'BITS-' + str(alpha) +'ALPHA-'+ str(beta)+'BETA-'+ str(lambda_) +'LAMBDA.csv')


