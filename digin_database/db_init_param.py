# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on May 4, 2012

@author: timekeeper
"""
import os

import configparser


class InitConnectingParam(object):
    """
    classdocs
    """
    __connection_mysql = {"host": "",
                          "user": "",
                          "password": "",
                          "dbname": ""}
    __source = {}

    __receiver = []

    __filename = None

    def __init__(self, filename):
        """
        Constructor
        """
        self.__filename = filename

    def initDBParams(self):
        """
        Initialization of data base connection parameters
        """
        try:
            if not os.path.isfile(self.__filename):
                print("Error file '%s' dosen't exists" % self.__filename)
            cnf = configparser.ConfigParser()
            cnf.read(self.__filename)
            sections = cnf.sections()
            options = cnf.options(sections[sections.index("database")])
            for option in options:
                val = cnf.get(sections[sections.index("database")], option)
                self.__connection_mysql[option] = val
        except Exception as exc:
            raise exc
        return self.__connection_mysql

    def initSource(self, source_type=""):
        try:
            if not os.path.isfile(self.__filename):
                print("Error file '%s' dosen't exists" % self.__filename)
            cnf = configparser.ConfigParser()
            cnf.read(self.__filename)
            sections = cnf.sections()
            options = cnf.options(sections[sections.index("source")])
            for option in options:
                val = cnf.get(sections[sections.index("source")], option)
                self.__source[option] = val
        except Exception as exc:
            raise exc
        return self.__source[source_type]

    def initLogFile(self):
        try:
            if not os.path.isfile(self.__filename):
                print("Error file '%s' dosen't exists" % self.__filename)
            cnf = configparser.ConfigParser()
            cnf.read(self.__filename)
            sections = cnf.sections()
            options = cnf.options(sections[sections.index("log")])
            for option in options:
                val = cnf.get(sections[sections.index("log")], option)
                self.__source[option] = val
        except Exception as exc:
            raise exc
        return self.__source["log_file"]

    def initReceiverParams(self):
        """
        Initialization of receivers
        """
        try:
            if not os.path.isfile(self.__filename):
                print("Error file '%s' dosen't exists" % self.__filename)
            cnf = configparser.ConfigParser()
            cnf.read(self.__filename)
            sections = cnf.sections()
            server = []
            i = 0
            while "consumer_%s" % i in sections:
                options = cnf.options(sections[sections.index("consumer_%s" % i)])
                for option in options:
                    val = cnf.get(sections[sections.index("consumer_%s" % i)], option)
                    server.append(val)
                    print(option)
                self.__receiver.append(tuple(server))
                server = []
                i += 1
        except Exception as exc:
            raise exc
        return tuple(self.__receiver)