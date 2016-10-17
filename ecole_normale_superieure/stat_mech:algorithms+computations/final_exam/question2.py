import random

L = 3
t_max = 1000
site = [0, 0]
for t in range(t_max):
    delta = random.choice([[1, 0], [0, 1], [-1, 0], [0, -1]])
    site[0] = (site[0] + delta[0]) % L
    site[1] = (site[1] + delta[1]) % L
print site
