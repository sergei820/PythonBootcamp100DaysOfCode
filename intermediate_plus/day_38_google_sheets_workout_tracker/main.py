from os import environ
from dotenv import load_dotenv
import requests

load_dotenv()

APP_ID = environ.get("NUTRITIONIX_APP_ID")
API_KEY = environ.get("NUTRITIONIX_API_KEY")

def start_app():
    print(API_KEY)



if __name__ == "__main__":
    start_app()
