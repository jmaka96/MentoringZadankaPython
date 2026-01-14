def checkPassword(password):
    return len(password) >= 8

print(checkPassword("blablabla"))
print(checkPassword("test"))
print(checkPassword("12345678"))
