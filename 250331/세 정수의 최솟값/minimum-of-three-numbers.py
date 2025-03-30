a,b,c=map(int,input().split())
min=0
if a<b and a<c:
    min=a
elif b<a and b<c:
    min=b
else:
    min=c
print(min)