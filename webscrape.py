from bs4 import BeautifulSoup
import requests

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

html=requests.get(url).text


soup=BeautifulSoup(html,'lxml')

division=soup.find_all('div',class_="col-sm-4 col-lg-4 col-md-4")


for i in division:


    heading=i.find('a',class_='title').text
    price=i.find('h4',class_='pull-right price').text

    print(f'''
Name:  {heading}
Price: {price}

''')
