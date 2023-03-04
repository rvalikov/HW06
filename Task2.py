# определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#
# После загрузки задания, вы можете проверить себя самостоятельно с помощью

list1 = input("ВВедите список")
n=int(input("Нижний диапозон"))
m=int(input("Верхний диапозон"))
list_a = list1.split(" ")
list_a1 = list(map(int, list_a))
list_index = []
print(list_a1)
for i in list_a1:
    if (i <= m and i >= n):
        print(i)
        index_a = list_a1.index(i)
        list_index.append(index_a)
print(list_index)

