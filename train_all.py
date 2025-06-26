from preprocessing.vectorizer import train_vectorizer
from train_model import train

data = [
    "GET /index.html HTTP/1.1",
    "GET /index.php?id=1 OR 1=1 HTTP/1.1",
    "GET /search?q=<script>alert('XSS')</script> HTTP/1.1",
    "POST /login HTTP/1.1\nHost: site.com\n\nusername=admin&password=pass123",
    "GET /products?category=electronics<script>malicious</script> HTTP/1.1"
]

labels = [1, -1, -1, 1, -1]  # 1: Benign, -1: Malicious (for IsolationForest)

X = train_vectorizer(data)
train(X)
