# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),

print(f"How much items do you want to buy")
N=int(input())

list=[]
for i in range(N):
    print(f"Item {i}:")
    item=input()

    print(f"Cost {i}:")
    cost=float(input())

    print(f"Number {i}:")
    number=float(input())

    dict = {"item": item, "cost": cost, "num": number}
    tupple=(i,dict)
    list.insert(i,tupple)

print(list)

# Show statistics
stat_item=[]
stat_cost=[]
stat_num=[]
for i in range(N):
    stat_item.append(list[i][1].get("item"))
    stat_cost.append(list[i][1].get("cost"))
    stat_num.append(list[i][1].get("num"))

print(f"Items: {stat_item}")
print(f"Cost: {stat_cost}")
print(f"Num: {stat_num}")