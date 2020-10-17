# Считать несколько имен людей одной строкой, записанных латиницей, через пробел, например:
# «Anna Maria Peter».
# Вывести их одной строкой в порядке возрастания «Anna Maria Peter».
# Вывести их одной строкой в порядке убывания «Peter Maria Anna».
strings = input()

print(' '.join(sorted(strings.split(' '))))
print(' '.join(sorted(strings.split(' '), reverse = True)))
