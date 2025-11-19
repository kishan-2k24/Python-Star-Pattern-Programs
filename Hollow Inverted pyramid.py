# Hollow inverted pyramid
n = 6
for i in range(n, 0, -1):
    if i==n:
        print("* " * (2 * n - 1))
    elif i==1:
        print(" " * (n - 1) + "*")
    else:
        inner=" " * (2 * i - 3)
        print(" " * (n - i) + "*" + inner + "*")
