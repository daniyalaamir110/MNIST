import tensorflow as tf

def _train_model():
    # Load the MNIST dataset
    mnist = tf.keras.datasets.mnist.load_data()
    (X_train, y_train), (X_test, y_test) = mnist

    # Normalize the input data
    X_train_norm = tf.keras.utils.normalize(X_train, axis=1)
    X_test_norm = tf.keras.utils.normalize(X_test, axis=1)

    # Create the model architecture
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))    # Flatten the input images
    model.add(tf.keras.layers.Dense(128, activation="relu"))    # Add a hidden layer with 128 units and ReLU activation
    model.add(tf.keras.layers.Dense(128, activation="relu"))    # Add another hidden layer with 128 units and ReLU activation
    model.add(tf.keras.layers.Dense(10, activation="softmax"))  # Add an output layer with 10 units for 10 classes and softmax activation

    # Compile the model
    model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    # Train the model
    model.fit(X_train_norm, y_train, epochs=3)

    # Evaluate the model
    loss, accuracy = model.evaluate(X_test_norm, y_test)
    print("Loss = {:.2f}".format(loss))
    print("Accuracy = {:.2f}".format(accuracy))

    # Make predictions
    predictions = model.predict(X_test_norm)
    print("Predictions for the first image:")
    print(predictions[0])
    print("Model prediction: {}".format(predictions[0].argmax()))
    print("Actual label: {}".format(y_test[0]))

    # Save the trained model
    model.save("src/mnist_model.keras")


if __name__ == "__main__":
    _train_model()
