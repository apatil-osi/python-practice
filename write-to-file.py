## --- Problem URL: https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

import requests
from bs4 import BeautifulSoup
 
base_url = 'https://www.nytimes.com/'
r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'lxml')

for story_heading in soup.find_all(class_="indicate-hover"):
    with open('NYT-titles.txt', 'a+') as f:
        if story_heading.a: 
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write("\n")
            f.write(story_heading.a.text)
        else: 
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write("\n")
            f.write(story_heading.contents[0])
