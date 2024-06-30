# Preprocessing
```
python3 ray_preprocess.py --pipeline-config cifar.io.datasets.hsv_ds_00 --pipeline-module cifar --remote-host ray://localhost:10001  --conda-env CIFAR
```
# Training
```
python3 ray_train.py --pipeline-config cifar.pipeline_configs.simple_cnn_arch --pipeline-module cifar --remote-host ray://localhost:10001 --conda-env CIFAR
```