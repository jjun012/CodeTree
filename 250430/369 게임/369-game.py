n=int(input())
i=1
while i<=n:
    if i%3==0:
        print(0,end=' ')
    elif '3'in str(i) or '6'in str(i) or '9' in str(i):
        print(0,end=' ')
    else:
        print(i,end=' ')
    i+=1
    