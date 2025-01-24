import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches the animals data from the API
    and returns a list of animals, each described as a dictionary
    """
    url = f"{BASE_URL}?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"No data found for the animal: {animal_name}.")
            return []
        else:
            print(f"Error {response.status_code}: {response.text}")
            return []
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []