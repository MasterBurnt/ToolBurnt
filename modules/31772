#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : SystemInfo
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt

import platform, getpass, multiprocessing, struct,time,sys

def __start__():
    print(f"""
-== User       : {getpass.getuser()}
-== Cpu        : {multiprocessing.cpu_count()}
-== Network    : {platform.node()}
-== Machine    : {platform.machine()}
-== Platform   : {platform.platform()}
-== Shell      : {struct.calcsize("P") * 8}-bit
-== System     : {platform.system()}
-== Release    : {platform.release()}
-== Version    : {platform.version()}
""")

