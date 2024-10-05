import numpy as np
import pandas as pd

from cifar.io.utils import get_s3_fs


def list_s3_dir(dir_path, fs, extension=""):
    return [
        file_path["name"]
        for file_path in fs.listdir(dir_path)
        if extension in file_path["name"]
    ]

def ray_list_cifar_files(dir_path):
    fs = get_s3_fs()
    files = list_s3_dir(dir_path, fs, ".npy")
    return pd.DataFrame({"file_name": files})


def read_dir(dir_path):
    fs = get_s3_fs()
    files = list_s3_dir(dir_path, fs, ".npy")
    loaded_data = [
        np.load(fs.open(npy_file), allow_pickle=True).item() for npy_file in files
    ]
    return loaded_data
