s=input()
s1=input()
n = len(s)
n1 = len(s1)
if n%2==0:
    i=n//2-1
else:
    i=n//2
if n1%2==0:
    j=n1//2-1
else:
    j=n1//2
print((s[0]+s[i]+s[-1])+(s1[0]+s1[j]+s1[-1]))