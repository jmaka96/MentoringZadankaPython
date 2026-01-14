class Car:
    def __init__(self,marka,model,rok):
        self.marka = marka
        self.model = model
        self.rok = rok
    def describe(self):
        print("Dane samochodu. Marka: "+ self.marka + ". model: " + self.model + ". rok produkcji: " + str(self.rok))

car1 = Car("Toyota", "Yaris", 2020)
car1.describe()

car2 = Car("Ferrari", "Spider", 2025)
car2.describe()

car3 = Car("Ford", "Focus", 1996)
car3.describe()
