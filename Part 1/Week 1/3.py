# Считать единой строкой без пробелов набор целых чисел (28745623873465386), удалить все дубликаты, вывести отдельными операторами вывода в порядке возрастания и в порядке убывания в виде кортежей целых чисел (2, 3, 4, 5, 6, 7, 8) и (8, 7, 6, 5, 4, 3, 2).

number = input()

numberList = list(number)

uniqueList = [int(item) for item in list(set(numberList))]

print(tuple(sorted(uniqueList)))
print(tuple(sorted(uniqueList, reverse = True)))
