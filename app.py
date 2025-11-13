from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Ipswich Coffee Shop API", "status": "healthy"})

@app.route('/products')
def products():
    return jsonify([{"id":1, "name":"Colombia Supremo", "price":14.99}])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
