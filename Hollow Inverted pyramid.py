# Hollow inverted pyramid
n = 5
for i in range(n):
    print(' '* i, end='')
    if i == 0 or i == n - 1:
        print('* ' * (n - i))
    else:
        print('* ' + '  ' * (n - i - 2) + '*')
