#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

def main():
    logging.basicConfig(filename='02.log', level=logging.WARNING)
    logging.critical('critical')
    logging.error('error')
    logging.warning('warning')
    logging.info('info')
    logging.debug('debug')

if __name__ == '__main__':
    main()

