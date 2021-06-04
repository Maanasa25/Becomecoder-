n=int(input())
temp=n
c=a=0
while n:
    r=n%10
    n=n//10
    c+=1
n=temp
while n:
    r=n%10
    n=n//10
    a=a+pow(r,c)
if a==temp:
    print('armstrong')
else:
    print('not armstrong')
