## --- Problem URL: https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

import bs4
import requests

if __name__ == "__main__":
    url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

    r = requests.get(url)

    soup = bs4.BeautifulSoup(r.text,'lxml')

    article = soup.find_all(class_="paywall")

    for words in article:
        print(words)