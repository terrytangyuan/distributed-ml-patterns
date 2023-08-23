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

See instructions [here](https://github.com/terrytangyuan/distributed-ml-patterns/blob/main/code/project/code/README.md).

# Clean-up

```
k3d cluster rm distml
kind delete cluster --name distml
```
