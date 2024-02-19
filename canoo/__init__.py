

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.canoo.com/about/"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

description_divs = soup.find_all('div', class_='description')


texts = []


for div in description_divs:

    text = div.get_text().strip()

    texts.append(text)


df = pd.DataFrame({'': texts})


df.to_csv('canoo_about_text.csv', index=False)





