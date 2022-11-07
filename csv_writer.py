import requests
import csv


from secrets import NASDAQ_KEY


class CsvWriter:
    def __init__(self,start_date,end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.header_counter = 0

    def save(self,country_codes):
        data_file = open('data_file.csv', 'w')
        for country in country_codes:
            api_url = f'https://data.nasdaq.com/api/v3/datasets/ECONOMIST/BIGMAC_{country[1]}?start_date={self.start_date}&end_date={self.end_date}&api_key={NASDAQ_KEY}'
            try:
                response = requests.get(api_url)
            except requests.exceptions.RequestException as err:
                print("request exception found")
                raise SystemExit(err)
            data = response.json()

            country_data = data["dataset"]
            csv_writer = csv.writer(data_file)

            if self.header_counter == 0:
                headers = country_data["column_names"]
                headers.insert(0, "contry_name")
                csv_writer.writerow(headers)
                self.header_counter += 1
            if country_data["data"] != []:
                rows = country_data["data"][0]
                rows.insert(0, country[0])
                csv_writer.writerow(rows)

        data_file.close()