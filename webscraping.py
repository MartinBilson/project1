import requests
from bs4 import beautifulsoup

#url of the webpage to scrape
url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

#send a get request to the webpage
response = requests.get(url)

#parse the html conten
response  = request.get(url)

#parse the html content
soup = BeautifulSoup(response.text, 'html.parser')

#find all the elements with the class card-content
titles = soup.find_all('h2', class_='title')

#Print the titles
for title in titles:
    print(title.text)