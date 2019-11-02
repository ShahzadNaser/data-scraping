from selenium import webdriver

from bs4 import BeautifulSoup

from openpyxl import load_workbook

import time

driver = webdriver.Firefox()
driver.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
wb = load_workbook(filename = '/home/shahzad/Documents/personal_work/gyms/riverside.xlsx')
sheet = wb.active
i=1

err = False
url = "https://www.google.com/search?newwindow=1&client=ubuntu&channel=fs&biw=1301&bih=670&sxsrf=ACYBGNQ0Xxv89_vRvHjN673ffsGXOb_XuQ:1570454601367&q=gyms+in+Riverside,+California&npsic=0&rflfq=1&rlha=0&rllag=33938563,-117422369,7669&tbm=lcl&ved=2ahUKEwiWzZmln4rlAhVGZ1AKHQcPDeAQjGp6BAgKED0&tbs=lrf:!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:;mv:[[34.0011132,-117.3180253],[33.8761546,-117.509602]];tbs:lrf:!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
driver.get(url)
time.sleep(10)
while err==False:
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
        wb.save(filename = '/home/shahzad/Documents/personal_work/gyms/riverside.xlsx')
        url = driver.find_element_by_id("pnnext").get_attribute('href')
        time.sleep(5)
    except Exception as e:
        print(e)
        err=True
        pass

