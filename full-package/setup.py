import os

import setuptools


def get_version():
    filename = os.path.join(os.path.dirname(__file__), "hello", "__init__.py")
    with open(filename, "r") as f:
        for line in f.readlines():
            if "__version__" in line:
                return line.split(" = ")[-1].strip("\"")
    raise ValueError("Could not read version")


setuptools.setup(
    name="hello",
    version=get_version(),
    packages=["hello"],
    entry_points={
        'console_scripts': ['pyhello=hello:main']
    },
)
