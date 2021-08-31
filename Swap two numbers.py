a1 = int(input("Enter no. 1: "))
b1 = int(input("Enter no. 2: "))
c=a1
a1=b1
b1=c
print("Using 3rd variable")
print("1st no.: ",a1)
print("2nd no: ",b1)

a2 = int(input("Enter no. 1: "))
b2 = int(input("Enter no. 2: "))
print("Without using 3rd variable")
a2=a2+b2
b2=a2-b2
a2=a2-b2
print("1st no.: ",a2)
print("2nd no: ",b2)

