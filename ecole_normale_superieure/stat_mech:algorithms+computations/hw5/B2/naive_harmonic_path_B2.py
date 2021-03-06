import math, random
import matplotlib.pyplot as plt

def rho_free(x, y, beta):    # free off-diagonal density matrix
    return math.exp(-(x - y) ** 2 / (2.0 * beta)) 

def read_file(filename):
    list_x = []
    list_y = []
    with open(filename) as f:
        for line in f:
            x, y = line.split()
            list_x.append(float(x))
            list_y.append(float(y))
    f.close()
    return list_x, list_y

beta = 4.0
N = 10                                            # number of slices
dtau = beta / N
delta = 1.0                                       # maximum displacement on one slice
n_steps = 10 ** 6                                 # number of Monte Carlo steps
x = [0.0] * N                                     # initial path
x_slice = []
slice = 0
for step in range(n_steps):
    k = random.randint(0, N - 1)                  # random slice
    knext, kprev = (k + 1) % N, (k - 1) % N       # next/previous slices
    x_new = x[k] + random.uniform(-delta, delta)  # new position at slice k
    old_weight  = (rho_free(x[knext], x[k], dtau) *
                   rho_free(x[k], x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x[k] ** 2))
    new_weight  = (rho_free(x[knext], x_new, dtau) *
                   rho_free(x_new, x[kprev], dtau) *
                   math.exp(-0.5 * dtau * x_new ** 2))
    if random.uniform(0.0, 1.0) < new_weight / old_weight:
        x[k] = x_new
    if step % 10 == 0:
        x_slice.append(x[slice])
    
plt.hist(x_slice, 100, normed = True, label = "x slice from path integral")
a,b = read_file("../B1/data_harm_matrixsquaring_beta4.0.dat")
plt.plot(a, b, label ="x from matrix multiplication")
plt.xlim(-2.0,2.0)
plt.title("Path integral x sampling")
plt.xlabel("x")
plt.ylabel("frequency")
plt.legend(loc = 'upper left', shadow = True, fontsize = 'medium')
plt.savefig("B2_slice_%i" % slice)
plt.show()
