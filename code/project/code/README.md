# Multi-worker Distributed Training

```
cd project/code
```

1.  Build an image
    ```
    docker build -f Dockerfile -t kubeflow/multi-worker-strategy:v0.1 .
    k3d image import kubeflow/multi-worker-strategy:v0.1 --cluster distml
    ```

2.  Specify your storageClassName and create a persistent volume claim to save 
    models and checkpoints
    ```
    kubectl create -f multi-worker-pvc.yaml
    ```

3.  Create a TFJob, if you use some GPUs other than NVIDIA, please replace 
    `nvidia.com/gpu` with your GPU vendor in the `limits` section.
    ```
    kubectl create -f multi-worker-tfjob.yaml
    ```
