x = input("Podaj współrzędną x: ")
y = input("Podaj współrzędna y: ")

cords = (int(x),int(y))

print(cords)
distanceSquared = cords[0]**2 + cords[1]**2

distance = distanceSquared**0.5

print(distance)


