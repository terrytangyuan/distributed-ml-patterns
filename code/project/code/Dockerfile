FROM tensorflow/tensorflow:2.1.0-gpu-py3

RUN pip install tensorflow_datasets==2.1.0

COPY multi-worker-distributed-training.py /
ENTRYPOINT ["python", "/multi-worker-distributed-training.py", "--saved_model_dir", "/train/saved_model/", "--checkpoint_dir", "/train/checkpoint"]
