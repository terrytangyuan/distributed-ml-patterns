import tensorflow as tf

images, labels = train  #A
images = images/255  #B

dataset = tf.data.Dataset.from_tensor_slices((images, labels))  #C
dataset  #D
# <TensorSliceDataset shapes: ((28, 28), ()), types: (tf.float64, tf.uint8)>

#A Split the training dataset object into images and labels.
#B Normalize the images.
#C Load in-memory array representation into a tf.data.Dataset object that will make it easier to use for training in TensorFlow.
#D Take a look at the information of the dataset such as shapes and data types.
