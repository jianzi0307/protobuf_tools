#!/usr/bin/python
# -*- coding:utf-8 -*-

import ConfigParser as parser
import sys,os

#获取脚本文件的当前路径
def curr_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def exec_command():
    runPrefix = ""

if __name__ == '__main__':
    curr_path = curr_dir()
    config = parser.ConfigParser()
    config.readfp(open('config.ini'))
    proto_home_path = config.get('default', 'proto_home_path')
    java_output_path = config.get('default', 'java_output_path')
    csharp_output_path = config.get('default', 'csharp_output_path')




