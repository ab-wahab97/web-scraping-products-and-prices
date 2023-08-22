from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

html=requests.get(url).text


soup=BeautifulSoup(html,'lxml')

products=soup.find_all('div',class_="col-sm-4 col-lg-4 col-md-4")


pname=[]
pprice=[]
pdesc=[]
for i in products:


    name=i.find('a',class_='title').text
    price=i.find('h4',class_='pull-right price').text
    desc=i.find('p',class_='description')
    pname.append(name)
    pprice.append(price)
    pdesc.append(desc)



df=pd.DataFrame({'Product Name':pname,"Price":pprice,'Description':pdesc})


df.to_csv('Product details.csv')



