from data_ingestion.api_client import fetch_hospital_data

data = fetch_hospital_data(limit=5, offset=0)

print(data.keys())
print(data["results"][0])