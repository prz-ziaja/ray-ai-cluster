init:
	mkdir -p data/mlflow_minio data/mlflow_postgres data/tensorboard

start-dc-deployment:
	docker compose -f deployment/docker-compose.yaml --env-file deployment/.env up -d --build
restart-dc-deployment:
	docker compose -f deployment/docker-compose.yaml --env-file deployment/.env restart
stop-dc-deployment:
	docker compose -f deployment/docker-compose.yaml --env-file deployment/.env stop

start-minikube:
	sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker
	minikube start --driver docker --container-runtime docker --gpus all --cpus 15 --memory 13312

start-k8s-deployment:
	eval $(minikube docker-env)
	docker build -f ./deployment/dockerfile_ray -t ray_image ./deployment/
	helm install mlflow oci://registry-1.docker.io/bitnamicharts/mlflow
	helm repo add kuberay https://ray-project.github.io/kuberay-helm/
	helm repo update
	helm install kuberay-operator kuberay/kuberay-operator --version 1.1.1
	helm install -f ./deployment/override.yaml  raycluster kuberay/ray-cluster --version 1.1.1
stop-k8s-deployment:
	echo 0	

start-local:
	mkdir -p run
	cd run
	ray start --head
	nohup mlflow ui > mlflow.log &

stop-local:
	ray stop
	echo "you have to manually kill following processes"
	ps -aux | grep mlflow