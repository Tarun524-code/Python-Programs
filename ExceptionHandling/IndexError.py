l=list(map(int,input().split()))
try:
    print(sum(l))
    print(min(l))
    print(max(l))
    print(sum(l)//len(l))
    p=int(input("Enter Index: "))
    print(l[p])
except IndexError:
    print("Index is more than list size not possible to access ")
    