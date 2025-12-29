# from bs4 import BeautifulSoup
# import requests  

# url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# ############ send a custom User-Agent header to Wikipedia: 
# ############ headers overrides the default python-requests agent that Wikipedia rejects

# headers = {
#     "User-Agent": "Mozilla/5.0 (compatible; SilviaDataBot/1.0; +https://example.com/contact)"
# }
# page = requests.get(url, headers=headers)
# page.raise_for_status()

# ############

# soup = BeautifulSoup(page.text, "html.parser")        #getting the html content of the page 

# #print(soup)

# soup.find_all('table', class_='wikitable sortable')


from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

headers = {               #headers and user agent setting to get accepted by wikipedia
    "User-Agent": "Mozilla/5.0 (compatible; SilviaDataBot/1.0; +https://example.com/contact)"
}

try:
    resp = requests.get(url, headers=headers, timeout=50)
    resp.raise_for_status()
except RequestException as e:
    print("Request error:", e)
    soup = None
else:
    soup = BeautifulSoup(resp.text, "html.parser")

# if soup is not None:
#     tables = soup.find_all("table", class_="wikitable sortable")
#     print("Found tables:", len(tables))
#     companies_table = tables[1]            #finds table 2 onpage
#     print(companies_table)                 #prints table 2 


if soup is not None:
    table1 = soup.find_all("table", class_="wikitable sortable")[1]
    table_headings = table1.find_all("th")      #finds table 2 headings
    #print(table_headings)                     #[<th>Rank </th>, <th>Name</th>, <th>Industry </th>, <th>Revenue <br/>(USD millions)................</th>, <th>Industry </th>, <th>Profits<br/>(USD millions) </th>]
    world_table_titles = (title.text.strip() for title in table_headings)          #world_table_titles is a generator expression, need conversion to list in order to print it
    print(list(world_table_titles))

else:
    print("No soup available - request failed")


import pandas as pd
df = pd.DataFrame(columns = world_table_titles)