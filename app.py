from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def api():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'Invalid input, send JSON with a "question" field'}), 400
    return jsonify({'answer': f"You asked: {data['question']}"})

if __name__ == '__main__':
    app.run(debug=True)
