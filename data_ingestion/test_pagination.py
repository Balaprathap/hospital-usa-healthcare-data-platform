from data_ingestion.pagination import fetch_all_hospital_data

records = fetch_all_hospital_data()

print("Total records fetched:", len(records))
print("First record:", records[0])