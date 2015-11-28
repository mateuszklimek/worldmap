import pycountry
import requests
import json
import argparse


def country_list(geojson_pth):
    with open(geojson_pth) as f:
        data = json.load(f)

    return [obj['properties']['name'] for obj in data['objects']['countries']['geometries']]


def fetch_ann_avgs(geojson_pth, output_path):
    """
    Fetch annual avgs for all countries.
    """
    ann_avgs = []
    for country in country_list(geojson_pth):
        try:
            country_code = pycountry.countries.get(name=country)
        except:
            print "pycountry did not find", country
            continue
        skipped = []
        fmt_str = (
            "http://climatedataapi.worldbank.org/climateweb/rest/v1/"
            "country/mavg/bccr_bcm2_0/tas/1980/1999/{}.JSON"
        )
        print "fetching data for ", country_code.alpha3
        fetched = requests.get(fmt_str.format(country_code.alpha3))
        try:
            data = fetched.json()
        except ValueError:
            skipped.append(country)
            print "no data fetched for", country
            continue

        ann_avgs.append({
            'name': country,
            'minTemperature': min(data[0]['monthVals']),
            'maxTemperature': max(data[0]['monthVals'])
        })
    print skipped
    print ann_avgs
    with open(output_path, 'w') as f:
        json.dump(ann_avgs, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch climate data')
    parser.add_argument('geojson', help='path to geojson')
    parser.add_argument('output', help='output json file path')

    args = parser.parse_args()
    fetch_ann_avgs(args.geojson, args.output)
