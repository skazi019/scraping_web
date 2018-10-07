# Scraping websites for university Data

import numpy as np
import pandas as pd
import lxml.html as lh
import requests

url = "https://www.stoodnt.com/blog/fall-2019-application-deadlines-and-gre-requirements-for-ms-in-us/"

page = requests.get(url)
doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

[len(t) for t in tr_elements[:12]]

col = []
i=0
for t in tr_elements[0]:
    i += 1
    name = t.text_content()
    print('%d:"%s"'%(i,name))
    col.append((name,[]))

for j in range(1, len(tr_elements)):
    T = tr_elements[j]

    if len(T) != 5:
        break

    i = 0

    for t in T.iterchildren():
        data = t.text_content()
        if i > 0:
            try:
                data = int(data)
            except:
                pass

        col[i][1].append(data)
        i += 1

[len(c) for (title, c) in col]
dict = {title:column for (title,column) in col}
df = pd.DataFrame(dict)

df.head()

df.to_csv('stoodnt.com_fallapps2019.csv', index=False)
