# Project Setup

```
k3d cluster create distml
k create ns kubeflow
kns kubeflow
k kustomize code/project/manifests | k apply -f -
```

# Run Workflow

```
k create -f code/project/manifests/e2e-demo/workflows-templates-tfjob.yaml
k create -f code/project/manifests/e2e-demo/e2e-workflow.yaml
```

# Clean-up

```
k3d cluster rm distml
```
