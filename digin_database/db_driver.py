# -*- coding: utf-8 -*-
"""
Created on Apr 20, 2012

@author: timekeeper
"""
import pymysql as mysql
import warnings

warnings.filterwarnings("ignore", category=mysql.Warning)


class DbDriver(object):
    """
    Getting from DB some specific infos for digin_* project
    """
    __db_conn = None

    def __init__(self, con_param):
        """
        Constructor
        """
        self.__db_conn = self.__init_connect(con_param)

    def __del__(self):
        """
        Destructor
        """
        if self.__db_conn is not None:
            self.__db_conn.close()

    def __init_connect(self, con_param):
        """
        Initiate connection to Mysql
        """
        self.__connection_param = con_param
        db_connect = self.__connection()
        return db_connect

    def __connection(self):
        """
        Create connection to Mysql
        """
        try:
            db_connect = mysql.connect(self.__connection_param['host'],
                                       self.__connection_param['user'],
                                       self.__connection_param['password'],
                                       self.__connection_param['dbname'],
                                       charset='utf8')
            db_connect.autocommit(1)
        except mysql.Error as e:
            raise e
        return db_connect

    @staticmethod
    def escape_string(st):
        return mysql.escape_string(st)

    def execute(self, sql_query, param=None):
        """
        Executing query from DB and return result set and description set
        return result, desc, rows
        """
        try:
            cursor = self.__db_conn.cursor()
            cursor.execute(sql_query, param)
            self.__db_conn.commit()
            result = cursor.fetchall()
            desc = cursor.description
            rows = cursor.rowcount

        except mysql.Warning:
            # noinspection PyShadowingNames
            result = []
            pass
        except mysql.OperationalError:
            # если произошла потеря соединения с Mysql
            self.__db_conn = self.__connection()
            cursor = self.__db_conn.cursor()
            cursor.execute(sql_query, param)
            self.__db_conn.commit()
            result = cursor.fetchall()
            desc = cursor.description
            rows = cursor.rowcount
        except mysql.Error as e:
            self.__db_conn.rollback()
            raise e
        return result, desc, rows
