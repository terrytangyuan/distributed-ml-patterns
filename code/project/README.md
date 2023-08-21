# Project Setup

## Cluster

```
cd project/
```

Via `kind`:

```
go install sigs.k8s.io/kind@v0.17.0
kind create cluster --name distml --image kindest/node:v1.25.3
```

Or via `k3d`:

```
k3d cluster create distml --image rancher/k3s:v1.25.3-k3s1
```


```
kubectl create ns kubeflow
kns kubeflow
kubectl kustomize manifests | kubectl apply -f -
```

# Run Workflow

```
kubectl create -f manifests/e2e-demo/workflows-templates-tfjob.yaml
kubectl create -f manifests/e2e-demo/e2e-workflow.yaml
```

# Clean-up

```
k3d cluster rm distml
kind delete cluster --name distml
```
