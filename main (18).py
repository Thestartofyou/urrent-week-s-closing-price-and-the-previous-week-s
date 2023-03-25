import requests

# Set the API endpoint and parameters
url = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_WEEKLY',
    'apikey': 'YOUR_API_KEY',
    'symbol': 'AAPL',
    'datatype': 'json'
}

# Send a GET request to the Alpha Vantage API
response = requests.get(url, params=params)

# If the response was successful, parse the JSON data
if response.status_code == 200:
    data = response.json()['Weekly Time Series']
    # Print the weekly close price and percentage change for the past 20 weeks
    prev_close = None
    for i in range(20):
        date = sorted(data.keys(), reverse=True)[i]
        close = float(data[date]['4. close'])
        if prev_close is not None:
            pct_change = (close - prev_close) / prev_close * 100
            print(f"Week ending {date}: {close:.2f} ({pct_change:.2f}%)")
        else:
            print(f"Week ending {date}: {close:.2f}")
        prev_close = close
else:
    # If the response was unsuccessful, print the HTTP status code
    print(f"Response returned with status code {response.status_code}")

