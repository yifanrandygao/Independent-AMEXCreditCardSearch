#########################################################################################
# Author: Yifan Gao                                                                     #
# This script runs web scraping technique on AMEX website with aim to acquire the       #
# highest reward points (85000, 10000 from self referral and 75000 from open account    #
# bonus) for AMEX Platinum credit card.                                                 #
# Prerequisites:                                                                        #
# 1. It is recommended to run Python 3.7 for this script. When running Python 3.6, I    #
# received an error with lxml parser so Python 3.6 does not work. I did not test other  #
# versions so they may work as well.                                                    #
# 2. Selenium needs browser driver to initialize web page so please download browser    #
# driver to your work directory. In this script, I use Chrome driver. Here is the url   #
# to download: https://chromedriver.storage.googleapis.com/index.html?path=2.45/        #
# 3. This script is written in Windows so it's recommended to run in Windows. It may    #
# work in MacOS or Linux.                                                               #
# 4. Install package selenium, BeautifulSoup4 and lxml before executing the script.     #
#########################################################################################
import selenium.webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import lxml

chrome_options = wd.ChromeOptions()
chrome_options.add_argument("--incognito")


# driver = wd.Chrome('C:/Users/ygao3/Documents/PycharmProjects/Web Driver/Chrome/chromedriver.exe',chrome_options=chrome_options)
## Set up counter to control # of loops
cnt=0

while True:
    # driver.implicitly_wait(8)
    ## Replace your own directory that stores chromedriver in the first argument.
    driver = wd.Chrome('F:/Seeds/WebDriver/Chrome/chromedriver.exe',
                       chrome_options=chrome_options)
    driver.set_window_size(1920, 1080)
    # driver = wd.Firefox(executable_path='F:/Seeds/WebDriver/Firefox/geckodriver.exe')
    ## Replace your own referal link here. Note when clicking the link it should display all personal cards, with
    ## the first one states "Your Referred Card"
    try:
        driver.get('https://amex.co/2ReG3cf')
        # driver.get('https://amex.co/2Qge8Fp')
    except:
        driver.quit()
    ## Set up a stop timer inder to wait the page to be fully loaded. 2 seconds is recommended here but if you feel your internet
    ## is faster/slower, please adjust downwards/upwards accordingly.
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[text()="All Personal Cards"]')))
    except:
        driver.quit()
    # time.sleep(4)
    ## Convert html page into a bs object with lxml parser.
    soup = BeautifulSoup(driver.page_source, 'lxml')
    ## Use string matching to break the loop if key word "Earn 75,000 Membership Rewards" found.
    ## 'Cnt > 100' controls another break option. By default, if the page loads more than 200 times the script will automatically
    ## stops. Adjust this accordingly with your need. I do not recomend changing this number over 1000.
    # greennode = soup.find_all(type='Click_MCLP_CardDetails_PreferredRewardsGreenChargeCard')[0].parent.parent.parent
    # if (greennode.find_all(string="Earn 25,000 Membership Rewards") != []) or (cnt > 1000):
    if (cnt > 0) and (cnt % 45 == 0):
        driver.quit()
        time.sleep(60)

    # if ('25,000' in greennode.get_text()) or (cnt > 10000):
    #     print(cnt)
    #     break
    # else:
    #     pass
    #     driver.quit()

    if (soup.find_all(string="Earn 20,000 Membership Rewards") != []) or (cnt > 10000):
    # if (soup.find_all(string="Earn 75,000 Membership Rewards") != []) or (cnt > 10000):
        break
    else:
        pass
        driver.quit()
        # driver.refresh()
    cnt += 1