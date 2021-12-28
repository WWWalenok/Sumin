
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


dH : list = [
    0.0,
    0.85,
    0.85,
    0.12,
    2.2,
    1.2,
    3
]
N = 2

S = 13


Vm = 5


H7 = 50 + 1.5 * N


nu = 6.59E-3


B : list = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0
]


L : list = [
    10 + 0.8 * N,
    20 + 0.5 * N,
    250 + 2 * N,
    180 + 0.9 * N,
    150 + 0.6 * N,
    220 + 0.6 * N,
    300 + 0.8 * N,
    180 + 1.1 * N,
    50 + 0.69 * N,
    150 + 0.9 * N,
    150 + 0.9 * N,
    180 + 0.85 * N,
    280 + 0.55 * N
]


Q : list = [
    0, # 1
    0, # 2
    0, # 3
    0, # 4
    0, # 5
    0, # 6
    190 + 0.5 * N, # 7
    120 + 0.5 * N, # 8
    0, # 9
    120 + 0.9 * N, # 10
    250 + 0.75 * N, # 11
    180 + 0.5 * N, # 12
    220 + 0.6 * N # 13
]

Q[0] = Q[1] = Q[2] = \
    Q[6] + \
    Q[7] + \
    Q[9] + \
    Q[10] + \
    Q[11] + \
    Q[12]

Q[3] = \
    Q[6] + \
    Q[9] + \
    Q[10] + \
    Q[11] + \
    Q[12]

Q[4] = \
    Q[6] + \
    Q[9] + \
    Q[10] + \
    Q[12]

Q[5] = \
    Q[6] + \
    Q[12]

Q[8] = \
    Q[9] + \
    Q[10]


H : list = [
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    H7,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1
]


D = [0] * S

V = [0] * S

KH : list = [
    0,
    0.1,
    1.0,
    1.0,
    1.0,
    1.0,
    2,
    2,
    1.0,
    2,
    2,
    2,
    2
]


DH = [0] * S

DHM = [0] * S


Re = [0] * S


La = [0] * S


MQ = 0

for i in range(0, S) :
    if B[i] == 1 :
        MQ = max(MQ, Q[i])

MD = 2 * math.sqrt(MQ / Vm / 3.14)


GostC = 9


Gost : list = [
    6,
    8,
    10,
    15,
    20,
    25,
    32,
    40,
    50
]

for i in range(0, GostC) :
    if (MD < Gost[i]) :
        MD = Gost[i]
        break




for i in range(0, S) :
    if B[i] == 1 :
        D[i] = MD

for i in range(0, S) :
    if not B[i] :
        D[i] = 2 * math.sqrt(Q[i] / Vm / 3.14)
    V[i] = 4 * Q[i] / (D[i] * D[i] * 3.14)

    Re[i] = V[i] * D[i] / nu

    if Re[i] < 2320:
        La[i] = 64 / Re[i]
    elif Re[i] < 4000:
        La[i] = 1.47E-5 * Re[i]
    elif Re[i] < 1.0E3:
        La[i] = 0.3164 * math.pow(Re[i], -0.25)
    elif Re[i] < 1.0E6:
        La[i] = 0.11 * pow(68 / Re[i] + 0.001 / D[i], 0.25)
    else:
        La[i] = 0.11 * pow(0.001 / D[i], 0.25)

    DH[i] = (La[i] * L[i] / D[i]) * V[i] * V[i] / 19.62

    DHM[i] = (KH[i]) * V[i] * V[i] / 19.62




H[6] = H7

for i in range(0, 6) :
    H[5 - i] = H[6 - i] + DH[6 - i] + DHM[6 - i]

H[12] = H[5] - DH[12] - DHM[12]
H[8] = H[4] - DH[8] - DHM[8]
H[11] = H[3] - DH[11] - DHM[11]
H[7] = H[2] - DH[7] - DHM[7]
H[9] = H[8] - DH[9] - DHM[9]
H[10] = H[8] - DH[10] - DHM[10]


print(H)
print(DH)
print(V)
print(Re)
print(La)

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

# Import Data

X_tag = 'N'
Y1_tags = 'H'
Y2_tags = 'V'

# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1, 1, figsize=(16,9))

x = [0] * 7 * 2

for i in range(0, 7) :
    for j in range(0, i):
        x[i * 2] += L[j]
        x[i * 2 + 1] += L[j]


y = [0] * 7 * 2

for i in range(0, 7) :
    y[i * 2] = H[i] + DHM[i]
    y[i * 2 + 1] = H[i]


ax1.plot(x, y)

v = [0] * 7 * 2

for i in range(0, 7) :
    v[i * 2] = V[i]
    v[i * 2 + 1] = V[i]

ax2 = ax1.twinx()
ax2.plot(x, v, color='red')

# Plot Line2 (Right Y Axis)

ax1.set_title("Зависимость", fontsize=22)

# Decorations
# ax1 (left Y axis)
ax1.set_xlabel(X_tag, fontsize=20)
ax1.tick_params(axis='x', rotation=0, labelsize=12)
ax1.set_ylabel(Y1_tags, color='tab:blue', fontsize=20)
ax1.tick_params(axis='y', rotation=0, labelcolor='tab:blue' )
ax1.grid(alpha=.4)

ax2.set_ylabel(Y2_tags, color='tab:red', fontsize=20)

ax2.tick_params(axis='y', labelcolor='tab:red')

fig.tight_layout()
plt.show()