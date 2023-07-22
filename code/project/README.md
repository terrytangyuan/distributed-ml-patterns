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
k create ns kubeflow
kns kubeflow
k kustomize manifests | k apply -f -
```

# Run Workflow

```
k create -f manifests/e2e-demo/workflows-templates-tfjob.yaml
k create -f manifests/e2e-demo/e2e-workflow.yaml
```

# Clean-up

```
k3d cluster rm distml
kind delete cluster --name distml
```
