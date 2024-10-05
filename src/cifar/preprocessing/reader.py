import numpy as np
from cifar.io.utils import get_s3_fs


def read_npy_map_batches(row, file_name_key, keep_source=False):
    fs = get_s3_fs()

    file_names = row[file_name_key]
    labels = []
    test = []
    data = []
    for file_name in file_names:
        temp = np.load(fs.open(file_name), allow_pickle=True).item()
        labels.append(np.array(temp['labels']).reshape([-1,1]))
        test.append(np.array(temp['test']).reshape([-1,1]))
        data.append(temp['data'])

    row['labels'] = np.concatenate(labels)
    row['test'] = np.concatenate(test)
    # move channel axis to 2nd position (for torch)
    row['data'] = np.transpose(np.concatenate(data), [0,3,1,2])

    if not keep_source:
        _ = row.pop(file_name_key)

    return row
