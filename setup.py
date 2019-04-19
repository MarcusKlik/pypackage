#  fst-format - Python package for ultra fast storage and retrieval of datasets
#
#  Copyright (C) 2019-present, Mark AJ Klik
#
#  This file is part of the fst-format Python package.
#
#  The fst-format Python package is free software: you can redistribute it
#  and/or modify it under the terms of the GNU Affero General Public License
#  version 3 as published by the Free Software Foundation.
#
#  The fst-format Python package is distributed in the hope that it will be
#  useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
#  General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with the fst-format Python package. If not, see
#  <http://www.gnu.org/licenses/>.
#
#  You can contact the author at:
#  - fst-format source repository: https://github.com/fstpackage/fst-format

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "fst-format",
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
    test_suite='nose.collector',
    tests_require=['nose']
)
