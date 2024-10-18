import requests

url = "https://www.royalroad.com/fiction/62881/reborn-as-a-demonic-tree"

response = requests.get(url)

print(response.text)
