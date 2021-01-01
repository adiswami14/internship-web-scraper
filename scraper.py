import requests

headers = {'User-Agent': 
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }

url = 'https://www.monster.com/jobs/search/?q=Software-Developer-Intern&where=New-Jersey' #monster job site
page = requests.get(url, headers = headers)
print(page.text)