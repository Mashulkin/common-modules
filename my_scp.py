# -*- coding: utf-8 -*-
"""
Push and pull files to/from the server
"""
import os
import sys


__author__ = 'Vadim Arsenev'
__version__ = '1.0.0'
__data__ = '30.07.2021'


def scp_push(filename, server, directory):
    os.system(f'scp {filename} {server}:{directory}')


def scp_pull(filename, server, directory):
    os.system(f'scp {server}:{directory} {filename}')


def main(file):
    filename = f'{os.getcwd()}/data/{file}'

    # Webserver Oracle
    server = 'opc@129.159.248.160'
    directory = '/var/www/html/data/'

    scp_push(filename, server, directory)


if __name__ == '__main__':
    main(sys.argv[1])
