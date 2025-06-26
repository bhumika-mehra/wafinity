from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    return f"✅ Dummy login successful! Payload: {request.data.decode()}"

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    return f"✅ Reached dummy backend route: /{path}"

if __name__ == '__main__':
    app.run(port=5001)

