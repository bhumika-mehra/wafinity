# rate_limiter.py
import time
from collections import defaultdict

class TokenBucket:
    def __init__(self, rate=1, capacity=5):
        self.rate = rate
        self.capacity = capacity
        self.tokens = defaultdict(lambda: capacity)
        self.last_check = defaultdict(lambda: time.time())

    def allow_request(self, client_ip):
        now = time.time()
        elapsed = now - self.last_check[client_ip]
        self.last_check[client_ip] = now
        self.tokens[client_ip] = min(self.capacity, self.tokens[client_ip] + elapsed * self.rate)

        if self.tokens[client_ip] >= 1:
            self.tokens[client_ip] -= 1
            return True
        else:
            return False
