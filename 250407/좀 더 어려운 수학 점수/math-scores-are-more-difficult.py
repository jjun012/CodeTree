a_m,a_e=map(int,input().split())
b_m,b_e=map(int,input().split())
if a_m!=b_m:
    if a_m>b_m:
        print("A")
    else:
        print('B')
else:
    if a_e>b_e:
        print('A')
    else:
        print('B')