a,b=map(int,input().split())
if a>b:
    n=a-b+1
    for i in range(n):
        print(a,end=' ')
        a-=1
else:
    n=b-a+1
    for i in range(n):
        print(b,end=' ')
        b-=1