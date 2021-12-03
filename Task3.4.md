# Домашнее задание к занятию "3.3. Операционные системы, лекция 1"

1. `chdir("/tmp")`

2. `openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3`

3. Сначала находим PID зависшего процесса командой: `lsof | grep some_file`
Затем перенаправляем в этот процесс пустую строку: `echo '' >/proc/<PID>/fd/3`

4. Зомби-процессы отображаются в таблице процессов, но ресурсы ОС не занимают.

5. `sudo apt update`\
`sudo apt install bpfcc-tools`\
`dpkg -L bpfcc-tools | grep sbin/opensnoop`\
`>/usr/sbin/opensnoop-bpfcc`\
`sudo /usr/sbin/opensnoop-bpfcc`\
PID    COMM               FD ERR PATH\
900    vminfo              6   0 /var/run/utmp\
551    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services\
551    dbus-daemon        18   0 /usr/share/dbus-1/system-services\
551    dbus-daemon        -1   2 /lib/dbus-1/system-services\
551    dbus-daemon        18   0 /var/lib/snapd/dbus-1/system-services/\
900    vminfo              6   0 /var/run/utmp\
551    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services\
551    dbus-daemon        18   0 /usr/share/dbus-1/system-services\
551    dbus-daemon        -1   2 /lib/dbus-1/system-services\
551    dbus-daemon        18   0 /var/lib/snapd/dbus-1/system-services/\
900    vminfo              6   0 /var/run/utmp\
551    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services\
551    dbus-daemon        18   0 /usr/share/dbus-1/system-services\
551    dbus-daemon        -1   2 /lib/dbus-1/system-services\
551    dbus-daemon        18   0 /var/lib/snapd/dbus-1/system-services/

6. Системный вызов `uname()`.
`Part of the utsname information is also accessible  via  /proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}.`

7. `;` - несколько команд последовательно, одну за другой. `&&` - вторая команда будет выполняться, только если первая вернула код успешного завершения.
Если применить `set -e` использовать `&&` не имеет смысла, т.к. команда прервётся после ошибки.

8. `-e` - прекращает выполнение скрипта, если команда завершилась ошибкой
`-u` - прекращает выполнение скрипта, если встретилась несуществующая переменная
`-x` - выводит выполняемые команды во время выполнения
`-o pipefail` - прекращает выполнение скрипта, если одна из частей пайпа завершилась ошибкой
`set -euxo pipefail` - делает скрипт более безопасным, т.к. прерывает скрипт, если есть ошибки во время выполнения сценария и выводит эти сообщения об ошибках. 

9. `Ss` - процессы, ожидающие завершения (спящие)
`R+` - выполняющиеся, фоновые процессы