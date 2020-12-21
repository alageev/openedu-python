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
