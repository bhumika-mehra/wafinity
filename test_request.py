import requests

http_payload = "GET /product.php?id=5 UNION SELECT * FROM users HTTP/1.1"  # SQLi

res = requests.post("http://127.0.0.1:8080/analyze", json={
    "http_request": http_payload
})

print(res.json())
