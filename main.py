import numpy as np
import math


def p_pollard(N):
    x = np.random.randint(1, N - 2)
    y = 1
    i = 0
    stage = 2
    while (math.gcd(N, abs(x - y)) == 1):
        if i == stage:
            y = x
            stage = stage * 2
        x = (np.power(x, 2) + 1) % N
        i += 1
    return math.gcd(N, abs(x - y))

def factorization(N):
    p = p_pollard(N)
    q = int(N / p)
    return p, q

if __name__ == '__main__':
    N = 1684413987
    p, q = factorization(N)
    print("p = ", p, "q = ", q)

