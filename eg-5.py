num=int(input())
ec=0
oc=0
while num:
    r=num%10
    num=num//10
    if r%2==0:
       ec=ec*10+r
    else:
       oc=oc*10+r
print(ec)
print(oc)
    
       
