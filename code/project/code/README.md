# Multi-worker Distributed Training

## Setup

```
cd project/code
```

Build the image
```
docker build -f Dockerfile -t kubeflow/multi-worker-strategy:v0.1 .
# If using k3d
k3d image import kubeflow/multi-worker-strategy:v0.1 --cluster distml
# If using kind
kind load docker-image kubeflow/multi-worker-strategy:v0.1 --name distml
```

Specify your storageClassName and create a persistent volume claim to save 
models and checkpoints
```
kubectl create -f multi-worker-pvc.yaml
```

## Submitting Training Job

Create a TFJob:
```
kubectl create -f multi-worker-tfjob.yaml
```

## Model serving

```
curl -s "https://raw.githubusercontent.com/kserve/kserve/release-0.10/hack/quick_install.sh" | bash
kubectl create -f inference-service.yaml

## TODO: Not working yet
# Client-side requirements
python3 -m pip install tensorflow-metal
python3 -m pip install tensorflow-macos==2.11.0
python3 -m pip install tensorflow-serving-api==2.11.0

MODEL_NAME=flower-sample
SERVICE_HOSTNAME=$(kubectl get inferenceservice ${MODEL_NAME} -o jsonpath='{.status.url}' | cut -d "/" -f 3)
python grpc_client.py --host $INGRESS_HOST --port $INGRESS_PORT --model $MODEL_NAME --hostname $SERVICE_HOSTNAME --input_path ./inference-input.json
```

## Debugging

Access the trained model
```
kubectl create -f access-model.yaml 
kubectl exec --stdin --tty access-model -- ls /trained_model
# Manually copy
# kubectl cp trained_model access-model:/pv/trained_model -c model-storage
```

## Cleanup

```
kubectl delete tfjob multi-worker-training
kubectl delete inferenceservice flower-sample
kubectl delete pod access-model
kubectl delete pvc strategy-volume
```

