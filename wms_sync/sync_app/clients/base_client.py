import requests

class BaseClient:
    def post_data(self, url, data):
        if data:
            response = requests.post(url, json=data)
            print(f'POST {url}: {response.status_code}')
