FROM python:3.9

RUN pip install tensorflow==2.11.0 tensorflow_datasets==4.7.0

COPY data-ingestion.py /
COPY predict-service.py /
COPY multi-worker-distributed-training.py /
ENTRYPOINT ["python", "/multi-worker-distributed-training.py", "--saved_model_dir", "/trained_model/saved_model_versions/1/", "--checkpoint_dir", "/trained_model/checkpoint"]
