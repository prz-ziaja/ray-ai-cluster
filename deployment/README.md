# KUBERNETES
```
helm install mlflow oci://registry-1.docker.io/bitnamicharts/mlflow
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update
helm install kuberay-operator kuberay/kuberay-operator --version 1.1.1
helm install -f override.yaml  raycluster kuberay/ray-cluster --version 1.1.1
```