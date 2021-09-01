n=int(input("Enter number: "))
total=0
while(n!=0):
    r=n%10
    n=n//10
    total=total+r
print("Sum of digits is: ",total)
