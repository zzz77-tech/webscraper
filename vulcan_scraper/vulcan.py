from bs4 import BeautifulSoup
import requests

#obtain the url of the site that we want to scrapt
url = 'https://vulcanpost.com/category/news/'
page = requests.get(url)

#store the articles 
articles =[]

# stores the weblink
links = []

#stores the results
results = []




soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.p)
news_headlines = soup.find_all('div',class_ = 'article-excerpt')
web_links = soup.find_all('a',class_ = 'article-list-item')

print(web_links)

# loop the headlines and append the headlines
for i in news_headlines:
    #print(i.find('p').text)
    articles.append(i.find('p').text)

for i in web_links:
    #print(i['href'])
    links.append('https://vulcanpost.com/'+ i['href'])

  
    


# traverse through every news article which is the links to the articles
# for every article, find the tag that contains the story and scrape 
# append results into array


for j in range(len(articles)):
    results.append([articles[j],links[j])
#print(results)
