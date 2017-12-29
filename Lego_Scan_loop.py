import selenium
import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests
import pandas



# driver = webdriver.Chrome()
driver = webdriver.Firefox()

#url = "https://shop.lego.com/en-IE/Star-Wars-Sets"


##Star Wars Sets
url1 = "https://shop.lego.com/en-IE/Star-Wars-Sets?all=2&callback=json&cc=ie&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=AE0F776D-FD75-4DB9-9DAD-AD4852EC41F3&q2=setTypesFacetCategory&rank=rank_vrs&showRetired=false&sp_q_exact_9=ie&userquery=*&x1=theme_id&x2=productType_id"


##New Sets
url2 ="https://shop.lego.com/en-US/New-Sets?all=1&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=newFlag&rank=RankUS&sp_q_exact_9=us&userquery=*&x1=featured_id"

##Dimensions
url3 ="https://shop.lego.com/en-US/DIMENSIONS-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=cat1360003&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"


##Mindstorms
url4 ="https://shop.lego.com/en-US/MINDSTORMS-Sets"

##Disney
url5 ="https://shop.lego.com/en-US/Disney-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=cat430002&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"

##Architecture
url6 ="https://shop.lego.com/en-US/Architecture-Set"

##DC Comics
url7 ="https://shop.lego.com/en-US/DC-Comics-Super-Heroes-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=cat160004&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"

##Elves
url8 ="https://shop.lego.com/en-US/Elves-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=cat1070002&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"

##City
url9 ="https://shop.lego.com/en-US/City-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=E2034D52-000A-43AB-A026-06F14E7A23C1&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"


##Classic
url10 = "https://shop.lego.com/en-US/Classic-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=cat1050003&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"


##Marvel
url11 = "https://shop.lego.com/en-US/Marvel-Super-Heroes-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=cat250004&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"


#Creator Expert
url12 = "https://shop.lego.com/en-US/Creator-Expert-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=cat1590002&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"


##Technic
url13 = "https://shop.lego.com/en-US/Technic-Sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=B723B97D-E82F-4294-AB93-24EE5D1C5531&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"


#3 in one Creator
url14="https://shop.lego.com/en-US/creator-3-in-1-sets?all=2&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=50442713-9503-4F44-B501-C1065943159B&q2=setTypesFacetCategory&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id&x2=productType_id"


##Lego Batman
url15="https://shop.lego.com/en-US/The-LEGO-Batman-Movie-Sets?all=1&callback=json&cc=us&count=18&do=json-db&i=1&jsonp=jsonCallback&lang=en&q=*&q1=cat1550001&rank=RankUS&showRetired=false&sp_q_exact_9=us&userquery=*&x1=theme_id"


urls = [url1, url2, url3, url4, url5, url6, url7, url8, url9 ,url10, url11, url12, url13, url14, url15]
i = 1

for url in urls:

    driver.get(url)

    r=requests.get(url)

    soup = BeautifulSoup(r.content)

    l = []

    for x in range(1, 200):
        ##slow
        time.sleep(5)
        ###Click on link

        print("Scaning item number: "+str(x))

        try:
            pageLink = ('//*[@id="maincontent"]/main/div/div/div/div/div[2]/div[2]/div/div['+str(x)+']/div[1]/a/img')

            pageClick = driver.find_element_by_xpath(pageLink).click()
        except:
            pass
        time.sleep(4)

        ###Gather item details
        ###Item list
        #for y in range(1, 11):

        ##slow
        time.sleep(5)

        ##Items
        d = {}

        # Test if there is a Title
        try:
            title = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/div[1]/div/div[2]/div[1]/h1').text
        except:
            title = " "
        #print("Title is a " + str(type(title)))
        title.lstrip("b'")

        d["Title"] = title
        ###Print Title Test
        print("Title")
        print("\n" + title)

        # Test if there is a Product details
        try:
            Prod_details = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/div[2]/div/p').text
        except:
            Prod_details = " "
        #Prod_details.lstrip("b'")
        d["Product Details"] = Prod_details.lstrip("b'")
        ###Print Title Test
        print("Product Details")
        print("\n" + Prod_details)


        # Test if there is a Price
        try:
            Price = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/div[1]/div/div[2]/div[1]/div[1]/div/span').text
        except:
            Price = " "
        #Price.lstrip("b'\nxe2\nx82\nxac")
        d["Price"] = Price
        ###Print Title Test
        print("Price")
        print("\n" + Price)

        # Test if there is a Item
        try:
            Item = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/div[2]/div/dl[1]/dd').text
        except:
            Item = " "
        #Item.lstrip("b'")
        d["Item"] = Item
        ###Print Title Test
        print("Item")
        print("\n" + Item)


        # Test if there is a Ages
        try:
            Ages = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/div[2]/div/dl[3]/dd').text
        except:
            Ages = " "
        #Ages.lstrip("b'")
        d["Ages"] = Ages.lstrip("b'")
        ###Print Title Test
        print("Ages")
        print("\n" + Ages)



        # Test if there is a Pieces
        try:
            Pieces = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div/div[2]/div/dl[4]/dd').text
        except:
            Pieces = " "
        #Pieces.lstrip("b'")
        d["Pieces"] = Pieces.lstrip("b'")
        ###Print Title Test
        print("Pieces")
        print("\n" + Pieces)

        ###Go back to page
        time.sleep(5)
        driver.get(url)


        ###Add to List
        ##Append List
        l.append(d)

        df = pandas.DataFrame(l)
        ##DF Sort
        # df.sort(ascending=False)
        InputFile = "Results/Results_"+str(i)+".csv"

        df.to_csv(InputFile)

    i = i + 1



    time.sleep(5)
driver.quit()