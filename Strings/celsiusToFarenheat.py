n = int(input("Enter number of temperatures: "))
celsius_list = []
for i in range(n):
    temp = float(input())
    celsius_list.append(temp)

fahrenheit_list = [(c * 9/5) + 32 for c in celsius_list]

print("Original Celsius list:", celsius_list)
print("Converted Fahrenheit list:", fahrenheit_list)

