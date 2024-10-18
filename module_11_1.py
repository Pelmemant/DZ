import requests

url = "https://www.royalroad.com/home"

response = requests.get(url)

print(response.text)
