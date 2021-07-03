# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# import json

# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {
#     'start': '1',
#     'limit': '5000',
#     'convert': 'GBP'
# }
# headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': '5d02a36c-6d3b-489d-8b35-08ad48a33bec',
# }

# session = Session()
# session.headers.update(headers)

# try:
#     response = session.get(url, params=parameters)
#     data = json.loads(response.text)
#     print(data)

# except (ConnectionError, Timeout, TooManyRedirects) as e:
#     print(e)

# with open('crypto_data.json', 'w') as outfile:
#     json.dump(data, outfile)
