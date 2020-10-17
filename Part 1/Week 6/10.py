# Считать с клавиатуры отдельными операторами:
# - заголовок страницы (например, Hello);
# - цвет заголовка первого уровня (например, blue);
# - цвет текста абзаца (например, red);
# - текст заголовка первого уровня (например, Title 1);
# - текст статьи (например, Article text).

# Использовать только латинские символы.
# Используя декораторы, сформировать текст html-страницы для публикации статьи.
# Пример входных данных:
# Hello
# blue
# red
# Title 1
# Article text

# Пример выходных данных:
# <html>
# <head>
# <title>Hello</title>
# <style>h1{color:blue}p{color:red}</style>
# </head>
# <body>
# <h1>Title 1</h1>
# <p>Article text</p>
# </body>
# </html>

def html(function):
    def wrapper():
        print('<html>')
        function()
        print('</html>')
    return wrapper

def head(function):
    def wrapper():
        print('<head>')
        function()
        print('</head>')
    return wrapper

def title(firstLevelHeaderText):
    print('<title>'
    + firstLevelHeaderText
    + '</title>'
    )

def style(firstLevelHeaderColor, paragraphColor):
    print('<style>h1{color:'
        + firstLevelHeaderColor
        + '}p{color:'
        + paragraphColor
        +'}</style>'
        )

def body(function):
    def wrapper():
        print('<body>')
        function()
        print('</body>')
    return wrapper

def firstLevelHeader(firstLevelHeaderText):
        print('<h1>'
        + firstLevelHeaderText
        + '</h1>')

def paragraph(text):
    print('<p>'
    + text
    + '</p>'
    )

@head
def titleAndStyle():
    pageHeader = input()
    firstLevelHeaderColor = input()
    paragraphColor = input()
    title(pageHeader)
    style(firstLevelHeaderColor, paragraphColor)

@body
def firstLevelHeaderAndParagraph():
    firstLevelHeaderText = input()
    text = input()
    firstLevelHeader(firstLevelHeaderText)
    paragraph(text)

@html
def headAndBody():
    titleAndStyle()
    firstLevelHeaderAndParagraph()

headAndBody()
