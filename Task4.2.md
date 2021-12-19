# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательная задача 1

Есть скрипт:
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:
| Вопрос  | Ответ |
| ------------- | ------------- |
| Какое значение будет присвоено переменной `c`?  | будет ошибка из-за сложения разнотипных переменных  |
| Как получить для переменной `c` значение 12?  | с=str(a)+b  |
| Как получить для переменной `c` значение 3?  | c=a+int(b)  |

## Обязательная задача 2
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = "~/netology/sysadm-homeworks/"+result.replace('\tmodified:   ', '')
        print(prepare_result)
```

### Вывод скрипта при запуске при тестировании:
```
~/netology/sysadm-homeworks/test/test3.txt
~/netology/sysadm-homeworks/test1.txt
~/netology/sysadm-homeworks/test2.txt
```

## Обязательная задача 3
1. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os
import sys

args=sys.argv
if len(args)==1:
    bash_command = ["git status"]
else:
    bash_command = ["cd "+args[1], "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = args[1]+"/"+result.replace('\tmodified:   ', '')
        print(prepare_result)
```

### Вывод скрипта при запуске при тестировании:
```
PS C:\users\eflvby\netology> python sysadm-homeworks\Task4.2.3.py c:/users/eflvby/netology/sysadm-homeworks
c:/users/eflvby/netology/sysadm-homeworks/test/test3.txt
c:/users/eflvby/netology/sysadm-homeworks/test1.txt
c:/users/eflvby/netology/sysadm-homeworks/test2.txt

PS C:\users\eflvby\netology> python sysadm-homeworks\Task4.2.3.py
fatal: not a git repository (or any of the parent directories): .git

PS C:\users\eflvby\netology> 
```

## Обязательная задача 4
1. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import socket
import time
sevrice_names=["drive.google.com", "mail.google.com", "google.com"]
service_ip=["74.125.131.194","64.233.165.83","64.233.163.138"]
while (1==1):
    iter=0
    for serv_name in sevrice_names:
        if iter>2:
            iter=0
        host_ip=socket.gethostbyname(serv_name)
        print(host_ip)
        if host_ip!=service_ip[iter]:
            print ("[ERROR] "+serv_name+" IP mismatch: "+service_ip[iter]+" "+host_ip)
            service_ip[iter]=host_ip
        iter+=1
    time.sleep(1)
```

### Вывод скрипта при запуске при тестировании:
```
PS C:\users\eflvby\netology> python sysadm-homeworks\Task4.2.4.py
74.125.131.194
64.233.164.19
[ERROR] mail.google.com IP mismatch: 64.233.165.83 64.233.164.19
64.233.163.102
[ERROR] google.com IP mismatch: 64.233.163.138 64.233.163.102
74.125.131.194
64.233.164.19
64.233.163.102
.................
173.194.222.194
64.233.164.19
64.233.163.102
173.194.222.194
64.233.164.19
64.233.161.102
[ERROR] google.com IP mismatch: 64.233.163.102 64.233.161.102
173.194.222.194
64.233.164.19
64.233.161.102
173.194.222.194
64.233.164.19
```

