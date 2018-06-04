#!/usr/bin/env python
#coding:utf-8
#__time__: 2018/5/31 18:02
#__author__ = 'ren_mcc'

import sys
from bypy import ByPy
import requests
requests.packages.urllib3.disable_warnings()


def yunpan(upload_dir, build_count):
    pattren = '(.*-{}.apk|.*-signed.apk)'.format(build_count)
    bp = ByPy(configdir='C:\\Users\\Administrator\\.bypy', processes=5, incregex=pattren)
    #显示网盘使用信息
    bp.info()
    #显示上传日志信息
    bp.verbose = True
    #同步上传
    bp.syncup(localdir =upload_dir, remotedir = build_count)
    #打印云盘目录
    bp.ls(build_count)
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception('argument count error')
    workspace = sys.argv[1]
    build_count = sys.argv[2]
    upload = sys.argv[3]

    if upload == 'true':        
        upload_dir = '{}\\{}'.format(workspace, build_count)
        yunpan(upload_dir, build_count)



