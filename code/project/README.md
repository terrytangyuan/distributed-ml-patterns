# Project Setup

```
cd project/
k3d cluster create distml
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
```
