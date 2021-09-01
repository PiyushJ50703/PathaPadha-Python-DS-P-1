n=int(input("Enter no: "))
sum=0
num=n
while(num!=0):
    r=num%10
    num=num//10
    a=r**3
    sum=sum+a
if(sum==n):
    print(n," is a Armstrong number")
else:
    print(n," is not a armstrong number")
