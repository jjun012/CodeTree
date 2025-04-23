c,n=input().split()
n=int(n)
if c=='A':
    for i in range(n):
        print(i+1,end=' ')
        i+=1
else:
    for i in range(n):
        print(n,end=' ')
        n-=1