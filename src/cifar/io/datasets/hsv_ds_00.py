from cifar.constants import plugin_triplet
from cifar.constants.secret import s3_secrets
from cifar.io.dataloaders.npy_loader import customDataModule

input_path = "/ray/cifar/raw/"
output_path = "/ray/cifar/hsv_ds_00/"
dataloader = customDataModule

keys_to_save = [
    "hsv",
    "labels",
    "test",
]

source_loader = plugin_triplet(
    "cifar.io.source_loader_s3",
    "ray_read_cifar_raw",
    {"dir_path": input_path},
)

plugins = (
    plugin_triplet(
        "cifar.preprocessing.format_converters",
        "rgb_to_hsv_map_batches",
        {"image_key": "data", "keep_source": False},
    ),
)

output_writer = plugin_triplet(
    "cifar.io.source_loader_s3",
    "ray_write_results",
    {"columns": keys_to_save, "dir_path": output_path},
)
