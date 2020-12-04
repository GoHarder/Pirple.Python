class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0


class Car(Vehicle):
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year, weight)
        self.isDriving = False

    def drive(self):
        self.isDriving = True
        self.tripsSinceMaintenance += 1
        self.needsMaintenance = self.tripsSinceMaintenance > 100

    def stop(self):
        self.isDriving = False

    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False


mustang = Car('Ford', 'Mustang', 2016, '1 ton')
corvette = Car('Chevrolet', 'Corvette', 2020, '1 ton')
challenger = Car('Dodge', 'Challenger', 2019, '1 ton')

for i in range(50):
    challenger.drive()
    challenger.stop()

for i in range(101):
    mustang.drive()
    mustang.stop()
    corvette.drive()
    corvette.stop()

corvette.repair()

cars = [mustang, corvette, challenger]

for car in cars:
    values = [
        car.make,
        car.model,
        car.year,
        car.weight,
        car.needsMaintenance,
        car.tripsSinceMaintenance
    ]
    for value in values:
        print(value)
    print('')
