# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\\t",
        "elements" : [
            { "name" : "first",
            "type" : "server",
            "ip" : "7175" 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import socket
import time
import json
import yaml

service_names={"drive.google.com": "74.125.131.194","mail.google.com": "64.233.165.83","google.com": "64.233.163.138"}
while(True):
    for k, v in service_names.items():
        host_ip=socket.gethostbyname(k)
        print(k, "-", v)
        if host_ip!=v:
            print ("[ERROR]", k, "IP mismatch:", v, host_ip)
            service_names[k]=host_ip
        with open("services.json", 'w') as js1:
            js1.write(json.dumps(service_names))
        with open("services.yaml", 'w') as ym1:
            ym1.write(yaml.dump(service_names))
    time.sleep(1)
```

### Вывод скрипта при запуске при тестировании:
```
PS C:\Users\Eflvby\netology\sysadm-homeworks> python Task4.3.2.py             
drive.google.com - 74.125.131.194
mail.google.com - 64.233.165.83
[ERROR] mail.google.com IP mismatch: 64.233.165.83 64.233.165.18
google.com - 64.233.163.138
[ERROR] google.com IP mismatch: 64.233.163.138 74.125.131.102
drive.google.com - 74.125.131.194
mail.google.com - 64.233.165.18
google.com - 74.125.131.102
drive.google.com - 74.125.131.194
...
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{"drive.google.com": "74.125.131.194", "mail.google.com": "64.233.165.18", "google.com": "74.125.131.102"}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
drive.google.com: 74.125.131.194
google.com: 74.125.131.102
mail.google.com: 64.233.165.18
```

