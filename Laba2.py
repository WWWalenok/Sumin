
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import math

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')


N = 2

m = 150 + 0.5 * N

nu = 0.659E-3

T = 300 + 1.2 * N

D : list = [
    0.8 + 0.001 * N,
    0.3 + 0.01 * N,
    0.42 + 0.001 * N
]

L : list = [
    1 + 0.05 * N,
    0.9 + 0.05 * N,
    1.1 + 0.05 * N
]

C : list = [
    0.5,
    0.2,
    1
]

DHM = [0] * 3
DHL = [0] * 3
V = [0] * 3
RE = [0] * 3
La = [0] * 3

SHM = 0
SHL = 0
g = 9.81
ro = 878.4
v = 2E-3

for i in range(0, 3) :
    V[i] = m / (ro * D[i] * D[i] * 3.14 * 0.25)
    RE[i] = V[i] * D[i] / v
    if RE[i] < 2320 :
        La[i] = 64 / RE[i]
    elif RE[i] < 4000 :
        La[i] = 1.47E-5*RE[i]
    elif RE[i] < 1.0E3:
        La[i] = 0.3164 * math.pow(RE[i], -0.25)
    elif RE[i] < 1.0E6:
        La[i] = 0.11 * pow(68 / RE[i] + 0.001 / D[i], 0.25)
    else :
        La[i] = 0.11 * pow(0.001 / D[i], 0.25)

    DHM[i] = C[i] * V[i] * V[i] / (2 * g)
    SHM += DHM[i]

    DHL[i] = La[i] * L[i] / D[i] * V[i] * V[i] / (2 * g)
    SHL += DHM[i]



print(V)
print(D)
print(DHM)
print(DHL)
print(La)
print(RE)

if SHM > SHL * 0.25 :
    print('Short')
else :
    print('Long')