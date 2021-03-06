import math, numpy
import matplotlib.pyplot as plt
import numpy as np

#Compute the anharmonic potential
def V(x,cubic,quartic):
    pot = x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4
    return pot

def Energy_pert(n, cubic, quartic):
    return n + 0.5 - 15.0 / 4.0 * cubic **2 * (n ** 2 + n + 11.0 / 30.0) \
         + 3.0 / 2.0 * quartic * (n ** 2 + n + 1.0 / 2.0)

def Z_pert(cubic, quartic, beta, n_max):
    Z = sum(math.exp(-beta * Energy_pert(n, cubic, quartic)) for n in range(n_max + 1))
    return Z

# Free off-diagonal density matrix
def rho_free(x, xp, beta):
    return (math.exp(-(x - xp) ** 2 / (2.0 * beta)) /
            math.sqrt(2.0 * math.pi * beta))

# Anharmonic density matrix in the Trotter approximation (returns the full matrix)
def rho_anharmonic_trotter(grid, beta, cubic, quartic):
    return numpy.array([[rho_free(x, xp, beta) * \
                         numpy.exp(-0.5 * beta * (V(x,cubic,quartic) + V(xp,cubic,quartic))) \
                         for x in grid] for xp in grid])

quartic = [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5]
x_max = 5.0
nx = 100
dx = 2.0 * x_max / (nx - 1)
x = [i * dx for i in range(-(nx - 1) / 2, nx / 2 + 1)]

for q in quartic:
    beta_tmp = 2.0 ** (-6)                   # initial value of beta (power of 2)
    beta     = 2.0 ** 1                      # actual value of beta (power of 2)
    rho = rho_anharmonic_trotter(x, beta_tmp, -q, q)  # density matrix at initial beta
    while beta_tmp < beta:
        rho = numpy.dot(rho, rho)
        rho *= dx
        beta_tmp *= 2.0
#        print 'beta: %s -> %s' % (beta_tmp / 2.0, beta_tmp)
    Z_perturbation = Z_pert(-q, q, beta, nx)        
#    Z = sum(rho[j, j] for j in range(nx + 1)) * dx
    print q, Z_perturbation
#    pi_of_x = [rho[j, j] / Z for j in range(nx + 1)]
#    f = open('data_harm_matrixsquaring_beta' + str(beta) + '.dat', 'w')
#    for j in range(nx + 1):
#        f.write(str(x[j]) + ' ' + str(rho[j, j] / Z) + '\n')
#    f.close()

#x_range = np.arange(0,101,1)
#plt.plot(x_range, pi_of_x, ls='dotted', label = "pi_of_x anharmonic", color = 'red')
#quantum_P = []
#for i in x:
#    quantum_P.append(exact_prob(i, beta))
#plt.plot(x_range, quantum_P, ls = 'dashed', label="exact prob harmonic beta=%.2f" % beta)
#plt.title("Matrix squaring, trotter approximation density matrix fitted")
#plt.legend(loc='upper left', shadow = True, fontsize = 'medium')
#plt.xlabel("x")
#plt.ylabel("probability")
#plt.savefig("hw5_B1_beta_%.2f.png" % beta)
#plt.show()
