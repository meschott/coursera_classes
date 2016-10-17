import random, math
import matplotlib.pyplot as plt

def markov_chain_step(N, sigma, delta, L):
    a = random.choice(L)
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    #minimum distance between disks
    min_dist = math.sqrt(min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a))
    box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
    if not (box_cond or min_dist < 2 * sigma):
        #replace the new coordinates for the one disk into the tracking array L.
        L[L.index(a)] = b
    return L
    
L = [[0.25, 0.25], [0.25, 0.75], [0.75, 0.25], [0.75, 0.75]]
sigma = 0.1197
sigma_sq = sigma ** 2
delta = 0.1
N = 4
n_steps = 10000000
histo_data = []

for steps in range(n_steps):
    new_position = markov_chain_step(N, sigma, delta, L)
    for k in range(N):
        histo_data.append(new_position[k][0])

plt.hist(histo_data, bins=100, normed=True)
plt.xlabel('x')
plt.ylabel('frequency')
plt.title('Markov chain: x coordinate histogram (density eta=0.18)')
plt.grid()
plt.savefig('markov_chain_x_sampling_histo.png')
plt.show()

