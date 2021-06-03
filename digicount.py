num=int(input())
dc=0
if num==0:
    dc=1
else:
    while num:
        r=num%10
        num=num//10
        dc+=1
print(dc)        
