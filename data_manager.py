import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/3fcb4979993d521647bbd3c417c00493/copyOfFlightDeals/prices"
SHEETY_CUSTOMERS_ENDPOINT= "https://api.sheety.co/3fcb4979993d521647bbd3c417c00493/copyOfFlightDeals/users"
SHEETY_TOKEN = {"Authorization": "Bearer qwd165e1g561er89g2d1261d81asd"}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_TOKEN)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=SHEETY_TOKEN)

    print("")
    def get_customer_emails(self):
        response = requests.get(url=SHEETY_CUSTOMERS_ENDPOINT, headers=SHEETY_TOKEN)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
