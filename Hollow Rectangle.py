# hollow rectangle with given rows n and cols = 2*n
n = 5
rows = n
cols = 2 * n
for r in range(1, rows + 1):
    if r == 1 or r == rows:
        print("* " * cols)
    else:
        print("*" + " " * (2 * cols - 3) + "*")