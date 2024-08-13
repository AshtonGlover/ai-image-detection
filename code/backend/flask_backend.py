from flask import Flask, jsonify, request
import tensorflow as tf
import sys
sys.path.append('/Users/ashtonglover/Desktop/ai-image-detection/code')
from preprocess import preprocess_image
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

image = None
uploaded = False

@app.route('/api/upload_image', methods=['POST'])
def upload_image():
    global image, uploaded
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    image = file

    uploaded = True

    return jsonify({'message': f'Image uploaded successfully'}), 200

@app.route('/api/get_decision', methods=['GET'])
def get_decision():
    global image, uploaded
    if not uploaded:
        return jsonify({'error': 'Must upload an image first'}), 400
    
    model = tf.keras.models.load_model('/Users/ashtonglover/Desktop/ai-image-detection/code/saved_model.h5')

    input_image = np.expand_dims(preprocess_image(image), axis=0)
 
    prediction = model.predict(input_image)[0][0]

    image = None

    print(prediction)

    if prediction <= 0.5:
        return jsonify({'result': False}), 200
    return jsonify({'result': True}), 200

if __name__ == '__main__':
    app.run(debug=True)