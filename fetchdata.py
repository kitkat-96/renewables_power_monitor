import pandas as pd
import requests

# Generation data range

def month_starts(year: int):
    return pd.date_range(
        start=f"{year}-01-01",
        end=f"{year}-12-01",
        freq="MS",
        tz="UTC"
    )

def fetch_month(start: pd.Timestamp) -> list[dict]:
    end = start + pd.DateOffset(months=1)
    start_str = start.strftime('%Y-%m-%dT00:00Z')
    end_str = end.strftime('%Y-%m-%dT00:00Z')
    api_url = f"https://api.carbonintensity.org.uk/generation/{start_str}/{end_str}"
    api_response = requests.get(api_url)
    data = api_response.json()
    return data['data']

def normalise_month(data: list[dict]) -> list[dict]:
    records = []
    for entry in data:
        row = {"time": pd.to_datetime(entry["from"], utc=True)}
        for fuel in entry["generationmix"]:
            row[fuel["fuel"]] = fuel["perc"]
        records.append(row)
    return records

def fetch_year(year: int) -> pd.DataFrame:
    all_records = []
    for start in month_starts(year):
        month_data = fetch_month(start)
        month_rows = normalise_month(month_data)
        all_records.extend(month_rows)

    # Build DataFrame
    df = pd.DataFrame(all_records)
    df.sort_values("time", inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df

df = pd.DataFrame(fetch_year(2025))

# print(row)
df.to_csv('generation_mix.csv', index=False)

# testing branch protection take 4