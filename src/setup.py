#!/usr/bin/env python

from setuptools import setup, find_packages
import string
import sys, os

setup(
    name = "rackspace-rest-toys",
    version = "0.0.1",
    author = "Carlos D. Garza",
    author_email = "carlos.garza@rackspace.com",
    license = "BSD",
    url = "https://github.com/crc32a/Rackspace-rest-API-Toys",
    description = "Demonstration of rackspace reset servicees",
    packages = find_packages(),
    install_requires = ["python-dateutil","PyXB"],
    include_package_data = True,
)
