# KUBERNETES
follow this links for more details:
 - [minikube install]()
 - [minikube setup](https://minikube.sigs.k8s.io/docs/tutorials/nvidia/)

```
sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker
minikube start --driver docker --container-runtime docker --gpus all --cpus 15 --memory 13312
```
Before you set up ray it is required to build image for ray and upload it minikube
```
eval $(minikube docker-env)
docker build -f dockerfile_ray -t ray_image .
```
Now you can deploy ray and mlflow.
```
helm install mlflow oci://registry-1.docker.io/bitnamicharts/mlflow
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update
helm install kuberay-operator kuberay/kuberay-operator --version 1.1.1
helm install -f override.yaml  raycluster kuberay/ray-cluster --version 1.1.1
```
After that make bucket in minio named 'ray'. Also create a minio token and paste it kubernetes section in `cifar.constants.secret.py`.
