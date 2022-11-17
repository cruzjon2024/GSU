from base64 import decode
import pandas as pd 
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image #Converting images into arrays 
import matplotlib.patches as mpatches
from sklearn.preprocessing import label_binarize #import Visualization Library - For Waffle Chart 
mpl.style.use('ggplot')
from wordcloud import WordCloud ,STOPWORDS
import urllib


#Example1 the word cloud of the first 2000 words of "Alice's Adventures in Wonderland "

# alice_novel = urllib.request.urlopen('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/alice_novel.txt').read().decode('utf-8')

# STOPWORDS=set(STOPWORDS) #words not necessary 

# alice_wc= WordCloud(
#         background_color='white',
#         max_words=2000,
#         stopwords=STOPWORDS
# )

# alice_wc.generate(alice_novel)

# #Display Word Cloud 
# plt.imshow(alice_wc)
# plt.axis('off')
# plt.show()

#Example 2 after Modifictaions 
#modify STOP WORDS 
# alice_novel = urllib.request.urlopen('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/alice_novel.txt').read().decode('utf-8')

# STOPWORDS=set(STOPWORDS) #words not necessary 

# alice_wc= WordCloud(
#         background_color='white',
#         max_words=2000,
#         stopwords=STOPWORDS
# )

# STOPWORDS.add('said')

# alice_wc.generate(alice_novel)

# fig=plt.figure(figsize=(14,18))

# plt.imshow(alice_wc)
# plt.axis('off')

# plt.show()


#example 3 with Mask Words with cloud 
alice_novel = urllib.request.urlopen('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/alice_novel.txt').read().decode('utf-8')

STOPWORDS=set(STOPWORDS) #words not necessary 

alice_mask= np.array(Image.open(urllib.request.urlopen('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%204/images/alice_mask.png')))

# initiate word cloud object 
alice_wc= WordCloud(
        background_color='white',
        max_words=2000,
        stopwords=STOPWORDS,
        mask=alice_mask,
)

#modify STOP WORDS 
STOPWORDS.add('said')

alice_wc.generate(alice_novel)

fig=plt.figure(figsize=(12,12))

plt.imshow(alice_wc)
plt.axis('off')

plt.show()
