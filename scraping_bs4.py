# Scraping websites using BeautifulSoup

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import urllib3

url = "https://www.datasciencedegreeprograms.net/rankings/masters/"

http = urllib3.PoolManager()

response = http.request('GET', url)

soup = BeautifulSoup(response.data, "lxml")
print(soup.prettify())
soup.h3

all_title = soup.findAll("h3")

uni = []

for title in all_title:
    print(title.text)
    uni.append(title.text)


uni

df = pd.DataFrame()

df['Universities'] = uni

df.head()

all_program = soup.findAll("h4")

all_program
programs = []

for prog in all_program:
    programs.append(prog.text)

programs

df = df.drop([0,1,32,33,34,35])

df.head()


df['Programs'] = programs

df.head()

all_desc = soup.findAll("p")

description = []

for desc in all_desc:
    description.append(desc.text)

description

desc_pd = pd.DataFrame(description)

print(desc_pd)
desc_pd = desc_pd.drop(desc_pd.index[0:13])

desc_pd = desc_pd.drop([72,73])

desc_pd


for i in range(14,71,2):
    desc_pd = desc_pd.drop(i)

desc_pd.index = np.arange(1, len(desc_pd) +1)
df.index = np.arange(1, len(df) +1)
desc_pd.head()
df.head()

pd.merge(df,desc_pd,)
