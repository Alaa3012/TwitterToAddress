import csv
from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions


def create_webdriver_instance():
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge("C:/Users/User/Downloads/edgedriver_win64/msedgedriver.exe")
    return driver


def twitter_search(driver, url):
    driver.get(url)
    driver.maximize_window()
    sleep(1)
    if (driver.current_url == url):
        ercType = driver.find_element_by_xpath(
            '//div[@class="css-1dbjc4n"][7]/div[2]').text[80::]  # [0][1].get_attribute('href')
        NFTaddress = driver.find_element_by_xpath(
            '//div[@class="css-1dbjc4n"][7]/div[2]/div/a').get_attribute('href')[29::]
        NFTId = driver.find_element_by_xpath(
            '//div[@class="css-1dbjc4n"][7]/div[2]').text[40:44:]
        return [NFTaddress, NFTId, ercType]
    else:
        return ''


def get_nft_info(url):
    driver = create_webdriver_instance()
    nftData = twitter_search(driver, url)
    if (nftData == ''):
        return False
    else:
        contractAddress = nftData[0]
        NFTid = nftData[1]
        ercType = nftData[2]
        return [contractAddress, NFTid, ercType]


#print(get_nft_info("https://twitter.com/SugaSquadNFT/nft"))
