# -*- coding: utf-8 -*-
"""
Writing and reading data to/from json file
"""
import os.path
import json


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '30.07.2021'


def json_write(pathFile, data):
    if not os.path.exists(os.path.dirname(pathFile)):
        os.makedirs(os.path.dirname(pathFile))

    with open(pathFile, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def json_read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
