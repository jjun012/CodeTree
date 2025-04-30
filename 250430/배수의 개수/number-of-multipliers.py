cnt_1=0
cnt_2=0
num=[]
for i in range(10):
    n=int(input())
    num.append(n)
for i in range(10):
    if num[i]%3==0:
        cnt_1+=1
    if num[i]%5==0:
        cnt_2+=1
print(cnt_1,cnt_2)