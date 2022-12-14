FROM tensorflow/tensorflow:2.7.1

RUN pip install tensorflow_datasets==4.5.2

COPY multi-worker-distributed-training.py /
ENTRYPOINT ["python", "/multi-worker-distributed-training.py", "--saved_model_dir", "/train/saved_model/", "--checkpoint_dir", "/train/checkpoint"]
