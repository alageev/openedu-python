# Считать с клавиатуры полный адрес англоязычной html страницы.
# С использованием urlparse получить из адреса кортеж значений.
# Вывести текст всех заголовков уровня h1 одной строкой через пробел без дополнительных символов вначале и конце строки.
# Примечание. Если внутри тегов h1 содержатся ссылки, то нужно выводить вместе со ссылками.

from urllib.parse import urlparse
import re
import urllib.request

url = input()
print(tuple(urlparse(url)))

with urllib.request.urlopen(url) as response:
    html = response.read()

batRegex = re.compile(r'<h1>(.+?)</h1>')

ml = batRegex.search(html.decode('utf8'))

print(' '.join(batRegex.findall(html.decode('utf8'))))
