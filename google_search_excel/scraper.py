from selenium import webdriver
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import time
driver = webdriver.Firefox()
wb = load_workbook(filename = '/home/shahzad/Documents/personal_work/restaurants/taxila.xlsx')
sheet = wb['Sheet1']
i=270
while i <= 662:
    i+=1
    key1 = "B{0}".format(i)
    key2 = "C{0}".format(i)
    url = "https://www.google.com/search?client=ubuntu&channel=fs&ei=mNJ7Xd_6LsfNwQLK4I7gCg&q={0} {1}".format(sheet[key1].value,sheet[key2].value)
    try:
        driver.get(url)
        soup =BeautifulSoup(driver.page_source, 'html.parser')
        menu = phone = reservation = ''
        if(len(soup.find_all('div', class_='i4J0ge'))>0):
            if(soup.find_all('div', class_='i4J0ge')[0].find("div",{"data-attrid":"kc:/local:menu"})):
                menu = soup.find_all('div', class_='i4J0ge')[0].find("div",{"data-attrid":"kc:/local:menu"}).find("a", href=True)["href"]
            if(soup.find_all('div', class_='i4J0ge')[0].find("div",{"data-attrid":"kc:/local:table_reservations"})):
                reservation = soup.find_all('div', class_='i4J0ge')[0].find("div",{"data-attrid":"kc:/local:table_reservations"}).find("a", href=True)["href"]
            if(soup.find_all('div', class_='i4J0ge')[0].find("span",{"data-local-attribute":"d3ph"})):
                phone = soup.find_all('div', class_='i4J0ge')[0].find("span",{"data-local-attribute":"d3ph"}).find('span').text
            
            key3 = "D{0}".format(i)
            key4 = "E{0}".format(i)
            key5 = "F{0}".format(i)
            
            sheet[key3].value = phone
            sheet[key4].value = menu
            sheet[key5].value = reservation
            time.sleep(3)
    except Exception:
        pass

wb.save(filename = '/home/shahzad/Documents/personal_work/restaurants/taxila.xlsx')

search = soup.find('div', {'id':'search'}).find("div", {'class':'srg'})
links = search.find_all("a", href=True)
for link in links:
    if("facebook.com" in link["href"]):
        link["href"]