import os, random, math, cmath
import matplotlib.pyplot as plt

#max density always equaled to pi/4 for square lattice
eta = .72
N_sqrt = 8
N = N_sqrt ** 2
sigma = math.sqrt (eta / (N*math.pi))
delxy = 1.0 / (2 * N_sqrt)
two_delxy = 2 * delxy
delta = 0.3 * sigma
n_steps = 10000
psi_same_density = []
psi_distribution = []
eta_distribution = []

print 1.0/N, sigma

def show_conf(L, sigma, title, fname):
    plt.axes()
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = plt.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                plt.gca().add_patch(cir)
    plt.axis('scaled')
    plt.title(title)
    plt.axis([0.0, 1.0, 0.0, 1.0])
    plt.savefig(fname)
    plt.show()
    plt.close()

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

def delx_dely(x, y):
    d_x = (x[0] - y[0]) % 1.0
    if d_x > 0.5: d_x -= 1.0
    d_y = (x[1] - y[1]) % 1.0
    if d_y > 0.5: d_y -= 1.0
    return d_x, d_y

def Psi_6(L, sigma):
    sum_vector = 0j
    for i in range(N):
        vector  = 0j
        n_neighbor = 0
        for j in range(N):
            if dist(L[i], L[j]) < 2.8 * sigma and i != j:
                n_neighbor += 1
                dx, dy = delx_dely(L[j], L[i])
                angle = cmath.phase(complex(dx, dy))
                vector += cmath.exp(6.0j * angle)
        if n_neighbor > 0:
            vector /= n_neighbor
        sum_vector += vector
    return sum_vector / float(N)

def average_Psi(L):
    total = 0
    T = len(L)
    for i in range(T):
        total += L[i] ** 2
    return math.sqrt(total) / float(T)

filename = 'disk_configuration_N%i_eta%.2f.txt' % (N, eta)
output_picture_file = 'disk_configuration_N%i_eta%.2f.png' % (N, eta)
figure_title = 'disk configuration N = %i and eta = %.2f' % (N,eta)


if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    L = []
    L = [[ delxy + i * two_delxy, delxy + j * two_delxy ] for i in range(N_sqrt) for j in range(N_sqrt)]
    print 'starting from a new square lattice configuration'
    show_conf(L, sigma, figure_title, output_picture_file)
#    print "L is \n", L

while eta > 0.2:
    for steps in range(n_steps):
        if n_steps % 100 == 0:
            psi_same_density.append(abs(Psi_6(L, sigma)))
   #         print eta, psi_same_density
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        b[0] = b[0] % 1.0
        b[1] = b[1] % 1.0
        #minimum distance between disks
        min_dist = min(dist(b,c) for c in L if c != a)
        if not min_dist < 2 * sigma:
            L[L.index(a)] = b
    psi_distribution.append(average_Psi(psi_same_density))
    eta_distribution.append(eta)
    psi_same_density = []
    eta -= 0.02
    sigma = math.sqrt (eta / (N*math.pi))
    print "eta = ", eta

f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()

show_conf(L, sigma, figure_title, output_picture_file)

#zip(*psi_distribution)
#plt.scatter(*zip(*psi_distribution))
plt.plot(eta_distribution, psi_distribution)
plt.title('Order parameter vs Density')
plt.xlabel('density (eta)')
plt.ylabel('Order paramter (Psi)')
plt.savefig('orderparam_vs_density.png')
plt.show()

print eta_distribution, psi_distribution
