import requests

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api"
get_response = requests.post(endpoint, json={"query":"Hello World"})
print(get_response.text)
print(get_response.status_code)
print(get_response.json()['message'])