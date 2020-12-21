#This solution doesn't work yet
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
