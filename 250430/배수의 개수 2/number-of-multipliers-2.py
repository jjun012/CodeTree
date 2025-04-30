cnt=0
num=[]
for i in range(10):
    n=int(input())
    num.append(n)
for i in range(len(num)):
    if num[i]%2!=0:
        cnt+=1
print(cnt)