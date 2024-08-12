import tensorflow as tf
from preprocess import preprocess_image
import numpy as np

model = tf.keras.models.load_model('saved_model.h5')

input_image = np.expand_dims(preprocess_image('/Users/ashtonglover/Desktop/ai-image-detection/data/test/FAKE/0.jpg'), axis=0)

prediction = model.predict(input_image)

print(prediction[0][0])