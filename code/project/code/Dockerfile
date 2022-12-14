FROM tensorflow/tensorflow:2.11.0

RUN pip install tensorflow_datasets==4.7.0

COPY multi-worker-distributed-training.py /
ENTRYPOINT ["python", "/multi-worker-distributed-training.py", "--saved_model_dir", "/train/saved_model/", "--checkpoint_dir", "/train/checkpoint"]
