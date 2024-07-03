s3_secrets = {
    "use_ssl": False,
    "key": "...",
    "secret": "...",
    "client_kwargs": {"endpoint_url": "http://s3:9000"},
}

s3_secrets_pa = {
    "access_key": "...",
    "secret_key": "...",
    "endpoint_override": "http://s3:9000"
}
MLFLOW_TRACKING_URI = "http://tracking_server:5000",
MLFLOW_TRACKING_USERNAME = ''
MLFLOW_TRACKING_PASSWORD = ''

######################################
# kubernetes

MLFLOW_TRACKING_URI = "http://mlflow-tracking"
MLFLOW_TRACKING_USERNAME = '...'
MLFLOW_TRACKING_PASSWORD = '...'

s3_secrets = {
    "use_ssl": False,
    "key": "...",
    "secret": "...",
    "client_kwargs": {"endpoint_url": "http://mlflow-minio"},
}

s3_secrets_pa = {
    "access_key": "...",
    "secret_key": "...",
    "endpoint_override": "http://mlflow-minio"
}