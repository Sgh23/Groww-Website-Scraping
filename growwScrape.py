from selenium import webdriver
from bs4 import BeautifulSoup
import time
url="https://groww.in/mutual-funds?q=&fundSize=&sortBy=3"
driver=webdriver.Chrome()
driver.get(url)
import time
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(9)
time.sleep(120)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(30)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(100)
element=driver.find_element_by_xpath("//*[@id='FundFilterPage']/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div")
dir(element)
element.click()
element.text
html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
results=soup.find_all("div",{'class':'f2CardContent'})
num=len(results)
print(num)
print(results[2].find("div",{'class':'fs16 clrBerbura fw500 f2LH34 truncate'}).get_text())
for result in results:
    print(result.get_text())
    

print(result.find("div",{'class':'fs16 clrBerbura fw500 f2LH34 truncate'}).get_text())
print(result.find("div",{'class':'fs12 clrAluminium ls2'}).get_text())
print(result.find("div",{'class':'valign-wrapper'}).get_text())

SchemeName=[]
Category=[]
Risk=[]
Ratings=[]
Return=[]
import pandas as pd
import numpy as np
#import csv
for result in results:
    sc=result.find("div",{'class':'fs16 clrBerbura fw500 f2LH34 truncate'}).get_text()
    SchemeName.append(sc) 
    cas = result.find_all('div', {'class':'fs12 clrAluminium ls2'})
    ca = cas[1].get_text()
    Category.append(ca) 
    ris=result.find("div",{'class':'fs12 clrAluminium ls2'}).get_text()   
    Risk.append(ris)
    rati=result.find("div",{'class':'fs12 clrAluminium ls2 valign-wrapper'}).get_text()
    Ratings.append(rati)
    ret=result.find("div",{'class':'f2YearReturn valign-wrapper'}).get_text()
    Return.append(ret)
    
 
    
data = []
for sn,cat,ri,ra,re in zip(SchemeName, Category, Risk, Ratings,Return):
    data.append({'SchemeName':sn,'Category':cat,'Risk':ri,'Ratings':ra,'Returns':re})
df=pd.DataFrame(data)
#     print(sn)
df
df.to_csv("Groww.csv")



groww=pd.read_csv("Groww.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)



groww.shape

#More Scraping
element1=driver.find_element_by_xpath("//*[@id='FundFilterPage']/div[2]/div/div[2]/div[2] ")
dir(element1)

results1=soup.find_all("div",{'class':'s11ResultSec'})
print(results1)


list_of_hrefs = []

content_blocks = driver.find_elements_by_class_name("s11ResultSec")

for block in content_blocks:
    elements = block.find_elements_by_tag_name("a")
    for el in elements:
        list_of_hrefs.append(el.get_attribute("href"))

print (list_of_hrefs)
    

len(list_of_hrefs)

import bs4
import requests
urls = list_of_hrefs
info=[]
for url in urls:
    ## getting the reponse from the page using get method of requests module
    page = requests.get(url)#, headers={"user-agent": user_agent.chrome})

    ## storing the content of the page in a variable
    html = page.content

    ## creating BeautifulSoup object
    soup = bs4.BeautifulSoup(html, "html.parser")
#     tab1=soup.find("div",{'class':'col l5'}).get_text()  col l12 divSections
    tab1 = soup.find_all('div', {'class':'col l12 divSections'}) #fnd1Section
    cab2 = tab1[2].get_text() #col l12 divSections
    info.append(cab2)

print(len(info))

#print(info)
 
print("end")
