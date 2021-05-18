# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def data(name, surname, date, city, email, phone):
    print(f"Name: {name}, Surname: {surname}, Date of birth: {date}, City: {city}, E-mail: {email}, Phone: {phone}")


print(f"Enter your Name")
Name = (input())

print(f"Enter your Surame")
Surname = (input())

print(f"Enter your Date of birth")
Date = (input())

print(f"Enter your City")
City = (input())

print(f"Enter your E-mail")
Email = (input())

print(f"Enter your Phone")
Phone = (input())

data(date=Date, surname=Surname, city=City, phone=Phone, email=Email, name=Name) # произвольный порядок аргументов. кажется работает
