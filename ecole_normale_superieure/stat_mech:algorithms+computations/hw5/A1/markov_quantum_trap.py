import random, math
import matplotlib.pyplot as plt
import numpy as np

def probability(x):
    psi_0_sq = ((1/(math.pi ** 0.25)) * math.exp(-x ** 2/2.0)) ** 2
    return psi_0_sq

position_list = []
x = 0.0
delta = 0.5
for k in range(1000000):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  (probability(x_new)/probability(x)):
        x = x_new 
    position_list.append(x)

plt.hist(position_list,100,normed=True, label="binned position frequency")
#Build analytical function
n = np.arange(-5,6,0.01)
P = []
for i in n:
    P.append(probability(i))
plt.plot(n,P, label="analytical function")
plt.legend(loc='upper right', shadow = True, fontsize='medium')
plt.title("Markov and Metropolis: decaying exponential")
plt.xlabel("position x")
plt.ylabel("frequency")
plt.savefig("hw5_A1.png")
plt.show()


