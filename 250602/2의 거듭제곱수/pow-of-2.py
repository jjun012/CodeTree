n=int(input())
x=1
num=2
while True:
    if num==n:
        break
    else:
        for i in range(x):
            num*=2
        x+=1
print(x)
    