class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print(f'Машина {self.name} поехала')


    def stop(self):
        print(f'Машина {self.name} остановилась')


    def turn_direction(self):
        print(f'Машина {self.name} повернула')


    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed}')

# ferrari = Car(450, 'blue', 'ferrari', 'no')
# ferrari.go()

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} превысил скорость на {self.speed - 60}!')
        else:
            print(f'Текущая скорость автомобиля {self.name} равна {self.speed}')

lada = TownCar(60, 'blue', 'лада', 'no')
nissan = TownCar(60, 'red', 'ниссан', 'no')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

ferrari = SportCar(300, 'red', 'феррари', 'no')
bugatti = SportCar(250, 'red', 'бугатти', 'no')

class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} превысил скорость на {self.speed - 60}!')
        else:
            print(f'Текущая скорость автомобиля {self.name} равна {self.speed}')

gazel = WorkCar(100, 'white', 'газель', 'no')
jeep = WorkCar(150, 'black', 'джип', 'no')

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = 'yes'

octavia = PoliceCar(180, 'white', 'октавия', 'yes')

lada.go()
lada.turn_direction()
lada.show_speed()

ferrari.go()
ferrari.turn_direction()
ferrari.show_speed()

gazel.go()
gazel.turn_direction()
gazel.show_speed()

octavia.go()
octavia.turn_direction()
octavia.show_speed()
octavia.is_police