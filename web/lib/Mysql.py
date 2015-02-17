#!/usr/bin/python2.7

import MySQLdb

class Mysql:
    def __init__(self,dbconfig):
        self.conn = None
        self.dbconfig = dbconfig

    def getConnection(self):
        if self.conn:
            return self.conn
        self.conn = MySQLdb.connect(**self.dbconfig)
        return self.conn
    def query(self,sql):
        try:
            cursor = self.getConnection().cursor()
            cursor.execute(sql)
            self.getConnection().commit()
        except Exception,e:
            self.conn = None
            cursor = self.getConnection().cursor()
            cursor.execute(sql)
            self.getConnection().commit()
        return cursor
