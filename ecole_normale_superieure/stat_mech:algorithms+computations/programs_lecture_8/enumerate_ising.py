
#This function, gray flip, is able to create all the unique configurations for this 2-d ising model. This is the crux of tris algorithm
def gray_flip(t, N):
    k = t[0]
    if k > N: return t, k
    t[k - 1] = t[k]
    t[k] = k + 1
    if k != 1: t[0] = 1
    return t, k

L = 4
N = L * L

# Python dictionary where the key is the spin site, and the value is all it's nearest neighbors using periodic boundary conditions
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N)
                                    for i in range(N)}
print nbr

S = [-1] * N
E = -2 * N
print S, E
tau = range(1, N + 2)
for i in range(1, 2 ** N):
    tau, k = gray_flip(tau, N)
    print 'tau is ', tau, 'k is', k
    # The change in energy is merely the change in energy of the spin that is flip with its nearest neigbors
    h = sum(S[n] for n in nbr[k - 1])
    E += 2 * h * S[k - 1] 
    S[k - 1] *= -1
    print S, E
