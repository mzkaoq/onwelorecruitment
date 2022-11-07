import requests
import csv

class CountryCodesApiHandler():
    def fetch(self):
        country_codes_url = "https://static.quandl.com/ECONOMIST_Descriptions/economist_country_codes.csv"
        try:
            response = requests.get(country_codes_url)
        except requests.exceptions.RequestException as err:
            print("request exception found")
            raise SystemExit(err)

        cr = csv.reader(response.text.splitlines(), delimiter=',')
        country_codes = list(map(lambda x: x[0].split("|"), list(cr)))[1:]

        return country_codes