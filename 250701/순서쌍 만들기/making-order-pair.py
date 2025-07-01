n=int(input())
x=n
y=n
for i in range(n):
    for j in range(n):
        print("(%d,%d)"%(x,y),end=' ')
        y-=1
    print()
    x-=1
    y=n