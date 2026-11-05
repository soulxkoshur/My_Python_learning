import sys
import requests

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=2d049040aa2bb541fbb5d1a078d4747c0b7397ba3c8e49322b5aa8fff2170062")
    response = response.json()
    data =response['data']
    amount = float(sys.argv[1]) * float(data['priceUsd'])
    print(f"${amount:,.4f}")
except requests.RequestException as e:
    print(f"Error fetching Bitcoin price: {e}")
except TypeError:
    print("Command-line argument is not a number.")
except IndexError: 
    sys.exit("Missing command-line argument.")
