# Считать отдельными операторами целочисленные ширину и высоту прямоугольника. Создать функцию (def), принимающую в качестве параметров ширину и высоту фигуры и название функции, которую необходимо выполнить. Имя вложенной функции передавать явным образом (например: (a,b,name='perim')).
# Внутри функции создать две вложенные функции (def) по подсчету площади и периметра фигуры. Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например, '20 18').

def function(a, b, name):
    def perimeter(a, b):
        return 2 * (a + b)

    def area(a, b):
        return a * b

    if name == 'perimeter':
        return perimeter(a, b)
    else:
        return area(a, b)

a = int(input())
b = int(input())

resultString = str(function(a, b, 'area')) + ' ' + str(function(a, b, 'perimeter'))
print(resultString)
