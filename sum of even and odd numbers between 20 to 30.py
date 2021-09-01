oddSum=0
evenSum=0
for i in range(20,30,2):
    if(i==20):
        continue
    if(i==30):
        break
    evenSum=evenSum+i
for i in range(20+1,30,2):
    oddSum=oddSum+i
print("Sum of odd numbers between 20 to 30 is: ",oddSum)
print("Sum of even numbers between 20 to 30 is: ",evenSum)

    
