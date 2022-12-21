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

## Model loading & prediction

```
kubectl create -f predict-service.py
kubectl exec --stdin --tty predict-service -- bin/bash
python3 /predict-service.py
```

## Model serving

```
curl -s "https://raw.githubusercontent.com/kserve/kserve/release-0.10/hack/quick_install.sh" | bash
kubectl create -f inference-service.yaml
# Remove readiness check if needed
kubectl edit deployment flower-sample-predictor-default-00001-deployment

# https://kserve.github.io/website/master/get_started/first_isvc/#4-determine-the-ingress-ip-and-ports
INGRESS_GATEWAY_SERVICE=$(kubectl get svc --namespace istio-system --selector="app=istio-ingressgateway" --output jsonpath='{.items[0].metadata.name}')
kubectl port-forward --namespace istio-system svc/${INGRESS_GATEWAY_SERVICE} 8080:80
# start another terminal
export INGRESS_HOST=localhost
export INGRESS_PORT=8080

MODEL_NAME=flower-sample                                                                                                      
INPUT_PATH=@./inference-input.json
SERVICE_HOSTNAME=$(kubectl get inferenceservice ${MODEL_NAME} -o jsonpath='{.status.url}' | cut -d "/" -f 3)
curl -v -H "Host: ${SERVICE_HOSTNAME}" http://${INGRESS_HOST}:${INGRESS_PORT}/v1/models/$MODEL_NAME:predict -d $INPUT_PATH

## TODO: gRPC serving. Not working yet
# Client-side requirements
python3 -m pip install tensorflow-metal
python3 -m pip install tensorflow-macos==2.11.0
python3 -m pip install tensorflow-serving-api==2.11.0
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

