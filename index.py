from flask import Flask, jsonify, request
from services import CreditExamination
app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 }
]

@app.route('/paymentAuth', methods=['POST'])
def post_payment_auth():
  data = request.get_json()
  print(data)
  if CreditExamination.exam('test', data['amount']):
    return jsonify({ 'authorised': True })
  else:
    return jsonify({ 'authorised': False, 'message': 'Payment declined: amount exceeded. [' + str(data['amount']) + ']' })


@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204

@app.route("/health")
def hello_world():
  return jsonify({ 'healthy': True })

if __name__ == "__main__":
    app.run()
