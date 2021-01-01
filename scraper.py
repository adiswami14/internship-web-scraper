import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }


internship_loc = input("Where are you searching for an internship?")
for char in internship_loc:
    if char == ' ':
        char = '-'

url = 'https://www.monster.com/jobs/search/?q=Software-Developer-Intern&where='+internship_loc #monster job site
page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'ResultsContainer')

internships = results.find_all('section', class_='card-content')

for internship in internships:
    title = internship.find('h2', class_='title')
    company = internship.find('div', class_='company')
    location = internship.find('div', class_='location')

    if None in (title, company, location):
        continue

    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print()