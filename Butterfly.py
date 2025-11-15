# Butterfly
# upper
n=5
for i in range(1,n+1):  
    print("*"*i + " "*(2*(n-i)) + "*"*i)
# lower
for i in range(n,0,-1):  
    print("*"*i + " "*(2*(n-i)) + "*"*i)