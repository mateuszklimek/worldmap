import pycountry

for country in pycountry.countries:
    print country.name, country.alpha2
