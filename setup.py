#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Dec 12, 2016

@author: timekeeper
"""

from setuptools import setup

# module_database = Extension('digin_database',)

setup(name='digin_database',
      version='0.1',
      description="Python pymysql wrapper",
      zip_safe=False,
      packages=['digin_database'], install_requires=['pymysql', 'lxml'])