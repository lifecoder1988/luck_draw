#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import MySQLdb.cursors

SMART_HOME_SOURCE = "local"
SMART_SAMPLE_SOURCE = "local"
WEB_SMART_SAMPLE_SOURCE = "web_local"

WEB = { 
    "listen" : { 
        "address" : "localhost",
        "port" : 8081
    }
}

DBCONFIG = {
    "local" : {
        "host" : "localhost",
        "user" : "root",
        "passwd" : "123456",
        "port" : 3306,
        "db" : "test",
        "charset" : "utf8"
    },
    "web_local" : {
        "host" : "localhost",
        "user" : "root",
        "passwd" : "123456",
        "port" : 3306,
        "db" : "test",
        "charset" : "utf8",
        "cursorclass" :MySQLdb.cursors.DictCursor
    },
}
