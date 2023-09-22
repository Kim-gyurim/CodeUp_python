def f(k):
    if k == 1:
        return 1
    return k + f(k-1)

n = int(input())
a = f(n)

for i in range(n):
    for j in range(i+1):
        print(a, end=" ")
        a -= 1
    print()