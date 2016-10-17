import random, sys, math
import matplotlib.pyplot as plt
import numpy as np

d = int(sys.argv[1])
delta = 0.1
n_hits = 0
n_runs = 10
old_radius_square = 0
new_radius_square = 0
Q = 2
volume_squared_sum = 0
volume_sum = 0
print "computing volume of the unit spheres up to", d, " dimensions with errors"

for g in range (6):
    n_trials = 10 ** g
    for h in range(n_runs):
        for i in range(1,d):
            x = [0.0] * i
            for j in range(n_trials):
                k = random.randint(0, i-1)
                x_old_k = x[k]
                x_new_k = x_old_k + random.uniform(-delta, delta)
                new_radius_square = old_radius_square + x_new_k ** 2 - x_old_k ** 2
                if new_radius_square < 1.0:
                    x[k] = x_new_k
                    old_radius_square = new_radius_square
                    alpha = random.uniform(-1.0,1.0)
                    if new_radius_square + alpha**2 < 1.0: n_hits += 1
            Q = Q * 2 * n_hits/float(n_trials)
            n_hits = 0
            old_radius_square = 0
        volume_squared_sum += Q ** 2
        volume_sum += Q
        Q = 2
    print "error for V[",d,"] with", n_trials, "is", math.sqrt(volume_squared_sum/n_runs - (volume_sum/n_runs) ** 2)/math.sqrt(n_runs)
    print "<v_sph[",d,"]=", volume_sum/n_runs
    volume_squared_sum = 0
    volume_sum = 0


