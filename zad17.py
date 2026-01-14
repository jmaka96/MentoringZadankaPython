car_count = 0

class Car:
    def __init__(self, marka, model, rok):
        global car_count
        self.marka = marka
        self.model = model
        self.rok = rok
        car_count += 1
    def describe(self):
        print("Dane samochodu. Marka: "+ self.marka + ". model: " + self.model + ". rok produkcji: " + str(self.rok))

    def print_count():
        global car_count
        print("liczba utworzonych samochodów: " + str(car_count))

car1 = Car("Toyota", "Yaris", 2020)
car1.describe()

car2 = Car("Ferrari", "Spider", 2025)
car2.describe()

car3 = Car("Ford", "Focus", 1996)
car3.describe()

Car.print_count()
