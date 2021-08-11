from urllib.request import urlopen
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup as bs

headers = {'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

#네이버 이미지 검색사이트
urladdress1 = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

#검색할 단어를 입력
urladdress2 = input('검색할 단어를 입력하세요 : ')

#단어에 대한 이미지를 몇개 갖고올 것인지 갯수 입력
crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))

#urladdress2를 한글검색 자동변환하여 urladdress1와 합침
urladdress3 = urladdress1 + quote_plus(urladdress2)

#
request = requests.get(urladdress3, headers = headers)
htmlcontent1 = request.text
#urlopen(urladdress3).read()


#
soup = bs(htmlcontent1, "html.parser")

print(soup)

tag = soup.select('#main_pack > section > div > div.photo_group._listGrid > div.photo_tile._grid > div')

for ta in tag:
    a_tag = ta.select_one('div > div.thumb > a > img')
    if a_tag is not None:
        print(a_tag)






#
data1 = soup.find_all(class_ = "_img")
#class_ = "_image _listImage"

print(data1)

n =1

for i in data1:
    print(n)

    img_source = i['src']

    with urlopen(img_source) as f:
        with open('C:/source/img/' + urladdress2 + str(n) + '.jpg','wb')as b:
            data1 = f.read()

            b.write(data1)

    n += 1

    if n > crawl_num:
        break

print('end')
