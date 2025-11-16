n=5
size=2*n-1
for i in range(size):
    row =[" "]*size
    row[i]='*'
    row[size-i-1]='*'
    print("".join(row))