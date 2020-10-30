# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:11:05 2020

@author: truet
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
import time


def username(username):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(f'https://reddit-user-analyser.netlify.app/#{username}')
    while True:
        reddits = [i.text.replace('\n',' - ') for i in driver.find_element_by_xpath('//h3[text()="Top subreddits"]/following-sibling::ul').find_elements_by_tag_name('li')]
        if len(reddits) != 0:
            break
        else:
            time.sleep(1)
    
    controversy_score = driver.find_element_by_xpath('//div[@class="core-summary d-flex flex-wrap justify-content-center"]/div[3]').get_attribute('data-value')
    
    user_subs = [reddit.split(' ')[0][3:] for reddit in reddits]
    driver.close()
    user_data = dict(username = username,
                     subs = user_subs,
                     score = controversy_score)
    
    return user_data



