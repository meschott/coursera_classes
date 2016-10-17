import random, sys, math
import matplotlib.pyplot as plt
import numpy as np

d = int(sys.argv[1])
d = d - 1
x = [0.0] * d 
delta = 0.1
n_trials = 10000000
n_hits = 0
old_radius_square = 0
new_radius_square = 0
r = []
print "estimating volume in", d + 1, " dimensions over volume in", d, "dimensions"

for i in range(n_trials):
    k = random.randint(0, d-1)
    x_old_k = x[k]
    x_new_k = x_old_k + random.uniform(-delta, delta)
    new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
    if new_radius_square < 1.0:
        x[k] = x_new_k
        old_radius_square = new_radius_square
#        r.append(math.sqrt(new_radius_square))
    alpha = random.uniform(-1.0,1.0)
    if new_radius_square + alpha**2 < 1.0: n_hits += 1
print 2.0 * n_hits / float(n_trials)

#plt.hist(r, bins = 100, normed = True)
#n = np.arange(0, 1, 0.01)
#plt.plot(n, 20 * n ** 19)
#plt.xlabel("bins")
#plt.ylabel("frequency")
#plt.title("normalized radius frequency fitted with 20*(r ** 19)")
#plt.savefig("hw_b1.png")
#plt.show()
