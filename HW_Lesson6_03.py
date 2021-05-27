my_dict = dict(wage = 30000, bonus = 5000)

class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income

class Position(Worker):

    def get_full_name(self):
        print(f'Сотрудника зовут {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход сотрудника равен {self.income}')

worker_1 = Position('John', 'Doe', 'Analyst', my_dict.get('wage') + my_dict.get('bonus'))
worker_2 = Position('Ivan', 'Ivanov', 'Analyst', my_dict.get('wage') + my_dict.get('bonus'))

worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()