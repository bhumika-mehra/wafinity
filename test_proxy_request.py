import requests

url = "http://127.0.0.1:9090/login"
data = "username=admin&password=123"

res = requests.post(url, data=data)

print("Status Code:", res.status_code)
print("Response:", res.text)
