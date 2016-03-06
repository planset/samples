#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.config


def main():
    logging.config.fileConfig('04_logging.conf')
    logger = logging.getLogger('logExample')
    
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')

if __name__ == '__main__':
    main()

