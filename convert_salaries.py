import json

f = open('salaries')
currencies = set()

all_curriences = [
    'COP', 'Rp', 'TWD', 'Rs', 'EGP', 'ILS', 'S$',
    'LBP', 'AU$', 'QAR', 'C$', 'NZ$', 'SAR', '\xe2\x82\xac',
    'CHF', 'CNY', 'R$', 'R', 'RM', 'HK$', '$',
    '\xc2\xa5', 'ARS', 'RUB', 'MXN', 'PHP', 'AED']

values = [
    3108, 13822, 32.6, 66.8, 7.82, 3.88, 1.41,
    1507, 1.38, 3.64, 1.33, 1.52, 3.75, 0.94,
    1.02, 6.39, 3.84, 14.4, 4.26, 7.75, 1,
    6.39, 9.66, 66.4, 16.62, 47.06, 3.67
]

to_json = []

for line in f:
    line = line.split()
    currency = line[-2]
    val = float(line[-1])
    names = line[1:-2]
    in_dollars = val * 1.0 / values[all_curriences.index(currency)]
    print names, in_dollars
    to_json.append(
        {
            'name' : " ".join(names[1:]),
            'country_code' : names[0],
            'salary': in_dollars
        }
    )

to_json.append(
    {
        'name': 'United Kingdom',
        'salary': 64507.5,
        'country_code': 'UK'
    }
)

f = open('salary-data-script.json', 'w')
json.dump(to_json, f, indent=4)



