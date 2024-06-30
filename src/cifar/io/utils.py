import s3fs
from pyarrow import fs

from cifar.constants.secret import s3_secrets_pa, s3_secrets


def get_s3_fs_pa():
    fs_pa = fs.S3FileSystem(**s3_secrets_pa)
    return fs_pa

def get_s3_fs():
    fs = s3fs.S3FileSystem(anon=False, **s3_secrets)
    return fs
