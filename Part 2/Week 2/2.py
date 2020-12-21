#Считать с клавиатуры полный адрес англоязычной html страницы.
#С использованием urlparse получить из адреса кортеж значений.
#Получить с помощью регулярных выражений и вывести текст всех заголовков уровня h1 одной строкой через пробел без дополнительных символов вначале и конце строки.
#Примечание. Если внутри тегов h1 содержатся ссылки, то нужно выводить вместе со ссылками.

import urllib
import urllib.request
import urllib.parse
from urllib.parse import urlparse
import os

inUrl = input()
urlStr = urlparse(inUrl)
findStr = "<h1>"
 
urlTuple = tuple(urlStr)
print (urlTuple)
def parseH1(inUrl,findStr):
    listTag = []
    inUrlFile = urllib.request.urlopen(inUrl)
    htmlFile = inUrlFile.read()
    htmlFileRez = htmlFile.decode('utf-8')
    f = open ('rez_tmp.html', 'w')
    for line in htmlFileRez:
        f.write(line)
    f = open ('rez_tmp.html', 'r')
    for line in f.readlines():
        if findStr in line:
            lineStr = line.strip()
            lineStr = lineStr[4:-5:]
            listTag.append(lineStr)
    f.close()
    os.remove('rez_tmp.html')
    finalStr = ' '.join(listTag)
    return finalStr
print (parseH1(inUrl,findStr))

