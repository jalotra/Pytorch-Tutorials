#  Lets quickly write a flask app that does something locally

from flask import Flask, jsonify, request
import requests
import inference as infer

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		file = request.files['file']
		image_bytes = file.read()
		class_id, class_name = infer.get_prediction(image_bytes)
		return jsonify({'class_id' : class_id, 'class_name' : class_name})

	


if __name__ == '__main__':
	app.run(host = 'localhost', port = '5000', debug = True)

