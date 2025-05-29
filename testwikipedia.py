
import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/94e85b626e80b6234bbc3d3e/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)
# {
#   "result": "success",
#   "base_code": "USD",
#   "conversion_rates": {
#     "EUR": 0.85,
#     "GBP": 0.75,
#     "JPY": 110.0, 