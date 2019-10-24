#  Lets quickly write a flask app that does something locally

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
	return {'IMAGE_CLASS_ID' : 'id', 'IMAGE_CLASS_NAME' : 'name' }


if __name__ == '__main__':
	app.run(host = 'localhost', port = '5000', debug = True)
