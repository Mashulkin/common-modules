# -*- coding: utf-8 -*-
"""
Removing data file
"""
import os


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '31.07.2021'


def remove_file(pathFile):
    try:
        os.remove(pathFile)
    except FileNotFoundError:
        pass
