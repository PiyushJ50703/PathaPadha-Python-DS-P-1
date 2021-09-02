s=input("Enter the string: ")
n=len(s)
print(n)
for i in range(0,n):
    if(n<2):
        print("Empty string")
        break
    if(i>1 and i<(n-2)):
        continue
    else:
        print(s[i],end='')
