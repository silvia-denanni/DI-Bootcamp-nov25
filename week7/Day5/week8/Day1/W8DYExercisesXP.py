#-------------------------------------------EXERCISE 1
# Read the HTML content of the page.
# Create a BeautifulSoup object to parse this HTML.
# Find the title of the webpage (the content inside the <title> tag).
# Extract all paragraphs (<p> tags) from the page.
# Retrieve all links (URLs in <a href=""> tags) on the page.


# import requests
# from bs4 import BeautifulSoup
# # -------------------------------------------Create file-like object from HTML string ----> StringIO
# from io import StringIO 

# -------------------------------------------Save provided HTML content to a VARIABLE first ---> 'html_content'

# html_content = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Sports World</title>
#     <style>
#         body { font-family: Arial, sans-serif; }
#         header, nav, section, article, footer { margin: 20px; padding: 15px; }
#         nav { background-color: #333; }
#         nav a { color: white; padding: 14px 20px; text-decoration: none; display: inline-block; }
#         nav a:hover { background-color: #ddd; color: black; }
#         .video { text-align: center; margin: 20px 0; }
#     </style>
# </head>
# <body>

#     <header>
#         <h1>Welcome to Sports World</h1>
#         <p>Your one-stop destination for the latest sports news and videos.</p>
#     </header>

#     <nav>
#         <a href="#football">Football</a>
#         <a href="#basketball">Basketball</a>
#         <a href="#tennis">Tennis</a>
#     </nav>

#     <section id="football">
#         <h2>Football</h2>
#         <article>
#             <h3>Latest Football News</h3>
#             <p>Read about the latest football matches and player news.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/football-video-id" frameborder="0" allowfullscreen>
#                 </iframe>
#             </div>
#         </article>
#     </section>

#     <section id="basketball">
#         <h2>Basketball</h2>
#         <article>
#             <h3>NBA Highlights</h3>
#             <p>Watch highlights from the latest NBA games.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/basketball-video-id" frameborder="0" allowfullscreen>
#                 </iframe>
#             </div>
#         </article>
#     </section>

#     <section id="tennis">
#         <h2>Tennis</h2>
#         <article>
#             <h3>Grand Slam Updates</h3>
#             <p>Get the latest updates from the world of Grand Slam tennis.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/tennis-video-id" frameborder="0" allowfullscreen></iframe>
#             </div>
#         </article>
#     </section>

#     <footer>
#         <form action="mailto:contact@sportsworld.com" method="post" enctype="text/plain">
#             <label for="name">Name:</label><br>
#             <input type="text" id="name" name="name"><br>
#             <label for="email">Email:</label><br>
#             <input type="email" id="email" name="email"><br>
#             <label for="message">Message:</label><br>
#             <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>
#             <input type="submit" value="Send">
#         </form>
#     </footer>

# </body>
# </html>
# """

# soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
# print(soup.h1.text) 
# print(soup.find_all('p'))
# links = soup.select('a[href]')
# for link in links:
#     print(link['href'])


#-------------------------------------------EXERCISE 2 Scraping robots.txt from Wikipedia

# import requests 

# url = 'https://en.wikipedia.org/robots.txt'
# response = requests.get(url)


#--------------------------------Add User-Agent header to mimic a real browser in order not to get a 403
# response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

# -------------------------------Check URL status code HTTP
# print(f"Status: {response.status_code}")   #>>>200

#--------------------------------Pass response.text ---the HTML content from 'response'---to BeautifulSoup 
# soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.text)
     

#-------------------------------------------EXERCISE 3 : Extracting Headers from Wikipedia’s Main Page

# page = 'https://en.wikipedia.org/'
# response = requests.get(page, headers= {'User-Agent': 'Mozilla/5.0'})

# soup = BeautifulSoup(response.text, 'html.parser')

# headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
# for i, heading in enumerate(headings):    #{i} = The number (1, 2, 3...) from loop counter
#     print(f"{i}. {heading.name}: {heading.get_text(strip=True)}")    #get the text inside that heading, cleaned up



#-------------------------------------------EXERCISE 4 : Checking for Page Title
#------------------------------------Write a Python program to check whether a page contains a title or not.


# url = 'https://en.wikipedia.org/'
# response = requests.get(url, headers= {'User-Agent': 'Mozilla/5.0'})

# soup = BeautifulSoup(response.text, 'html.parser')

# try:
#     url_title = soup.find('h1')
#     if url_title:
#         print(f'Here is the URL title: {url_title.get_text(strip=True)}.')
#     else: 
#         print('No URL title found!')
#         url_title = None
# except:
#     url_title = None
#     print("Error finding title")



#-------------------------------------------Exercise 5 : Analyzing US-CERT Security Alerts
#-------------------------------------------Write a Python program to get the number of security alerts issued by US-CERT in the current year.
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# import time

# current_year = datetime.now().year
# url = 'https://www.cisa.gov/news-events/cybersecurity-advisories?f%5B0%5D=advisory_type%3A93'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# Try with timeout and delay
# try:
#     time.sleep(2)  # Be polite
#     response = requests.get(url, headers=headers, timeout=15)
#     print(f"Status: {response.status_code}")
    
#     soup = BeautifulSoup(response.text, 'html.parser')
#     alert_divs = soup.find_all('div', class_='c-teaser__meta', string='Alert')
    
#     print(f"Total security alerts found: {len(alert_divs)}")
    
    
# except requests.exceptions.RequestException as e:
#     print(f"Connection failed: {e}")


#-------------------------------------------Exercise 6 Scraping Movie Details
# Write a Python program to get movie name, year and a brief summary of the top 10 random movies from this 
# IMBD website.


# import requests
# from bs4 import BeautifulSoup
# import random

# url = 'https://www.imdb.com/list/ls091294718/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find all movie items in the list (IMDb list structure)
# movie_items = soup.find_all('div', class_='lister-item-content')

# # Get top 10 random movies
# random_movies = random.sample(movie_items, min(10, len(movie_items)))       #picks 10 random movies from the  list

# print("Top 10 Random Movies:\n")
# for i, movie in enumerate(random_movies, 1):
#     # Extract title
#     title_elem = movie.find('h3', class_='lister-item-header')
#     title = title_elem.find('a').text.strip() if title_elem and title_elem.find('a') else "N/A"
    
#     # Extract year (usually in span after title)
#     year_elem = movie.find('span', class_='lister-item-year')
#     year = year_elem.text.strip('() ') if year_elem else "N/A"
    
#     # Extract summary (first paragraph or description)
#     summary_elem = movie.find('p', class_='')
#     summary = summary_elem.text.strip()[:150] + "..." if summary_elem else "No summary available"
    
#     print(f"{i}. **{title} ({year})**")
#     print(f"   Summary: {summary}\n")