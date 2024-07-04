# Intro
The following cluster setup can be deployed two ways:
 - using docker compose,
 - using kubernetes.
However deployment using kubernetes is more scalable and realiable thanks to already defined charts. I strongly recommend deploying using kubernetes.
The setup was developed on ubuntu 24.04. Deployment on other platforms may cause unexpected problems. 

# Prerequisite
## Docker
 - Install docker - [link](https://docs.docker.com/engine/install/ubuntu/).
 - Install NVIDIA Container Toolkit - [link](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html).
## Kubernetes
Kubernetes can be setup in many different ways. The development of the setup was done using minikube. In the case of minikube perform steps in section Prerequisite.Docker and additionale perform steps below:
 - Install minikube - [link](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download)
 - Setup gpu for minikube - [link](https://minikube.sigs.k8s.io/docs/tutorials/nvidia/)
 - Install helm - [link](https://helm.sh/docs/intro/install/)

# Deployment
## Docker
In the case of docker at this point you can execute `make start-dc-deployment` in the main repo directory.  
However some parts in docker deployment require manual setup.  
When docker deployment is running open browser and go to 'localhost:9001' - minio login should show up.  
Log in using credentials defined in `.env` file and create 2 buckets - `ray` and `mlflow`.  
Next create a token and paste keys into `.env` file (override `MINIO_ACCESS_KEY=...` and `MINIO_SECRET_ACCESS_KEY=...`).
Also paste keys into `src.cifar.constants.secret.py` in docker section. Also comment out all lines in kubernetes section in mentioned file.

## KUBERNETES
First startup minikube cluster by executing:
```
sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker
minikube start --driver docker --container-runtime docker --gpus all --cpus 15 --memory 13312
```

Next you can execute `make start-k8s-deployment` in the main directory of this repo.

Next you need to write down some k8s secrets - mlflow and minio. The simplest way to do this is to check the secrets in k9s. Also this can be done by executing:
```
kubectl get secrets -A
# find mlflow and minio secrets
kubectl get secret -o yaml <secret_name>
# copy values in data section
echo <encrypted data> | base 64
# results of the upper command is decoded value
```
When you have the secrets you can log into minio. Create a bucket in minio named `ray`. Next create a minio token and paste it kubernetes section in `cifar.constants.secret.py`. Also paste the mlflow secrets that you have decrypted.
