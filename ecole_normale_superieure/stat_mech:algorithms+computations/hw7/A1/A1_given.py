import math, random, pylab

def pi_x(x, beta):
    sigma = 1.0 / math.sqrt(2.0 * math.tanh(beta / 2.0))
    return math.exp(-x ** 2 / (2.0 * sigma ** 2)) / math.sqrt(2.0 * math.pi) / sigma

def levy_harmonic_path(k):
    x = [random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(k * beta / 2.0)))]
    if k == 2:
        Ups1 = 2.0 / math.tanh(beta)
        Ups2 = 2.0 * x[0] / math.sinh(beta)
        x.append(random.gauss(Ups2 / Ups1, 1.0 / math.sqrt(Ups1)))
    return x[:]

beta = 2.0
nsteps = 1000000
low = levy_harmonic_path(2)
high = low[:]
data_0 = []
data_1 = []
for step in xrange(nsteps):
    k = random.choice([0, 1])
    low[k] = levy_harmonic_path(1)[0]
    high[k] = low[k]
    data_0.append(low[0])
    data_1.append(low[1])

    
pylab.hist(data_0, bins=100,normed=True, label = 'particle 0')
pylab.hist(data_1, bins=100,normed=True, label = 'particle 1')
xrange = [a*0.1 for a in range(-40, 40)]
pi = [pi_x(a, beta) for a in xrange]
pylab.plot(xrange, pi, label = 'exact solution', linewidth = 3)
pylab.title("position of two distinguishable non-interacting particles")
pylab.xlabel("position")
pylab.ylabel("bin frequency")
pylab.legend(loc="upper right", shadow=True, fontsize = "medium")
pylab.savefig('A1_given.png')
pylab.show()
