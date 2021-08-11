#키워드 검색을 자동화하여 필요한 이미지만 저장하기위해 설치
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#이미지를 저장하기 위해 일정 시간을 두기 위해 설치
import time

#해당 이미지를 담아 둘 폴더가 없을경우를 대비하여 적용
import os

#이미지를 순서대로 다운받기 위해서 설치
from urllib.request import urlretrieve

#인터넷에 검색할 키워드
keyword='강아지'

print('Loading...')

#크롬 웹 브라우저를 열기 위한 드라이버
driver = webdriver.Chrome('C:/source/test/chromedriver.exe')
driver.implicitly_wait(30)

#네이버 이미지를 갖고오기위해 url설정
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'.format(keyword)

#설정한 url를 드라이버에 삽입
driver.get(url)

#필요한 이미지를 추출하기 위해 html에서 body태그를 추출
body = driver.find_element_by_css_selector('body')

#1초에 한번씩 range()안에 있는 숫자만큼 페이지 다운 스크롤 실행
for i in range(3):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

#body태그에서 추출한 소스에서 이미지와 관련된 이미지태그만 다시 추출
imgs=driver.find_elements_by_css_selector('#main_pack > section > div > div.photo_group._listGrid > div.photo_tile._grid > div > div > div.thumb > a > img')
result = []


#추출된 이미지태그에서도 이미지경로가 있는 src속성을 찾아서 리스트형인 result에 추가
for img in imgs:
    if 'http' in img.get_attribute('src'):
        result.append(img.get_attribute('src'))
#print(result)


#해당경로에 폴더가 없을 경우 폴더를 생성시킴
if not os.path.isdir('C:/source/test/dog'):
    os.mkdir('C:/source/test/dog')
    print("Create new directory!")

#enumerate형으로 변환하여 순서대로 반복문 실행
for index, link in enumerate(result):
    
    #확장자 제작
    start = link.rfind('.')
    end = link.rfind('&')
    filetype = link[start:end]

    #파일에 자료를 입력
    urlretrieve(link,'C:/source/test/dog/dog{}{}'.format(index,filetype))
print('Download Complete!')

