# Внутри функции создать две вложенные функции (lambda) по подсчету площади и периметра фигуры. Вывести одной строкой через пробел площадь и периметр, разделенные пробелом (например '20 18').

def function(a, b, name):
    perimeter = lambda a, b: 2 * (a + b)
    area      = lambda a, b: a * b
    
    if name == 'perimeter':
        return perimeter(a, b)
    else:
        return area(a, b)

a = int(input())
b = int(input())

resultString = str(function(a, b, 'area')) + ' ' + str(function(a, b, 'perimeter'))
print(resultString)
