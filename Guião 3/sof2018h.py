from bayes_net import *

# Crie uma nova rede de Bayes
bn = BayesNet()

# Adicione as variáveis à rede
bn.add('sc', [], 0.6)
bn.add('pt', [], 0.05)
bn.add('pa', [('pt', True)], 0.25)
bn.add('pa', [('pt', False)], 0.004)
bn.add('cp', [('sc', True), ('pa', True)], 0.02)
bn.add('cp', [('sc', True), ('pa', False)], 0.01)
bn.add('cp', [('sc', False), ('pa', True)], 0.011)
bn.add('cp', [('sc', False), ('pa', False)], 0.001)
bn.add('cnl', [('sc', True)], 0.9)
bn.add('cnl', [('sc', False)], 0.001)
bn.add('fr', [('pt', True), ('pa', True)], 0.9)
bn.add('fr', [('pt', True), ('pa', False)], 0.9)
bn.add('fr', [('pt', False), ('pa', True)], 0.1)
bn.add('fr', [('pt', False), ('pa', False)], 0.01)

# Calcule a probabilidade conjunta
conjunction = [('sc', True), ('pt', True), ('pa', True), 
               ('cp', True), ('cnl', True), ('fr', True)]
print(bn.jointProb(conjunction))