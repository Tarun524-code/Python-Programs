try:
    n1 = int(input())
    n2 = int(input())
    c = n1//n2
    print(f"Division: {c}")
except ValueError:
    print("Both Input must be numbers")
except ZeroDivisionError:
    print("Division Not Possible")