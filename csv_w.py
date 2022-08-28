# -*- coding: utf-8 -*-
"""
Writing data to csv file
"""
import csv
import os.path


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '30.07.2021'


def write_csv(pathFile, data, order):
    if not os.path.exists(os.path.dirname(pathFile)):
        os.makedirs(os.path.dirname(pathFile))

    with open(pathFile, 'a', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)
