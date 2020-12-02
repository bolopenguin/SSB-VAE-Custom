#Modifiche eseguite in ogni riga: 
#01- sostituito -l prima del 32 con -c
#Vecchia versione python test_models_cifar.py -M 1 -p 1.0 -v 1 -a 1000000.0 -b 0.000008 -g 0.0 -r 5 -l 32 -o 'VDSH_CIFAR-32BITS.csv'
#02) sostituito il valore di b con quello di -g ( che poi diventerà -l )
#Vecchia versione python test_models_cifar.py -M 1 -p 1.0 -v 1 -a 1000000.0 -b 0.000008 -l 0.0 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
#03) trasformare il valore di -b il prodotto di alpha per quello che era gamma


python test_models_cifar.py -M 1 -p 0.1 -v 1 -a 1000000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 0.2 -v 1 -a 100000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 0.3 -v 1 -a 1000000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 0.4 -v 1 -a 100000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 0.5 -v 1 -a 100000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 0.6 -v 1 -a 1000000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 0.7 -v 1 -a 100000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 0.8 -v 1 -a 100000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 0.9 -v 1 -a 1000000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'
python test_models_cifar.py -M 1 -p 1.0 -v 1 -a 1000000.0 -b 0.0 -l 0.000008 -r 5 -c 32 -o 'VDSH_CIFAR-32BITS.csv'

python test_models_cifar.py -M 2 -p 0.1 -v 1 -a 0.1 -b 100000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 0.2 -v 1 -a 1.0 -b 1000000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 0.3 -v 1 -a 1.0 -b 1000000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 0.4 -v 1 -a 10.0 -b 10000000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 0.5 -v 1 -a 10000 -b 100000000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 0.6 -v 1 -a 100 -b 100000000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 0.7 -v 1 -a 1.0 -b 10000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 0.8 -v 1 -a 1.0 -b 10000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 0.9 -v 1 -a 100.0 -b 100000 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'
python test_models_cifar.py -M 2 -p 1.0 -v 1 -a 100.0 -b 10 -l 0.003906 -r 5 -c 32 -o 'PHS_CIFAR-32BITS.csv'

python test_models_cifar.py -M 3 -p 0.1 -v 1 -a 100000 -b 100000000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 0.2 -v 1 -a 1 -b 1000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 0.3 -v 1 -a 10.0 -b 1000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 0.4 -v 1 -a 100 -b 10000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 0.5 -v 1 -a 1000000 -b 100000000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 0.6 -v 1 -a 1000 -b 100000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 0.7 -v 1 -a 1000 -b 10000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 0.8 -v 1 -a 1000000 -b 100000000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 0.9 -v 1 -a 1000000 -b 10000000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
python test_models_cifar.py -M 3 -p 1.0 -v 1 -a 1000 -b 1000000 -l 0.003906 -r 5 -c 32 -o 'SSBVAE_CIFAR-32BITS.csv'
