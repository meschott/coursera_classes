import math, random, pylab

def V(x, cubic, quartic):
    pot = x ** 2 / 2.0 + cubic * x ** 3 + quartic * x ** 4
    return pot

def levy_harmonic_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        Ups1 = 1.0 / math.tanh(dtau) + \
               1.0 / math.tanh(dtau_prime)
        Ups2 = x[k - 1] / math.sinh(dtau) + \
               xend / math.sinh(dtau_prime)
        x.append(random.gauss(Ups2 / Ups1, \
               1.0 / math.sqrt(Ups1)))
    return x

def levy_free_path(xstart, xend, dtau, N):
    x = [xstart]
    for k in range(1, N):
        dtau_prime = (N - k) * dtau
        x_mean = (dtau_prime * x[k - 1] + dtau * xend) / \
                 (dtau + dtau_prime)
        sigma = math.sqrt(1.0 / (1.0 / dtau + 1.0 / dtau_prime))
        x.append(random.gauss(x_mean, sigma))
    return x

beta = 20.0
N = 100
sigma = 1.0 / math.sqrt(2.0 * math.tanh(beta/2.0))
dtau = beta / N
delta = 1.0
quartic = 1.0
cubic = -1.0
Ncut = N/8
n_steps = 4000000
n_accepted = 0
x = [1.0] * N
Trotter_weight_old = math.exp(sum(-V(a, cubic, quartic) * dtau for a in x))
data = []
for step in range(n_steps):
    if step % 100000 == 0:
        print step
    x_new = levy_free_path(x[0], x[Ncut], dtau, Ncut) + x[Ncut:]
    Trotter_weight_new = math.exp(sum(-V(a, cubic, quartic) * dtau for a in x_new))
    if random.uniform(0.0, 1.0) < min(1, Trotter_weight_new/Trotter_weight_old):
        x = x_new[:]
        n_accepted += 1
        Trotter_weight_old = Trotter_weight_new
    x = x[Ncut:] + x[:Ncut]
    if step % N == 0:
        k = random.randint(0, N - 1)
        data.append(x[k])

print "acceptance ratio is", n_accepted/float(n_steps)
pylab.hist(data, normed=True, bins=100, label='QMC')
#list_x = [0.1 * a for a in range (-30, 31)]
#list_y = [math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) * \
#          math.exp(-x ** 2 * math.tanh(beta / 2.0)) for x in list_x]
#pylab.plot(list_x, list_y, label='analytic')
#pylab.legend()
pylab.xlabel('$x$')
pylab.ylabel('frequency')
pylab.title('quantum anharmonic oscillator (beta=%s, N=%i, cubic=%s, quartic=%s)' % (beta, N, cubic, quartic))
#pylab.xlim(-2, 2)
#pylab.savefig('plot_B1_beta%s.png' % beta)
#pylab.show()

#y = [dtau * a for a in range(0,N)]
#pylab.plot(x, y)
#pylab.xlabel('$x$')
#pylab.ylabel('$beta$/N')
#pylab.title('naive_harmonic_path (beta=%s, N=%i)' % (beta, N))
pylab.savefig('plot_C1.png')
pylab.show()
