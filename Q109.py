import requests

# Write a program (assuming you have internet access) that fetches data
# from a public API using the requests module and prints part of the JSON
# response.
def fetch_data():
    url = 'https://api.publicapis.org/entries'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data['entries'][0])  # Print the first entry in the JSON response
    else:
        print('Failed to fetch data')

fetch_data()