import requests
import pycountry
from bs4 import BeautifulSoup

ACCESS_TOKEN='e7a082245b1a6d860730eabecaf3f59b1b0d0a4b427312d1'
country_num = 0

for country in pycountry.countries:
    country_num += 1
    if country_num < 11:
        continue

    country_code = country.alpha2
    url = 'http://www.payscale.com/research/%s/Skill=Software_Development/Salary' % country_code
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    currency = ''
    num_sal = 0
    value = 0

    for salary in soup.find_all("td", class_="vm"):
        salary = salary.text.replace(',', '').strip()
        for i in range(len(salary)):
            if salary[i:].isdigit():
                currency = salary[:i].strip()
                value += int(salary[i:])
                num_sal += 1
                break

    if num_sal > 0:
        print country_num, country.alpha2, country.name, currency, value * 1.0 / num_sal if num_sal else 0




