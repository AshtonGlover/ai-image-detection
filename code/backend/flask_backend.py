from flask import Flask, jsonify, request
import tensorflow as tf
from preprocess import preprocess_image
import numpy as np

app = Flask(__name__)

image = None

@app.route('/api/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    image = file
    return jsonify({'message': f'Image uploaded successfully'}), 200

@app.route('/api/get_decision', methods=['GET'])
def get_decision():
    model = tf.keras.models.load_model('saved_model.h5')

    input_image = np.expand_dims(preprocess_image('/Users/ashtonglover/Desktop/ai-image-detection/data/test/FAKE/0.jpg'), axis=0)

    prediction = model.predict(input_image)[0][0]

    if prediction <= 0.5:
        return jsonify({'result': False}), 200
    return jsonify({'result': True}), 200
    


if __name__ == '__main__':
    app.run(debug=True)