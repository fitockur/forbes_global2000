import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) C'
                  'hrome/77.0.3865.90 Safari/537.36',
}

for url in ['https://www.forbes.com/global2000/list/1/#tab:overall']:
    try:
        response = requests.get(url, headers=headers)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        content = response.content
        soup = BeautifulSoup(response.content, 'html.parser')

    print(soup.prettify())