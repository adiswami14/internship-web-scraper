import requests
from bs4 import BeautifulSoup
from notifier import notify

headers = {'User-Agent': 
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }


#internship_loc = input("Where are you searching for an internship? ") 
# this is where I was able to enter the area to search for internship

#url = 'https://www.monster.com/jobs/search/?q=Software-Developer-Intern&where='+internship_loc #monster job site

url = 'https://www.monster.com/jobs/search/?q=Software-Developer-Intern&where=New-Jersey'
page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'ResultsContainer')

internships = results.find_all('section', class_='card-content')

for internship in internships:
    title = internship.find('h2', class_='title')
    company = internship.find('div', class_='company')
    location = internship.find('div', class_='location')
    tag= internship.find('a')
    

    if None in (title, company, location, tag):
        continue

    link = tag.get('href')
    #print(title.text.strip())
    #print(company.text.strip())
    #print(location.text.strip())
    notify(title.text.strip(), company.text.strip(), location.text.strip(), link.strip())
    #print()