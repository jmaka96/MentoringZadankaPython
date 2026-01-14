numbers = [3, 5, 10, 15, 20]

suma = 0

for x in numbers:
    suma += x
print("Suma wszystkich liczb w liście: "+ str(suma))

avg = suma/len(numbers)

print("Średnia wszystkich liczb w liście: " + str(avg))
