from contry_codes_api import CountryCodesApiHandler
from s3_manager import S3Manager
from csv_writer import CsvWriter

start_date = "2021-07-31"
end_date = "2021-07-31"

if __name__ == "__main__":
    country_codes_manager = CountryCodesApiHandler()
    country_codes = country_codes_manager.fetch()
    csv_writer = CsvWriter(start_date,end_date)
    csv_writer.save(country_codes)
    s3_manager = S3Manager()
    s3_manager.send()