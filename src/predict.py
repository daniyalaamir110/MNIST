import tensorflow as tf
import numpy as np
import cv2

def predict(img):
    model = tf.keras.models.load_model("src/mnist_model.keras")

    # Preprocessing image
    img = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (28, 28))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.bitwise_not(img)
    img = img.reshape(1, 28, 28, 1)
    img = img / 255.0

    res = model.predict(img)[0]

    return int(np.argmax(res)), float(max(res))
