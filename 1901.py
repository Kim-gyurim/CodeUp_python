n=int(input())

def f(n):
    if n!=1:
        f(n-1)
    print(n)
f(n)