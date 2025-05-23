n=int(input())
sum=0
cnt=0
for i in range(n):
    a=int(input())
    sum+=a
    cnt+=1
avg=sum/cnt
print(sum,f"{avg:0.1f}")