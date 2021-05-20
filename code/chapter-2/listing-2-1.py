import tensorflow as tf  #A

train, test = tf.keras.datasets.fashion_mnist.load_data()  #B

# Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz
# 32768/29515 [=================================] - 0s 0us/step
# Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-images-idx3-ubyte.gz
# 26427392/26421880 [==============================] - 0s 0us/step
# Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-labels-idx1-ubyte.gz
# 8192/5148 [===============================================] - 0s 0us/step
# Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-images-idx3-ubyte.gz
# 4423680/4422102 [==============================] - 0s 0us/step

#A Load TensorFlow library.
#B Download the Fashion-MNIST dataset and then load it into memory.
