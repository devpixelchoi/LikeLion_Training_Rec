#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, warnings
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[2]:


warnings.filterwarnings(action='ignore')


# In[3]:


driver = webdriver.Chrome('chromedriver_90')
url = 'https://www.amazon.com/'
driver.get(url)


# In[4]:


sel_search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
sel_btn = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')


# In[5]:


sel_search.clear()
sel_search.send_keys("bose soundlink")
sel_btn.click()


# In[6]:


open_1 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[1]/div/span/div/div/div[2]/div[2]/div/div[1]/h2/a/span')
open_1.click()


# In[7]:


open_rev = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
open_rev.click()


# In[8]:


open_see_all = driver.find_element_by_xpath('//*[@id="cr-pagination-footer-0"]/a')
open_see_all.click()


# In[9]:


page = driver.page_source
soup = BeautifulSoup(page, 'lxml')


# In[22]:


all_names = []
all_stars = []
# all_rev_titles = []
all_dates = []
all_colors = []
all_reviews = []

all_comments = soup.findAll("div", class_='a-section celwidget')

for page in range(4042):
    next_page = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
    
    for one in all_comments:
        one_name = one.find("span", class_="a-profile-name").text
        all_names.append(one_name)
#       print(all_names)
        
        one_star = one.find("span", class_="a-icon-alt").text
        all_stars.append(one_star)
#       print(all_stars)  

        one_date = one.find("span", class_="a-size-base a-color-secondary review-date").text
        all_dates.append(one_date)
#       print(all_date)
        
        one_color = one.find("a", class_="a-size-mini a-link-normal a-color-secondary").text
        all_colors.append(one_color.strip())
#       print(all_colors)

        one_review = one.find('span', class_='a-size-base review-text review-text-content')
        all_reviews.append(one_review.text.strip())
#       print(all_reviews)


# In[23]:


total_review = {'Names : ':all_names, 'Stars : ': all_stars, 'Date : ':all_dates, 
                'Color : ': all_colors, 'Comments : ':all_reviews}
total_review = pd.DataFrame(total_review)
total_review


# In[24]:


total_review.to_csv("Amazon_review_collect.csv", index=False)

print(os.getcwd())
print(os.listdir(os.getcwd()))

