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

Switch to "kubeflow" namespace:
```
kubectl config set-context --current --namespace=kubeflow
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

After making code changes, run the following to resubmit the job:
```
kubectl delete tfjob --all; docker build -f Dockerfile -t kubeflow/multi-worker-strategy:v0.1 .; kind load docker-image kubeflow/multi-worker-strategy:v0.1 --name distml; kubectl create -f multi-worker-tfjob.yaml
```

## Model loading & prediction

```
kubectl create -f predict-service.yaml
kubectl exec --stdin --tty predict-service -- bin/bash
python3 /predict-service.py
```

## Model selection

```
python3 /model-selection.py
```

## Model serving

```
# Install KServe
curl -s "https://raw.githubusercontent.com/kserve/kserve/v0.10.0-rc1/hack/quick_install.sh" | bash

# Create inference service
kubectl create -f inference-service.yaml

# https://kserve.github.io/website/master/get_started/first_isvc/#4-determine-the-ingress-ip-and-ports
INGRESS_GATEWAY_SERVICE=$(kubectl get svc --namespace istio-system --selector="app=istio-ingressgateway" --output jsonpath='{.items[0].metadata.name}')
kubectl port-forward --namespace istio-system svc/${INGRESS_GATEWAY_SERVICE} 8080:80
# start another terminal
export INGRESS_HOST=localhost
export INGRESS_PORT=8080

MODEL_NAME=flower-sample                                                                                                      
INPUT_PATH=@./inference-input.json
SERVICE_HOSTNAME=$(kubectl get inferenceservice ${MODEL_NAME} -o jsonpath='{.status.url}' | cut -d "/" -f 3)
curl -v -H "Host: ${SERVICE_HOSTNAME}" "http://${INGRESS_HOST}:${INGRESS_PORT}/v1/models/$MODEL_NAME:predict" -d $INPUT_PATH

## TODO: gRPC serving. Not working yet
# Client-side requirements
python3 -m pip install tensorflow-metal
python3 -m pip install tensorflow-macos==2.11.0
python3 -m pip install tensorflow-serving-api==2.11.0
```

Autoscaled inference service:
```
# https://github.com/rakyll/hey
brew install hey
kubectl create -f autoscaled-inference-service.yaml

hey -z 30s -c 5 -m POST -host ${SERVICE_HOSTNAME} -D inference-input.json "http://${INGRESS_HOST}:${INGRESS_PORT}/v1/models/$MODEL_NAME:predict"
```

## Workflow

```
kubectl create -f workflow.yaml
```

## Debugging

Access the trained model
```
kubectl create -f access-model.yaml 
kubectl exec --stdin --tty access-model -- ls /trained_model
# Manually copy
# kubectl cp trained_model access-model:/pv/trained_model -c model-storage
```

Run TFServing commands in the KServe container:
```
kubectl exec --stdin --tty flower-sample-predictor-default-00001-deployment-84759dfc5f6wfj -c kserve-container -- /usr/bin/tensorflow_model_server --model_name=flower-sample \
      --port=9000 \
      --rest_api_port=8080 \
      --model_base_path=/mnt \
      --rest_api_timeout_in_ms=60000
```

## Cleanup

```
kubectl delete tfjob --all
kubectl delete wf --all
kubectl delete inferenceservice flower-sample
kubectl delete pods --selector=app=flower-sample-predictor-default-00001 --force --grace-period=0
kubectl delete pod access-model --force --grace-period=0
kubectl delete pod predict-service --force --grace-period=0
kubectl delete pvc strategy-volume
```

