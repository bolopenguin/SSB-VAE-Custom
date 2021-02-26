# SSB-VAE: Self-Supervised Bernoulli Autoencoders for Semi-Supervised Hashing

This repository contains the code to reproduce the results presented in the paper 
[*Self-Supervised Bernoulli Autoencoders for Semi-Supervised Hashing*](https://arxiv.org/abs/2007.08799).
# Description

We investigate the robustness of hashing methods based on variational autoencoders 
to the lack of supervision, focusing on two semi-supervised approaches currently in use. 
In addition, we propose a novel supervision approach in which the model uses 
its own predictions of the label distribution to implement the pairwise objective. Compared to the best 
baseline, this procedure yields similar performance in 
fully-supervised settings but improves significantly the results when labelled data is scarce.

Then we can search for the best hyper-parameters through a grid search which tries different set of values 
and generates new values based on the precision achieved on the training.

# Requirements

Python 3.7

Tensorflow 2.1

Keras 2.3.1

# Usage

The code is organised in four different scripts, one per dataset. 
Specifically, the scripts *test_model_[**data**].py* considers the dataset **data** and take as input 
the following parameters:


- *M* is the index of the model considered. In particular, we compare three semi-supervised
 methods based on variational autoencoders: *(M=1)* **VDHS-S** is a variational autoencoder 
 proposed in [[1]](#1) that employs Gaussian latent variables, unsupervised learning and pointwise supervision; 
 *(M=2)* **PHS-GS** is a variational autoencoder proposed in [[2]](#2) that assumes Bernoulli latent variables, 
 unsupervised learning, and both pointwise and pairwise supervision; 
 and *(M=3)* **SSB-VAE** is our proposed method based on Bernoulli latent variable, unsupervised learning, pointwise 
 supervision and self-supervision.

- *p* is the level (percentage) of supervision to consider when training the autoencoder based on semi-supervised approach.
- *a*, *b* and *l* a,b,l are the hyperparameters associated to the different components of the semi-supervised
 loss. In particular, *a* is the coefficient of the pointwise component, *l* is associated to the pairwise component 
 and *b* is the weight associated to the KL divergence when computing the unsupervised loss
- *r* is the number of experiments to perform, given a set of parameters. This is used to compute an average performance
considering multiple initialisation of the same neural network. Notice that the results reported in the paper are 
computing by averaging *r=5* experiments.
- *l* is the size of the latent sub-space generated by the encoder. This also corresponds to the number of bits of 
the generated hash codes.

The script utils.py is used to import the needed packages and all of the custom routines for performance evaluation.

The script base_networks.py contains the custom routines to define all the components of a neural networks.

The script supervised_BAE.py defines the three types of autoencoder (*VDSH, PHS, SSB-VAE*).
 
The script test_values.py allows to test the software over a chosen dataframe and set of values.

The script test_values_all.py allows to perform the grid search over the values contained in the css inside the folder Hyperparameters over a chosen
dataframe.

The script new_values.py generates the new values for the hyper-parameters to test in the following runs of the code.

The script visualising.py allows to build graph over the results achieved to study the precision of the different hyper-parameters set.

The script post_processing.py allows to collect all the results provided by the test_values.py and test_values_all.py files and it computes the
 tables as reported in the paper.

## Guide to the usage

To test a particular dataset over a set of chosen hyper-parameters values run the script:
``` 
python test_values.py -M 3 -p 1 -a 10 -b 100 -l 0.01 -r 2 -s 0 -v 1 -c 16 -d snippets
```
The output will be inside the csv: *./Results/ResultsTraning/SSBVAE_SNIPPETS-16BITS-10ALPHA-100BETA-0.01LAMBDA.csv*

To search for the best hyper-parameters run the following scripts in order:
``` 
python test_values_all.py -M 3 -r 2 -s 0 -v 1 -c 16 -d snippets
cd Results
python post_processing.py
python new_values.py
cd ../
```
And then repeat again in order to try the new values (which will lead to a better precision).
The results of the test_values_all.py are stored in the csv inside the folder Results/ResultsTraining
The table built by the script post_processing.py is stored inside the folder Results/ResultsPostProcessing
The new hyper-parameters generated by the script new_values.py are stored inside the folder Hyperparameters

To generate the graphs stored in the directory Images run the following script:
``` 
python visualising.py -c 16
```

# References
<a id="1">[1]</a> 
 S. Chaidaroon and Y. Fang. “Variational deep semantic hashing for text documents”. SIGIR. 2017, pp. 75–84. 

<a id="1">[2]</a>  S. Z. Dadaneh et al. “Pairwise Supervised Hashing with Bernoulli Variational Auto-Encoder and Self-Control Gradient Estimator”. Proc. UAI. 2020
