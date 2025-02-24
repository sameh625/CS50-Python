import json
import requests as req
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
try:
    num = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
else:
    try:
        response = req.get("https://api.coincap.io/v2/assets/bitcoin").json()
        price = float(response["data"]["priceUsd"])
        ans = num * price
        print(f"${ans:,.4f}")
    except req.RequestException:
        print("invalid")
