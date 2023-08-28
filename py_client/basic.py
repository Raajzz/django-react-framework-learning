import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get("https://httpbin.org/anything")
print(get_response.text)
print(get_response.json())
print(get_response.status_code)