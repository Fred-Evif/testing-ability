# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 07:29:57 2024

@author: FredEvif
"""


""" pyproject.toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
include = ["localaplace"]
exclude = ["images", "test.py", ".gitignore"]

[project]
name = "localaplace"
version = "0.0.1"
urls = { text = "https://github.com/LSTM-Kirigaya" }
authors = [
    { name = 'lstm-kirigaya', email = 'xxxxxxxx@qq.com' }
]
description = "implement of local laplace filter algorithm"
readme = "README.md"
requires-python = ">=3.5"
license = { text = "Apache 2.0" }
keywords = [
    'local laplace filter',
    'local-laplace-filter',
    'computer vision',
    'tone mapping',
    'image process'
]
classifiers = [
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3'
]
dependencies = [
    'numpy',
    'opencv-python',
    'tqdm'
]
"""