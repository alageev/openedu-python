# week 1 - regexp

import re

a = input().strip()

ex = re.compile(r"<p> adress [0-9]+: (.*?)</p>")

result = list(map(lambda x: tuple(x.strip().split()), ex.findall(a)))

print(", ".join(map(lambda x: " ".join(x), result)))
print(", ".join(map(lambda x: " str.".join(x), result)))


# week 2 - Регулярные выражения и BeautifulSoup

from urllib.parse import urlparse
import re
import urllib.request

urlr = input()
print(tuple(urlparse(urlr)))

with urllib.request.urlopen(urlr) as response:
    html = response.read()
    
exp = re.compile(r'<h1>(.+?)</h1>')
print(" ".join(exp.findall(html.decode())))


# week 3
import re
import urllib.request
import threading as thr

# <img class="image a11y-hidden" src="https://mc.yandex.ru/watch/723233"/>

urlr = input()

html = ''

with urllib.request.urlopen(urlr) as response:
    html = response.read().decode()

exp = re.compile(r"""<img .*src="(http.+?)".*/>""")

found = list(set(exp.findall(html)))


def imgsrc(ururu, n):
    try:
        with urllib.request.urlopen(ururu) as response:
            print("Potok {} zakonchil zagruzku {}".format(n, ururu))
    except:
        print("error")
            
            
for x, y in enumerate(found):
    print("{} izobrazhenie {}".format(x+1, y))
    thr.Thread(target=imgsrc, args=(y, x+1)).start()


# week 4

import re
import urllib.request
import threading as thr

# <img class="image a11y-hidden" src="https://mc.yandex.ru/watch/723233"/>

urlr = input()

html = ''

with urllib.request.urlopen(urlr) as response:
    html = response.read().decode()

exp = re.compile(r"""<img .*src="(http.+?)".*/>""")

found = list(set(exp.findall(html)))


def imgsrc(ururu, n):
    try:
        with urllib.request.urlopen(ururu) as response:
            print("Process {} downloaded {}".format(n, ururu))
    except:
        print("error download")
            
            
for x, y in enumerate(found):
    print("{} image {}".format(x+1, y))
    thr.Thread(target=imgsrc, args=(y, x+1)).start()


# week 5 - fail
import re
import urllib.request
import threading as thr

urlr, n = input().split()
n = int(n)

html = ''

with urllib.request.urlopen(urlr) as response:
    html = response.read().decode()

href = re.compile(r"""(Django 2.0)""")

found = list(href.findall(html))
print(len(found))
