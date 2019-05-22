#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

player = '/usr/bin/mpg123'
file_dir = os.path.split(os.path.abspath(__file__))[0]


def get_ip_str():
    cmd = "ifconfig|grep inet|grep -v inet6|awk '{print $2}'|grep -v 127"
    with os.popen(cmd) as f:
        content = f.read()
    ip_list = content.strip().split()
    ip_str = ('s' + 'e'.join(ip_list) + 'e').replace('.','d')
    return ip_str

def speak_ch(ch):
    filename = os.path.join(file_dir, ch + '.mp3')
    cmd = player + ' ' + filename + ' 1>/dev/null 2>1'
    os.system(cmd)
    
if __name__ == '__main__':
    ip_str = get_ip_str()
    for ch in ip_str:
        speak_ch(ch)
