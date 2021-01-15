import os  #A
import tensorflow_io as tfio  #B

endpoint="postgresql://{}:{}@{}?port={}&dbname={}".format(  #C
    os.environ['TFIO_DEMO_DATABASE_USER'],
    os.environ['TFIO_DEMO_DATABASE_PASS'],
    os.environ['TFIO_DEMO_DATABASE_HOST'],
    os.environ['TFIO_DEMO_DATABASE_PORT'],
    os.environ['TFIO_DEMO_DATABASE_NAME'],
)

dataset = tfio.experimental.IODataset.from_sql(  #D
    query="SELECT co, pt08s1 FROM AirQualityUCI;",
    endpoint=endpoint)
print(dataset.element_spec)  #E
# {'co': TensorSpec(shape=(), dtype=tf.float32, name=None), 'pt08s1': TensorSpec(shape=(), dtype=tf.int32, name=None)}

#A Load Python’s built-in OS  library for loading environment variables related to the PostgreSQL database.
#B Load TensorFlow I/O library.
#C Construct the endpoint for accessing the PostgreSQL database.
#D Select two columns from the AirQualityUCI table in the database and instantiate a tf.data.Dataset object.
#E Inspect the specification of the dataset such as the shape and data type for each column.
