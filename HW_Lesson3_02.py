def print_user_info(name, surname, birth, city, email, phone):
    print(f'Информация о пользователе: Имя {[name]} - Фамилия {[surname]} - Год рождения {[birth]} - '
          f'Город рождения {[city]} - Электронный адрес {[email]} - Телефон {[phone]}')

name = input('Введите имя пользователя - ')
surname = input('Введите фамилию пользователя - ')
birth = input('Введите год рождения пользователя - ')
city = input('Введите город пользователя - ')
email = input('Введите email пользователя - ')
phone = input('Введите телефон пользователя - ')

print(print_user_info(name, surname, birth, city, email, phone))