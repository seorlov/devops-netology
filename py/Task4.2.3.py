#!/usr/bin/env python3

import os
import sys
#try:
    args[1]=="None"
    args=sys.argv
    if args[1]=="None":
        bash_command = ["git status"]
        print("one")
    else:
        bash_command = ["cd "+args[1], "git status"]
        print("two")
    result_os = os.popen(' && '.join(bash_command)).read()
    is_change = False
    for result in result_os.split('\n'):
        if result.find('modified') != -1:
            prepare_result = "%USERPROFILE%/netology/sysadm-homeworks/"+result.replace('\tmodified:   ', '')
            print(prepare_result)
#except:
 #   print("Ошибка. Указанный каталог не является git-репозиторием")
