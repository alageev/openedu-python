# Считать 1 строкой html вида:

#<!DOCTYPE html>
#<html>
#<head>
#<title></title>
#</head>
#<body>
#<h1> <font color="#00FF00">OpenEdu </font></h1>
#<font color="#FF0000">
#<p> adress 1: Kronverkskiy 49</p>
#<p> adress 2: Lomonosova 9</p>
#<p> adress 3: Birxhevaya 14</p>
#<p> adress 4: Grivzova 14 </p> </font>
#</body> </html>
#
#Найти и вывести одной строкой через запятую адреса:
#Kronverkskiy 49, Lomonosova 9, Birxhevaya 14, Grivzova 14
#
#Вставить после названий улиц 'str.' и вывести одной строкой через запятую адреса:
#Kronverkskiy str.49, Lomonosova str.9, Birxhevaya str.14, Grivzova str.14

import re

string = input()

batRegex = re.compile(r': (.+?)</p>')
searchResults = batRegex.findall(string)
for i in range(len(searchResults)):
    if searchResults[i][-1] == ' ':
        searchResults[i] = searchResults[i][:-1]
    if searchResults[i][0] == ' ':
        searchResults[i] = searchResults[i][0:]
print(', '.join(searchResults))


strings = []
newStrings = []

for string in searchResults:
    strings.append(string.split(' '))

for string in strings:
    string[1] = 'str.' + string[1]
    newStrings.append(string[0] + ' ' + string[1])
print(', '.join(newStrings))
