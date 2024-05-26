from setuptools import find_packages, setup

setup(
    name="cifar",
    version="0.1",
    description="ML package for cifar dataset classification using ray-ai-cluster setup.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://github.com/prz-ziaja/ray-ai-cluster",
    author="prz-ziaja",
    author_email="None",
)
