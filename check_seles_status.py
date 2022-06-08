import time
from selenium import webdriver
import linemessage
import schedule


def selectclick(Xpath, driver):
    time.sleep(2)
    select = driver.find_element_by_xpath(Xpath)
    select.click()


def checkpagechange():
    #open webpage
    driver = webdriver.Chrome(executable_path = r"C:\Users\rsugi\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\chromedriver_binary\chromedriver.exe")

    #confirm URL
    try:
        driver.get(r'https://www.canyon.com/ja-jp/road-bikes/aero-bikes/aeroad/aeroad-cf-slx/aeroad-cf-slx-8-disc-di2/2771.html?dwvar_2771_pv_rahmenfarbe=BU%2FBU')
    except:
        linemessage.sendmessage('URL changed!')

    #acccept cookies
    selectclick('//*[@id="js-data-privacy-save-button"]', driver)

    #select color (must change)
    selectclick('//*[@id="js-productsummary"]/div[1]/div[4]/ul/li[2]/button', driver)

    #select size if it exists
    try:
        #size
        selectclick('//*[@id="js-productsummary"]/div[1]/div[4]/div[3]/ul/li[3]/button', driver)
        linemessage('Time has come!')
        #add to cart
        selectclick('//*[@id="js-productDetailBuyButtonSticky"]/button/span', driver)
        #show cart
        selectclick('//*[@id="app"]/div[3]/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/button[1]', driver)
        #go to buy
        selectclick('//*[@id="js-cartCheckoutStep"]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/a', driver)

    except:
        linemessage.sendmessage('Not yet')

    driver.quit()


#check page at 7:00 am and 12:00
schedule.every().day.at("07:10").do(checkpagechange)
schedule.every().day.at("15:00").do(checkpagechange)

while True:
    schedule.run_pending()
    time.sleep(1)
