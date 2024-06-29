import importlib
import json

import numpy as np
import ray

from utils import parse_args, ray_connect

@ray.remote(scheduling_strategy="SPREAD")
def main(dataset_module_name):
    def function_builder(func, **kwargs):
        def inner(*inner_args, **inner_kwargs):
            return func(*inner_args, **kwargs, **inner_kwargs)

        inner.__name__ = func.__name__
        return inner

    dataset_module = importlib.import_module(dataset_module_name)
    source_loader_module, source_loader_name, source_loader_args = (
        dataset_module.source_loader
    )
    output_writer_module, output_writer_name, output_writer_args = (
        dataset_module.output_writer
    )

    print(source_loader_module, source_loader_name)
    source_loader = importlib.import_module(source_loader_module).__getattribute__(
        source_loader_name
    )
    output_writer = importlib.import_module(output_writer_module).__getattribute__(
        output_writer_name
    )

    dataset = source_loader(**source_loader_args)

    for plugin_module, plugin_name, plugin_args in dataset_module.plugins:
        plugin = function_builder(
            importlib.import_module(plugin_module).__getattribute__(plugin_name),
            **plugin_args
        )
        if "map_batches" in plugin.__name__:
            dataset = dataset.map_batches(plugin)
        elif "flat_map" in plugin.__name__:
            dataset = dataset.flat_map(plugin)
        else:
            dataset = dataset.map(plugin)

    output_writer(dataset, **output_writer_args)


if __name__ == "__main__":
    args = parse_args()
    ray_connect(args)

    ray.get(main.remote(args.pipeline_config))
