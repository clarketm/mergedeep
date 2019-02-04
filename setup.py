import re

import setuptools, os


def open_local(paths, mode="r", encoding="utf8"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)
    return open(path, mode=mode, encoding=encoding)


with open_local(["mergedeep", "__init__.py"]) as f:
    version = re.search(r"__version__ = [\"'](\d+\.\d+\.\d+)[\"']", f.read()).group(1)

with open_local(["README.md"]) as f:
    long_description = f.read()


setuptools.setup(
    name="mergedeep",
    version=version,
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="A deep merge function for 🐍.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/mergedeep",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
