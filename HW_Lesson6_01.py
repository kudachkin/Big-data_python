import time

class TrafficLight:

    def __init__(self, color):
        self.__color = color


    def running(self):
        print(f'Загорается {self.__color} цвет')


green = TrafficLight('Зеленый')
yellow = TrafficLight('Желтый')
red = TrafficLight('Красный')

red.running()
time.sleep(7)
yellow.running()
time.sleep(2)
green.running()