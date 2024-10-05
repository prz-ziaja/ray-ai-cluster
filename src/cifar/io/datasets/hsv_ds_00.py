from cifar.constants import plugin_spec, function_spec
from cifar.io.dataloaders.npy_loader import customDataModule
from cifar.io.utils import get_s3_fs_pa
from torchvision.transforms import v2

input_path = "s3://ray/cifar/raw/"
output_path = "s3://ray/cifar/hsv_ds_00/"
dataloader = customDataModule

metadata_path = output_path
image_dir_path = input_path

transform = None

keys_to_save = [
    "hsv",
    "labels",
    "test",
]

source_loader = function_spec(
    "cifar.io.source_loader_s3",
    "ray_list_cifar_files",
    {"dir_path": input_path},
)

ray_source_connector = function_spec(
    "ray.data",
    "from_pandas",
    {"override_num_blocks": 1},
)

plugins = (
    plugin_spec(
        "cifar.preprocessing.reader",
        "read_npy_map_batches",
        {"file_name_key": "file_name", "keep_source": False},
        {},
        {},
    ),
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
    {"column": keys_to_save, "path": output_path, "filesystem": get_s3_fs_pa()}
)
