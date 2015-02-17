#!/usr/bin/python2.7
# -*- coding: utf-8 -*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import os

LIB_PATH = os.path.dirname(os.path.abspath(__file__)) + "/lib"
CONFIG_PATH = os.path.dirname(os.path.abspath(__file__)) + "/config"
sys.path.append(LIB_PATH)
sys.path.append(CONFIG_PATH)


import bottle

import json 

bottle.debug(True)


import functools

from bottle import get, post, route,run, jinja2_view,static_file,request

view = functools.partial(jinja2_view, template_lookup=['templates'])


import smart_config 

import logging.config
logging.config.fileConfig(CONFIG_PATH + "/logger.conf")
logger = logging.getLogger()
from  datetime  import *

import Util 

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')


@get('/')
@view('index.html')
def get_luck():
    luck_type = request.query.get('luck_type') or 'first'
    data = {}
    count = 0
    luck = {"first":10,"second":20,"third":30}
    count = luck[luck_type]


    return {
        "count" : count,
        "total" : 100,
    }

@get('/test')
@view('test.html')
def test():
    return {}

@post('/luck')
def post_luck():
    pass




run(host=smart_config.WEB["listen"]["address"], port=smart_config.WEB["listen"]["port"],reloader=True)
