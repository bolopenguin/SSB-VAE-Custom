import numpy as np
import sys
from optparse import OptionParser

from utils import obtain_parameters
from test_models_20news import test20news
from test_models_cifar import testcifar
from test_models_snippets import testsnippets
from test_models_TMC import testtmc

op = OptionParser()
op.add_option("-M", "--model", type=int, default=3, help="model type (1,2,3)")
op.add_option("-p", "--ps", type=float, default=1.0, help="supervision level (float[0.1,1.0])")
op.add_option("-a", "--alpha", type=float, default=0.0, help="alpha value")
op.add_option("-b", "--beta", type=float, default=0.003906, help="beta value")
op.add_option("-l", "--lambda_", type=float, default=0.0, help="lambda value")
op.add_option("-r", "--repetitions", type=int, default=2, help="repetitions")
op.add_option("-s", "--reseed", type=int, default=0, help="if >0 reseed numpy for each repetition")
op.add_option("-v", "--addvalidation", type=int, default=1, help="if >0 add the validation set to the train set")
op.add_option("-c", "--length_codes", type=int, default=16, help="number of bits")
op.add_option("-d", "--ds", type="string", default="20news", help="Dataset to train: 20news, cifar, tmc, snippets")

(opts, args) = op.parse_args()
ps = float(opts.ps)
dataset = str(opts.ds).lower()


if (dataset == "20news"):
    print("TESTING 20NEWS")
    test20news(model=3, ps=ps, addvalidation=1, alpha=opts.alpha, beta=opts.beta, lambda_=opts.lambda_, repetitions=opts.repetitions, nbits=opts.length_codes,
               ofilename='./Results/SSBVAE_20NEWS-' + str(opts.length_codes) + 'BITS-' + str(opts.alpha) + 'ALPHA-' + str(
                   opts.beta) + 'BETA-' + str(lambda_) + 'LAMBDA.csv')

elif (dataset == "cifar"):
    print("TESTING CIFAR")
    testcifar(model=3, ps=ps, addvalidation=1, alpha=opts.alpha, beta=opts.beta, lambda_=opts.lambda_, repetitions=opts.repetitions, nbits=opts.length_codes,
              ofilename='./Results/SSBVAE_CIFAR-' + str(opts.length_codes) + 'BITS-' + str(opts.alpha) + 'ALPHA-' + str(
                  opts.beta) + 'BETA-' + str(lambda_) + 'LAMBDA.csv')

elif (dataset == "snippets"):
    print("TESTING SNIPPETS")
    testsnippets(model=3, ps=ps, addvalidation=1, alpha=opts.alpha, beta=opts.beta, lambda_=opts.lambda_, repetitions=opts.repetitions, nbits=opts.length_codes,
                 ofilename='./Results/SSBVAE_SNIPPETS-' + str(opts.length_codes) + 'BITS-' + str(opts.alpha) + 'ALPHA-' + str(
                     opts.beta) + 'BETA-' + str(lambda_) + 'LAMBDA.csv')

elif (dataset == "tmc"):
    print("TESTING TMC")
    testtmc(model=3, ps=ps, addvalidation=1, alpha=opts.alpha, beta=opts.beta, lambda_=opts.lambda_, repetitions=opts.repetitions, nbits=opts.length_codes,
            ofilename='./Results/SSBVAE_TMC-' + str(opts.length_codes) + 'BITS-' + str(opts.alpha) + 'ALPHA-' + str(
                opts.beta) + 'BETA-' + str(lambda_) + 'LAMBDA.csv')
else:
    raise ValueError('ERROR: WRONG DATASET NAME')
