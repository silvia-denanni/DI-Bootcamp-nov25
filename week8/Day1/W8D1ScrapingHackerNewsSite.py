###################################SCRAPING HACKER NEWS WEBSITE###################################

import requests                       #allows us to download the HTML
from bs4 import BeautifulSoup         #allows us to use the HTML and grab different data to do what we need to do

#response = requests.get('https://news.ycombinator.com/news')
#print(response)         #>>> HTTP Status [200]

url = requests.get('https://news.ycombinator.com/news')
#print(site.text)         #>>> HTTP Status [200] + string containing all of the page HTML
soup = BeautifulSoup(url.text, 'html.parser')  #parsing the HTML 
#print(soup.body)                              #<body>....</body>
#print(soup.body.contents)                     #all body contents in list form
#print(soup.find_all('div'))                   #finds all divs in the page
#print(soup.find('a'))                         #finds the first link on the page
#print(soup.find('id=score_20514755'))         #finds the element in question
#print(soup.select('.score'))             #finds through the use of css selectors all of the SPAN CLASSES ('.') including 'score' elements on the page
#print(soup.select('#score_46406129'))    #finds through the use of css selectors ONLY of the SPAN CLASS ('#') with the SPECIFIC ID


links = soup.select('.title')        #finds through the use of css selectors the SPAN CLASS ('.') storylink 
votes = soup.select('.score')            #finds through the use of css selectors the SPAN CLASS ('.') score, 'votes' (.score) has fewer elements than 'links' above

def create_custom_hackernews (links, votes):    #getting only the text (e.g. title of the links) not the HTML
    hackernews_list = []
    for idx, item in enumerate(links):
        if idx >= len(votes):        # avoid going past the end (there are titles without score (e.g. job posts, ads) this is to avoid votes[idx] failing)
            break

        title = links[idx].getText()                         #grab index of each link ('links' returns a list)
        href = links[idx].get('href', None)                                    #'None' in case of broken link
        points = int(votes[idx].getText().replace(' points', ''))              #get just an integer
        hackernews_list.append({'title': title, 'link': href, 'points': points})    #append to the list the dictionary containing titles and links of the articles

    return hackernews_list

print(create_custom_hackernews(links,votes))