
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "fst-mark-klik",
    version = "0.0.1",
    author= "Mark AJ Klik",
    author_email = "markklik@gmail.com",
    description = "Lightning Fast Serialization of DataFrames for Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/fstpackage/fstpy",
    packages = find_packages(),
    zip_safe = False,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha"
    ],
)
