# Создайте класс, осуществляющий подсчет и изменение числа книг. Названия книг, их количество считываются одной строкой вида 'Boogeyman 66 Battleground 50', число книг - произвольное.
# В классе должен быть реализован конструктор, деструктор, методы просмотра числа, взятия и возвращения книг.
# Реализовать вывод начальных значений, взятие по 1 книге, возвращение по 1 книге с выводом текущего числа после вызова каждого из методов, меняющих значение книг.
# Типичный ответ одной строкой: 'Boogeyman 66 65 66 Battleground 50 49 50'.

class Library:
    def __init__(self):
        self.bookList = list()

    def __del__(self):
        pass
    
    def addBook(self, name, number):
        self.bookList.append(name)
        self.bookList.append([int(number)])
    
    def takeBook(self, name):
        index = self.bookList.index(name)
        self.bookList[index + 1].append(self.bookList[index + 1][-1] - 1)
        return self.countBooks(name)

    def returnBook(self, name):
        index = self.bookList.index(name)
        self.bookList[index + 1].append(self.bookList[index + 1][-1] + 1)
        return self.countBooks(name)

    def countBooks(self, name):
        index = self.bookList.index(name)
        return self.bookList[index + 1][-1]

string = input().split(' ')

library = Library()

for i in range(len(string) // 2):
    library.addBook(string[2 * i], string[2 * i + 1])

for i in range(len(library.bookList)):
    if i % 2 == 0:
        name = library.bookList[i]
        library.takeBook(name)
        library.returnBook(name)


returnString = ''
for i in range(len(library.bookList)):
    if i % 2 == 0:
        returnString += ' ' + library.bookList[i] + ' '
    else:
        returnString += ' '.join([str(item) for item in library.bookList[i]])

print(returnString[1:])
