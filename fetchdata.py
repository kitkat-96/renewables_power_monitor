import pandas as pd
import requests

historic_records = [] 

start_date = '2025-11-01T00:00Z' #YYYY‑MM‑DDT00:00Z
end_date = '2025-11-30T23:30Z' #YYYY‑MM‑DDT00:00Z

api_url = f"https://api.carbonintensity.org.uk/generation/{start_date}/{end_date}"

api_response = requests.get(api_url)
data = api_response.json()

for entry in data['data']:
    row = {'time': pd.to_datetime(entry['from'], utc=True)} # use 'from' as timestamp
    for fuel in entry['generationmix']:
        row[fuel['fuel']] = fuel['perc']
    historic_records.append(row)


df = pd.DataFrame(historic_records)

# print(row)
df.to_csv('generation_mix.csv', index=False)

# testing branch protection take 4