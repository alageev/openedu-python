#Ввести с клавиатуры строку латиницей (1-3 слова). Зашифровать ее с использованием гарантированных алгоритмов шифрования. Сформировать словарь, где в качестве ключа используется название гарантированного алгоритма шифрования, а в качестве значения - результат шифрования в шестнадцатеричном представлении { 'sha1': 'd0b…', 'md5', '1f3…',…}.
# Итог вывести отдельными операторами вывода в виде пар ключа и значения, отсортированных по возрастанию ключа:
# md5 1f3…
# sha1 d0b…

import hashlib

string = input().encode()

dictionary = dict()
dictionary['md5']    = hashlib.md5(string).hexdigest()
dictionary['sha1']   = hashlib.sha1(string).hexdigest()
dictionary['sha224'] = hashlib.sha224(string).hexdigest()
dictionary['sha256'] = hashlib.sha256(string).hexdigest()
dictionary['sha384'] = hashlib.sha384(string).hexdigest()
dictionary['sha512'] = hashlib.sha512(string).hexdigest()

print('md5 ' + str(dictionary['md5']))
print('sha1 ' + str(dictionary['sha1']))
print('sha224 ' + str(dictionary['sha224']))
print('sha256 ' + str(dictionary['sha256']))
print('sha384 ' + str(dictionary['sha384']))
print('sha512 ' + str(dictionary['sha512']))
