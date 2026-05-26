import requests


def fetch_arbeitnow_data():
    url = 'https://www.arbeitnow.com/api/job-board-api'

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    return data['data']