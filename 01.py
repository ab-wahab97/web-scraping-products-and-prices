from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.rozee.pk/job/jsearch/q/python').text

print(html_text)

soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find('div',class_="job")
company=jobs.find('a',class_='display-inliner')


