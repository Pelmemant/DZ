import requests


def get_html_content(url):
    response = requests.get(url)
    return response.text


def post_form_data(url, data):
    response = requests.post(url, data=data)
    return response.json()


def check_status_code(url):
    response = requests.head(url)
    return response.status_code


n = "https://github.com/"
html_content = get_html_content(n)
print(html_content[:200])
form_data = {
    "username": "user",
    "password": "password"
}
response_json = post_form_data(n, form_data)
print(response_json)

status_code = check_status_code(n)
print(status_code)
