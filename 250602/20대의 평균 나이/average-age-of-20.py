age=[]
cnt=0
while True:
    n=int(input())
    if n<20 or n>29:
        break
    age.append(n)
    cnt+=1
avg=sum(age)/cnt
print("%0.2f"%avg)