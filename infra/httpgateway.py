from flask import Flask, request, jsonify

app = Flask(__name__)


# HTTP Endpoint to receive messages
@app.route('/http-receiver', methods=['POST'])
def http_receiver():
    message = request.json.get('message')
    print(f"HTTP: Received message: {message}")
    return jsonify({"status": "received", "message": message}), 200


app.run(debug=True, port=5000)
print("started http receiver")
