import requests
import pandas as pd

url = "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0"

response = requests.get(url, params={"limit":5})

print("status code:",response.status_code)

data = response.json()

records = data["results"]
df = pd.DataFrame(records)

print(df.head())
print(df.columns)