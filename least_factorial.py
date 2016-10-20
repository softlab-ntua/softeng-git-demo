def least_factorial(n):
    k = 1
    m = 1
    while True:
        # The invariant here is that k == (m-1)!
        if k >= n: return k
        m = m + 1
        k = k * m
