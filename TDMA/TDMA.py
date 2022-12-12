def tdma(a, b, c, d):
    n = len(d)
    w = [0 for i in range(n)]
    g = [0 for i in range(n)]
    x = [0 for i in range(n)]

    w[0] = c[0] / b[0]
    g[0] = d[0] / b[0]

    for i in range(1, n):
        w[i] = c[i] / (b[i] - a[i] * w[i-1])
        g[i] = (d[i] - a[i] * g[i-1]) / (b[i] - a[i] * w[i-1])

    x[n-1] = g[n-1]

    for i in reversed(range(n-1)):
        x[i] = g[i] - w[i] * x[i+1]

    return x
