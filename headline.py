# -*- coding: utf-8 -*-
"""
Reading data from csv file
"""
from common_modules.csv_w import write_csv
from common_modules.txt_r import read_txt

import os.path


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '22.08.2021'


def print_headline(filename, columns, order):
    """
    Insert table header
    """
    if os.path.isfile(filename):
        return
    headline = dict()
    for line in read_txt(columns).split('\n'):
        key = line.split(':')[0].strip()
        value = line.split(':')[1].strip()
        headline.update({key: value})
    write_csv(filename, headline, order)
