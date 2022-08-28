# -*- coding: utf-8 -*-
"""
Reading data from csv file
"""


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '30.07.2021'


def read_txt(filename):
    with open(filename, 'r') as file:
        text = file.read().strip()
    
    return text
