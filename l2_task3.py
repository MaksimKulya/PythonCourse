# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print(f"Enter the month name as a number 1-12")
N = int(input())

list_month=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
dict_month={0:"Jan",1:"Feb",2:"Mar",3:"Apr",4:"May",5:"June",6:"July",7:"Aug",8:"Sep",9:"Oct",10:"Nov",11:"Dec"}

print(f"List says: the {N}th month is {list_month[N-1]}")

print(f"Dict says: The {N}th month is {dict_month.get(N-1)}")