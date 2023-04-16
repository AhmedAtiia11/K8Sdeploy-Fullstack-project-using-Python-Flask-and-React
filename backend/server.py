from flask import Flask,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/health')
def health():
    response = jsonify(msg="healthy")
    return response




if __name__=="__main__":
    app.run(debug=True,port=5000, host="0.0.0.0")
