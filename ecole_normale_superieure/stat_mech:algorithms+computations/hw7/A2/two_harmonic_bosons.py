import math, random, pylab

def z(beta):
    return 1.0 / (1.0 - math.exp(- beta))

def pi_two_bosons(x, beta):
    pi_x_1 = math.sqrt(math.tanh(beta / 2.0)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta / 2.0))
    pi_x_2 = math.sqrt(math.tanh(beta)) / math.sqrt(math.pi) *\
             math.exp(-x ** 2 * math.tanh(beta))
    weight_1 = z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta))
    weight_2 = z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta))
    pi_x = pi_x_1 * weight_1 + pi_x_2 * weight_2
    return pi_x

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

def rho_harm_1d(x, xp, beta):
    Upsilon_1 = (x + xp) ** 2 / 4.0 * math.tanh(beta / 2.0)
    Upsilon_2 = (x - xp) ** 2 / 4.0 / math.tanh(beta / 2.0)
    return math.exp(- Upsilon_1 - Upsilon_2)

list_beta = [0.1 * a for a in range(1, 51)]
nsteps = 1000
prob_one_cycle = []
prob_two_cycles = []

for beta in list_beta:
    low = levy_harmonic_path(2)
    high = low[:]
    data = []
    perm1 = 0
    perm2 = 0
    for step in xrange(nsteps):
        # move 1
        if low[0] == high[0]:
            k = random.choice([0, 1])
            low[k] = levy_harmonic_path(1)[0]
            high[k] = low[k]
            perm1 += 1
        else:
            low[0], low[1] = levy_harmonic_path(2)
            high[1] = low[0]
            high[0] = low[1]
            perm2 += 1
        data += low[:]
        # move 2
        weight_old = (rho_harm_1d(low[0], high[0], beta) *
                  rho_harm_1d(low[1], high[1], beta))
        weight_new = (rho_harm_1d(low[0], high[1], beta) *
                  rho_harm_1d(low[1], high[0], beta))
        if random.uniform(0.0, 1.0) < weight_new / weight_old:
            high[0], high[1] = high[1], high[0]
    prob_one_cycle.append(perm1/float(nsteps))
    prob_two_cycles.append(perm2/float(nsteps))

fract_two_cycles = [z(beta) ** 2 / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]
fract_one_cycle = [z(2.0 * beta) / (z(beta) ** 2 + z(2.0 * beta)) for beta in list_beta]

pylab.plot(list_beta, prob_one_cycle, label = 'one cycle data', linewidth = 5)
pylab.plot(list_beta, prob_two_cycles, label = 'two cycle data', linewidth = 5)
pylab.plot(list_beta, fract_one_cycle, label = 'exact one cycle function')
pylab.plot(list_beta, fract_two_cycles, label = 'exact  two cycle function')

#pylab.hist(data, bins=100,normed=True, label = 'position of two bosons')
#xrange = [a*0.1 for a in range(-40, 40)]
#pi = [pi_two_bosons(a, beta) for a in xrange]
#pylab.plot(xrange, pi, label = 'exact solution', linewidth = 3)
pylab.title("fractional frequency of a permutation for various beta")
pylab.xlabel("beta")
pylab.ylabel("fraction")
pylab.legend(loc="upper right", shadow=True, fontsize = "medium")
pylab.savefig('fractions.png')
pylab.show()

