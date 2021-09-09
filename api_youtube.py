from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#
# fonction
#

UserInput = input("Enter a word or a sentence and it will give you the first result on youtube : ")
url = "https://www.youtube.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
browser.find_element_by_id('search').click()
browser.find_element_by_id('search').send_keys(UserInput)
browser.find_element_by_id('search-icon-legacy').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a').click()
time.sleep(7)
if browser.find_element_by_xpath('//*[@id="ad-text:7"]'):
    browser.find_element_by_xpath('//*[@id="ad-text:7"]').click()


