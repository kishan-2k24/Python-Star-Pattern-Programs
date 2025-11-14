n=8
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
for j in range(n - 1):
    print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')
