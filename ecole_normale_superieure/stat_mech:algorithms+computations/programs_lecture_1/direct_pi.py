import random, math
n_trials = 400000
n_hits = 0
var = 0.0
obs_total = 0.0
obs_squared_total = 0.0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
        obs_total += 4.0
        obs_squared_total += 16.0
#    var += (Obs - math.pi)**2
var = obs_squared_total/n_trials - (obs_total/n_trials) ** 2
print 4.0 * n_hits / float(n_trials), math.sqrt(var / n_trials)
print "variance is ",var
print "so sigma is ", math.sqrt(var)
