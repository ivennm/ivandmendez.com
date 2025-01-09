from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run-drink-program', methods=['GET'])
def run_drink_program():
    # Simulate running the Python program
    drink_name = "Latte"  # Replace this with dynamic output if needed
    return jsonify({'drink': drink_name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

