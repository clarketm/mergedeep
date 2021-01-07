import setuptools, os


def open_local(paths, mode="r", encoding="utf8"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)
    return open(path, mode=mode, encoding=encoding)


with open_local(["README.md"]) as f:
    long_description = f.read()

setuptools.setup(
    name="mergedeep",
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="A deep merge function for 🐍.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/mergedeep",
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
