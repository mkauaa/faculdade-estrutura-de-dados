def fatorial(n):
    if n == 0:
        fat = 1
    else:
        fat = n * fatorial(n-1)
    return fat

print(fatorial(5))