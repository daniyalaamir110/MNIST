from flask import Flask, request, jsonify, abort
from predict import predict

app = Flask(__name__)

@app.route('/predict-digit', methods=['POST'])
def predict_digit():
    try:
        image_file = request.files['image']
        digit, probability = predict(image_file)

        data = {
            'digit': digit,
            'probability': probability
        }

        return jsonify(data)
    
    except Exception as e:
        abort(400, str(e))


if __name__ == '__main__':
    app.run()
