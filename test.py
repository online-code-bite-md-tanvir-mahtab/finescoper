from lib2to3.pgen2 import driver
from seleniumwire.undetected_chromedriver import webdriver
import undetected_chromedriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

import pandas  as pd
import os
import datetime
print('hello world')




if __name__ == '__main__':
    web_site_endpoint = 'https://www.coupang.com/vp/products/5379602817?itemId=7987637268&vendorItemId=75276537973&sourceType=srp_product_ads&clickEventId=559c01d5-e30d-429a-b7d9-a83da4ec52af&korePlacement=15&koreSubPlacement=5&isAddedCart='
    option = Options()
    option.headless = True

    driver = webdriver.Chrome(options=option)

    driver.get(url=web_site_endpoint)



    html_page = driver.page_source

    driver.close()
    driver.quit()
    soup = BeautifulSoup(html_page,'html.parser')
    try:
        product_name = soup.find('h2',class_='prod-buy-header__title').text
    except:
        product_name = " "
    try:
        product_price = (soup.find('span',class_='total-price').text).split()[0].split('원')[0].split(',')
        product_price = int(''.join(product_price))
    except:
        product_price = 0
    try:
        product_review = (soup.find('span',class_='count').text).split(" ")[0]
    except:
        product_review = 0.0
    try:
        product_sell = ((soup.find('span',class_='reward-cash-txt').text).split(" ")[28])
    except:
        product_sell = 0
    time = datetime.datetime.now()
    time.strftime('%j:%m:%Y')
    df2 = pd.DataFrame({
        'name':[product_name],
        'price':[product_price],
        'sell':[product_sell],
        'time':[time],
    })
    # # df2.to_csv("product_track.csv",index=False)
    # print(df2['price'][0])
    # print(df2['time'][0])
    print(df2)

# os.remove('ABM 민자 수저세트.csv')


