import re
import json
import urllib.request as request

url = input()
with request.urlopen(url) as response:
    txt = response.read().decode()
pattern = re.compile(r"COURSES = {(.*)}")
a = re.findall(pattern=pattern, string=txt)[0]
courses = (json.loads("{" + a + '}'))
a = 0
for number in sorted(courses.keys()):
    r = number + ' ' + courses[number]['title'] + ' ' + courses[number]['url']
    print(r)
    a += 1
    if a > 2:
        break
