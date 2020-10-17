# Считать одной строкой произвольное количество пар элементов "Название книги Число экземпляров", второй строкой название алгоритма хеширования md5
# Aibolit 66 Barmaley 67
# md5

# Создать 2 класса:
# 1-й преобразует строку вида 'Aibolit 66 Babmaley 67', где название книги уникально, в словарь.
# 2-й осуществляет хеширования названия книги алгоритмом md5.
# Вывести отдельными операторами вывода:
# - элементы словаря, отсортированные по возрастанию ключа, например:
# Aibolit 66
# Barmaley 67
# - результаты хеширования в виде пар названия алгоритма и результатов хеширования ключей, отсортированных по возрастанию, представленных в шестнадцатеричном виде, сведенных в одну строку через пробел вида
# md5 c47.... md5 5d....' (без пробелов в начале и конце строки).

import hashlib

class Library:
    def __init__(self):
        self.dictionary = dict()

    def __del__(self):
        pass
    
    def addBook(self, name, number):
        self.dictionary[name] = number

    def countBooks(self, name):
        return self.dictionary[name][-1]

class Cipher(Library):

    def __init__(self):
        self.strings = list()

    def __del__(self):
        pass

    def encipher(self, string):
        self.strings.append(hashlib.md5(string).hexdigest())

    def encipheredList(self):
        return sorted(self.strings)

strings = input().split(' ')
algorithm = input()

library = Library()
cipher = Cipher()

for i in range(len(strings) // 2):
    library.addBook(strings[2 * i], strings[2 * i + 1])
    cipher.encipher(strings[2 * i].encode())

sortedBooks = []

for book in library.dictionary:
    sortedBooks.append(book)

for book in sorted(sortedBooks):
    print(book + ' ' + library.dictionary[book])

strings = cipher.encipheredList()

returnString = ''

for string in cipher.encipheredList():
    returnString += ' md5 ' + string

print(returnString[1:])
