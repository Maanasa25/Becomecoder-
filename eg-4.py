num=int(input())
ecount=0
ocount=0
while num:
    r=num%10
    num=num//10
    if r%2==0:
        ecount+=1
    else:
        ocount+=1
if ecount%2==0 and ocount%2!=0:
    print("Even Odd")
elif ecount%2==0 and ocount%2==0:
    print("Even")
elif ocount%2!=0 and ecount%2!=0:
    print("Odd")
else:
    print("Mixed")
