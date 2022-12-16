# Multi-worker Distributed Training

```
cd project/code
```

1.  Build an image
    ```
    docker build -f Dockerfile -t kubeflow/multi-worker-strategy:v0.1 .
    # If using k3d
    k3d image import kubeflow/multi-worker-strategy:v0.1 --cluster distml
    # If using kind
    kind load docker-image kubeflow/multi-worker-strategy:v0.1 --name distml
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

4.  Access the trained model
    ```
    kubectl create -f access-model.yaml 
    kubectl exec --stdin --tty access-model -- ls /train/saved_model
    kubectl cp access-model:/train ./trained_model/

    kubectl cp ./trained_model/ access-model:/mnt/pvc/train/saved_model
    ```

5.  Model serving

    ```
    curl -s "https://raw.githubusercontent.com/kserve/kserve/release-0.10/hack/quick_install.sh" | bash
    kubectl create -f inference-service.yaml
    ```
