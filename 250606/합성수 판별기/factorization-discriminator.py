n=int(input())
sat=False
for i in range(2,n,1):
    if n%i==0:
        sat=True
if sat==True:
    print("C")
else:
    print("N")