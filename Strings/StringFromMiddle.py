s=input()
n=len(s)
if n==0:
    print("empty")
else:
    if n%2==0:
        i=n//2-1
    else:
        i=n//2
    print(s[i-1]+s[i]+(s[i+1]))