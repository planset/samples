#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

def main():
    FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
    logging.basicConfig(format=FORMAT)
    logging.critical('critical')
    logging.error('error')
    logging.warning('warning')
    logging.info('info')
    logging.debug('debug')

if __name__ == '__main__':
    main()

