n=int(input())
cnt=0
num=1
while n>1:
    n//=num
    cnt+=1
    num+=1
print(cnt)