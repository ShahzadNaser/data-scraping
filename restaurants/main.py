from selenium import webdriver

from bs4 import BeautifulSoup

from openpyxl import load_workbook

import time

driver = webdriver.Firefox()
driver.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
wb = load_workbook(filename = '/home/shahzad/Documents/personal_work/restaurants/wahcantt.xlsx')
sheet = wb.active
i=1
index = 1
err = False
url = "https://www.google.com/search?newwindow=1&client=ubuntu&hs=9iz&channel=fs&tbm=lcl&sxsrf=ACYBGNQU3jTq9-qzY2sZ6BBhxrvU8mBE2g%3A1569694290917&ei=UqKPXZjQN4bawAKQsa_QBA&q=restaurants+in+wah+cantt+pakistan&oq=restaurants+in+wah+cantt+pakistan&gs_l=psy-ab.3..33i22i29i30k1l6.4409.91251.0.91499.14.13.0.0.0.0.441.1375.2-1j2j1.4.0....0...1c.1.64.psy-ab..10.3.1107...0j0i20i263k1j0i22i30k1.0.wXtfgNT8XZs#rlfi=hd:;si:;mv:[[33.8021345,72.7997712],[33.7350154,72.70552359999999]];tbs:lrf:!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9"
driver.get(url)
time.sleep(10)
while err==False and index<21:
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find('div', {'id':'search'})
        search_divs = search.find_all('div', {'class':'VkpGBb'})
        for div in search_divs:
            key1 = "A{0}".format(i)
            key2 = "B{0}".format(i)
            try:
                if(div.find("div",{"class":"dbg0pd"}).find("div")):
                    sheet[key1].value = div.find("div",{"class":"dbg0pd"}).find("div").text
            except Exception:
                pass
            try:
                if(div.find("span",{"class":"rllt__details lqhpac"}).find_all("div")[1].find("span")):
                    sheet[key2].value = div.find("span",{"class":"rllt__details lqhpac"}).find_all("div")[1].find("span").text
            except Exception:
                pass
            except Exception:
                pass
            i+=1
        wb.save(filename = '/home/shahzad/Documents/personal_work/restaurants/wahcantt.xlsx')
        url = driver.find_element_by_id("pnnext").get_attribute('href')
        time.sleep(5)
    except Exception as e:
        print(e)
        err=True
        pass

