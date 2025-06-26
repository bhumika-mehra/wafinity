from aiohttp import web, ClientSession
import joblib
import os
import datetime
from rate_limiter import TokenBucket

# Load ML model and vectorizer
model = joblib.load("models/waf_model.joblib")
vectorizer = joblib.load("models/vectorizer.joblib")

# Initialize token bucket rate limiter (e.g., 1 req/sec, burst of 5)
rate_limiter = TokenBucket(rate=1, capacity=5)

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

async def handle_request(request):
    client_ip = request.remote or "127.0.0.1"

    # Apply rate limiting
    if not rate_limiter.allow_request(client_ip):
        return web.Response(status=429, text="Too Many Requests - Rate Limit Exceeded")

    # Read HTTP data
    try:
        http_data = await request.read()
        http_text = http_data.decode(errors='ignore')
    except Exception as e:
        return web.Response(status=400, text="Invalid HTTP Payload")

    # ML classification
    vec = vectorizer.transform([http_text])
    prediction = model.predict(vec)[0]
    label = 'malicious' if prediction else 'benign'

    # Log the request
    with open("logs/request_log.csv", "a") as f:
        f.write(f"{datetime.datetime.now()},{http_text.replace(',', ' ')},{label}\n")

    # Block malicious requests
    if prediction == 1:
        return web.Response(status=403, text="Blocked: Malicious Request")

    # Forward to backend
    backend_url = f"http://127.0.0.1:5001{request.rel_url}"
    headers = dict(request.headers)

    async with ClientSession() as session:
        try:
            async with session.request(
                method=request.method,
                url=backend_url,
                data=http_data,
                headers=headers
            ) as resp:
                content = await resp.read()
                return web.Response(status=resp.status, body=content, headers=resp.headers)
        except Exception as e:
            return web.Response(status=500, text=f"Error: {str(e)}")

# Create app and route
app = web.Application()
app.router.add_route("*", "/{tail:.*}", handle_request)

if __name__ == "__main__":
    web.run_app(app, port=9090)
