# MNIST Handwritten Digit Detection API

The MNIST dataset consists of handwritten digits from 0 to 9. We will use deep learning to build an API for handwritten digit detection.

## How it Works

1. The user submits an image of a handwritten digit to the API.
2. The API preprocesses the image, converting it to a format suitable for deep learning models.
3. The preprocessed image is then fed into the trained deep learning model.
4. The model predicts the digit represented by the image.
5. The predicted digit is returned as the output of the API.

## Project Setup

To set up the MNIST Handwritten Digit Detection API project, follow these steps:

1. Clone the project repository from GitHub:
    ```bash
    git clone https://github.com/daniyalaamir110/MNIST.git
    ```

2. Navigate to the project directory:
    ```bash
    cd MNIST
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Train the deep learning model:
    ```bash
    make train
    ```

5. Start the API server:
    ```bash
    make start
    ```

## How it Works

The API server should now be running on `http://localhost:5000`. You can test it by submitting an `image` of a handwritten digit using the provided API endpoint.
`http://localhost:5000/predict-digit`.

### Example response:
```
{
    "digit": 2,
    "probability": 0.9999926090240479
}
```
