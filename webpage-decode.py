## --- Problem URL: https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

from distutils.filelist import findall
import requests
from bs4 import BeautifulSoup
 
base_url = 'https://www.nytimes.com/'
r = requests.get(base_url)

soup = BeautifulSoup(r.text, 'lxml')

for story_heading in soup.find_all(class_="indicate-hover"):
    #print(story_heading)
    if story_heading.a: 
        print(story_heading.a.text)
    else: 
        print(story_heading.contents[0])

