n=int(input())
largest = 0
smallest = 9
 
while (n):
        r = n % 10
        n=n//10
        if r>largest:
            largest=r
        elif r<smallest:
            smallest=r
 
print(largest)
print(smallest)
 
