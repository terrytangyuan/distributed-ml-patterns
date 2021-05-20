import tensorflow_io as tfio  #A

d_train = tfio.IODataset.from_mnist(  #B
    'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz',
    'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz')

#A Load TensorFlow I/O library.
#B Load the MNIST dataset from a URL to access dataset files directly without downloading via HTTP file system support.
