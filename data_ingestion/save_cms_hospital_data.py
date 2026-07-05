import requests
import pandas as pd

url = "https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0"

response = requests.get(url, params={"limit": 1000})

data = response.json()
records = data["results"]

df = pd.DataFrame(records)

df.to_csv("data_ingestion/cms_hospital_quality.csv", index=False)

print("Saved CMS hospital data successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))