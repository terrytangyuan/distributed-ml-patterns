# Multi-worker Distributed Training


1.  Build a image
    ```
    docker build -f Dockerfile -t kubeflow/multi-worker-strategy:v0.1 .
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
