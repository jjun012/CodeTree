n=int(input())
cnt=0
for i in range(1,101,1):
    cnt+=i
    if cnt>=n:
        print(i)
        break

