from cifar.constants import plugin_spec, function_spec
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

source_loader = function_spec(
    "cifar.io.local_fs",
    "ray_read_cifar_raw",
    {"dir_path": input_path},
)

ray_source_connector = function_spec(
    "ray.data",
    "from_pandas",
    {"override_num_blocks": 4},
)

plugins = (
    plugin_spec(
        "cifar.preprocessing.format_converters",
        "rgb_to_hsv_map_batches",
        {"image_key": "data", "keep_source": False},
        {},
        {},
    ),
)

output_writer = function_spec(
    "",
    "write_numpy",
    {"columns": keys_to_save, "dir_path": output_path}
)
