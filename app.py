#print("Hello World")
from flask import Flask

app = Flask(__name__)

@app.route('/api/')
def home():
    return {"message": "Welcome to TDS Solver API"}

if __name__ == '__main__':
    app.run(debug=True)
    