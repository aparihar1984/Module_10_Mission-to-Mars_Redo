#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Section 10.3.3
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup

import pandas as pd


# In[2]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)


# In[3]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[5]:


slide_elem.find("div", class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[8]:


# Section 10.3.4


# ### Featured Images

# In[9]:


# Visit URL 
# url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# browser.visit(url)


# In[10]:


# Find and click the full image button -- NOTE: webpage down thus this code didn't work on 10/31/2021
# full_image_elem = browser.find_by_id('full_image')
# full_image_elem.click()


# In[11]:


# Find the more info button and click that -- NOTE: webpage down thus this code didn't work on 10/31/2021
# browser.is_element_present_by_text('more info', wait_time=1)
# more_info_elem = browser.links.find_by_partial_text('more info')
# more_info_elem.click()


# In[12]:


# Parse the resulting html with soup -- NOTE: webpage down thus this code didn't work on 10/31/2021
# html = browser.html
# img_soup = soup(html, 'html.parser')


# In[13]:


# Find the relative image url -- NOTE: webpage down thus this code didn't work on 10/31/2021
# img_url_rel = img_soup.select_one('figure.lede a img').get("src")
# img_url_rel


# In[14]:


# Use the base URL to create an absolute URL -- NOTE: webpage down thus this code didn't work on 10/31/2021
# img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
# img_url


# In[15]:


# Section 10.3.5


# In[16]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[ ]:


df.to_html()


# In[ ]:


browser.quit()


# In[ ]:




