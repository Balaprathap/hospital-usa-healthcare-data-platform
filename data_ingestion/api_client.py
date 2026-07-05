import requests

from config.config import CMS_API_URL


def fetch_hospital_data(limit=1000, offset=0):

    params = {
        "limit": limit,
        "offset": offset
    }

    response = requests.get(CMS_API_URL, params=params)

    response.raise_for_status()

    return response.json()