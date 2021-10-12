from flask import Flask, jsonify, request
app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

@app.route('/paymentAuth', methods=['POST'])
def post_payment_auth():
  data = request.get_json()
  print(data)
  return jsonify({ 'authorized': True, 'message': 'hoge' })


@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204

@app.route("/health")
def hello_world():
  return jsonify({ 'healthy': True })

if __name__ == "__main__":
    app.run()
