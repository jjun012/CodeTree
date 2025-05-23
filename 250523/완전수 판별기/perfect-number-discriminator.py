n=int(input())
sum=0
idx=1
while idx <n:
    if n%idx==0:
        sum+=idx
    idx+=1
if n==sum:
    print('P')
else:
    print('N')