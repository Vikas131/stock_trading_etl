import requests
import os
from dotenv import load_dotenv
load_dotenv()
import csv

API_KEY = os.getenv("API_KEY")
limit = 2

url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={limit}&sort=ticker&apiKey={API_KEY}'

response = requests.get(url)
data = response.json()
tickers = []

for ticker in data['results']:
    tickers.append(ticker)


example = {'ticker': 'A', 
           'name': 'Agilent Technologies Inc.',
            'market': 'stocks',
            'locale': 'us',
            'primary_exchange': 'XNYS',
            'type': 'CS',
            'active': True,
            'currency_name': 'usd',
            'cik': '0001090872',
            'composite_figi': 'BBG000C2V3D6',
            'share_class_figi': 'BBG001SCTQY4',
            'last_updated_utc': '2025-09-30T06:05:29.844698933Z'}

fieldnames = list(example.keys())
output_csv = 'tickers.csv'
with open(output_csv,mode='w',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for t in tickers:
      row = {key: t.get(key,'')for key in fieldnames}
      writer.writerow(row)
print(f'Wrote{len(tickers)} rows to {output_csv}')