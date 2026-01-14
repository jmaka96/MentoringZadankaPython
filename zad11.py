names = ["Kuba", "Konrad", "Marysia", "Ada", "Rafal", "Jurek", "Kuba", "Ania", "Kazimierz", "Konrad", "Ada", "Marysia", "Ada", "Ada", "Ania", "Ada"]

counts = {}
for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

print(counts)
