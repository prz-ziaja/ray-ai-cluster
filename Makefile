init:
	mkdir -p data/mlflow_minio data/mlflow_postgres data/tensorboard

start-deployment:
	docker compose -f deployment/docker-compose.yaml --env-file deployment/.env up -d --build
restart-deployment:
	docker compose -f deployment/docker-compose.yaml --env-file deployment/.env restart
stop-deployment:
	docker compose -f deployment/docker-compose.yaml --env-file deployment/.env stop
