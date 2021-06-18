def fib(n):
    # fib[n] = f[n]

    if f[n] == 0:
        if n == 0:
            f[n] = 0
            return f[n]
        if n == 1:
            f[n] = 1
            return f[n]
        f[n] = fib(n-2) + fib(n-1)
    return f[n]


n = 35
f = [0]*(n + 1)

print(fib(n))
print(f)
