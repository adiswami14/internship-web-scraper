import requests

headers = {'User-Agent': 
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    
url = 'https://www.internships.com/app/search?position-types=internships&context=seo&seo-mcid=31828911233804585432785361850966752390&remote=true&keywords=Paid&location=New+Jersey'
page = requests.get(url, headers = headers)
print(page.text)