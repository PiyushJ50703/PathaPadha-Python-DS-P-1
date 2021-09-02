s=input("Enter String: ")
n=len(s)
s1=s[n-3::]
s2="ing"
s3="ly"
if(n>=3):
    if(s1==s2):
        s=s+s3
    else:
        s=s+s2
print(s)
