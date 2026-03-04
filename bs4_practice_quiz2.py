'''
Beautiful Soup Practice Quiz 2
==============================
'''

from bs4 import BeautifulSoup
html='''
<html>
    <head>
        <title>Lorem Ipsum</title>
    </head>
    <body>
        <div id=header>
            <h1 id=top>Lorem <span class=bold>Ipsum</span></h1>
            <img src=top-image.png>
        </div>
        <div id=body>
            <h2>Lorem</h2>
            <p class=bold>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            <p class=bold>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
            <h2>Ipsum</h2>
            <ol>
                <li><img class=bold src=ceasar.png></li>
                <li class=bold><em>Veni</em></li>
                <li class=bold><em>Vidi</em></li>
                <li class=bold><em>Vici</em></li>
            </ol>
        </div>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

########################################
tags = soup.select('div > li')
problem1 = len(tags)
print("problem1=",problem1)
# problem1= 0

########################################
tags = soup.select('div li')
problem1a = len(tags)
print("problem1a=",problem1a)
# problem1a= 4

########################################
tags = soup.select('img.bold')
problem1b = len(tags)
print("problem1b=",problem1b)
# problem1b= 1

########################################
tags = soup.select('li.bold')
problem1c = len(tags)
print("problem1c=",problem1c)
# problem1c= 3

########################################
tags = soup.select('li .bold')
problem1d = len(tags)
print("problem1d=",problem1d)
# problem1d= 1

########################################
tags = soup.select('h2+p')
problem1e = len(tags)
print("problem1e=",problem1e)
# problem1e= 1

########################################
tags = soup.select('div>h2+p,h2')
problem1f = len(tags)
print("problem1f=",problem1f)
# problem1f= 3

########################################
tags = soup.select('ol')
accumulator = []
for tag in tags:
    accumulator += tag.select('img')
problem2 = len(accumulator)
print("problem2=",problem2)
# problem2= 1

########################################
# in our project, we will need to do CSS selectors and combine
# them with python code / for loops
# this will allow us to do more complex variations of CSS selectors and python code
tags = soup.select('div')
accumulator = []
for tag in tags:
    accumulator += tag.select('img')
problem2a = len(accumulator)
print("problem2a=",problem2a)
# problem2a= 2

########################################
tags = soup.select('body')
accumulator = []
for tag in tags:
    accumulator += tag.select('title')
problem2b = len(accumulator)
print("problem2b=",problem2b)
# problem2b= 0

########################################
tags = soup.select('html')
accumulator = []
for tag in tags:
    accumulator += tag.select('title')
problem2c = len(accumulator)
print("problem2c=",problem2c)
# problem2c= 1

########################################
tags1 = soup.select('h1')
tags2 = soup.select('#top')
tags = tags1 + tags2
problem3 = len(tags)
print("problem3=",problem3)
# problem3= 2

########################################
tags1 = soup.select('p')
tags2 = soup.select('.bold')
tags = tags1 + tags2
problem3b = len(tags)
print("problem3b=",problem3b)
# problem3b= 9

########################################
tags1 = soup.select('div')
tags2 = soup.select('.bold')
tags = tags1 + tags2
problem3c = len(tags)
print("problem3c=",problem3c)
# problem3c= 9
