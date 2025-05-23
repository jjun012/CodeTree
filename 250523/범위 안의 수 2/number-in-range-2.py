sum=0
cnt=0
for i in range(10):
    a=int(input())
    if a>=0 and a<=200:
        sum+=a
        cnt+=1
    
avg=sum/cnt
print(sum,f"{avg:0.1f}")