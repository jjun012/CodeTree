a,b=map(int,input().split())
if a>b:
    n=a-b+1
    for i in range(n):
        print(n,end=' ')
        n-=1
else:
    n=b-a+1
    for i in range(n):
        print(n,end=' ')
        n-=1