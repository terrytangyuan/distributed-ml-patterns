FROM python:3.9

RUN pip install tensorflow==2.11.0 tensorflow_datasets==4.7.0

COPY data-ingestion.py /
COPY predict-service.py /
COPY model-selection.py /
COPY multi-worker-distributed-training.py /
