# Pyramid with spaced stars
n=8
for i in range(1, n + 1):
    print(' ' * (n - i) + ('* ' * i).rstrip())
    
