try:
    n1 = int(input())
    n2 = int(input())
    sum = n1+n2
    pro = n1*n2
    print(f"Sum :{sum} \n Product :{pro}")
    quo = n1//n2
    print(f"Quotient :{quo}")
except ZeroDivisionError:
    print("Bot Num must be Non Zero Numbers")
    c = n1//2
    print(c)
    