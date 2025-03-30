list=list(map(int,input().split()))
if list[0]==min(list):
    print(1,end=' ')
else:
    print(0,end=' ')

if list[0]==list[1]==list[2]:
    print(1)
else:
    print(0)
