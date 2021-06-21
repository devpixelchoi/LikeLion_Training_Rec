#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from wordcloud import WordCloud
import numpy as np
from PIL import Image


# In[10]:


f = open("Amazon_review_collect_Analysis.csv", encoding='utf-8')
text = f.read()
f.close() 


# In[11]:


from matplotlib import rc
# rc('font', family='NanumGothic')


# In[26]:


wcloud = WordCloud('./data/D2Coding.ttf',
                   background_color='white',
                   stopwords = ["color","bought","I","it","to","the","is","that","this","a","you"],
                   relative_scaling = .8).generate(text)
                 
    
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
plt.imshow(wcloud, interpolation='bilinear')
plt.axis("off")

