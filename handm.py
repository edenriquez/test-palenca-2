import requests
import json 
session = requests.Session()
start = 0
end = 80
products = session.get("https://www2.hm.com/es_mx/search-results/_jcr_content/search.display.json?q=zapatos&sort=stock&image-size=small&image=stillLife&offset={}&page-size={}&page-size=40".format(start, end), headers={
    'authority':'www2.hm.com',
    'accept':'application/json, */*; q=0.01',
    'accept-language':'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7',
    'sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"macOS"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'
})

filtered_products = json.loads(products.content)['products']

for product in filtered_products:
    print(json.dumps(product, indent=2))
