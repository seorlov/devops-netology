# Домашнее задание к занятию "3.4. Операционные системы, лекция 2"
1. vagrant@vagrant:/etc/systemd/system$ ps -e |grep node_exporter  
  12594 ?        00:00:00 node_exporter
vagrant@vagrant:/etc/systemd/system$ systemctl stop node_exporter
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to stop 'node_exporter.service'.
Authenticating as: vagrant,,, (vagrant)
Password: 
==== AUTHENTICATION COMPLETE ===
vagrant@vagrant:/etc/systemd/system$ ps -e |grep node_exporter  
vagrant@vagrant:/etc/systemd/system$ systemctl start node_exporter
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to start 'node_exporter.service'.
Authenticating as: vagrant,,, (vagrant)
Password: 
==== AUTHENTICATION COMPLETE ===
vagrant@vagrant:/etc/systemd/system$ ps -e |grep node_exporter  
  12707 ?        00:00:00 node_exporter

Сервис:
vagrant@vagrant:/etc/systemd/system$ cat /etc/systemd/system/node_exporter.service
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=vagrant
Group=vagrant
Type=simple
ExecStart=/usr/local/bin/node_exporter
EnvironmentFile=/etc/default/node_exporter

[Install]
WantedBy=multi-user.target

Переменная окружения
vagrant@vagrant:/etc/default$ sudo cat /proc/12914/environ 
LANG=en_US.UTF-8LANGUAGE=en_US:PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/binHOME=/home/vagrantLOGNAME=vagrantUSER=vagrantSHELL=/bin/bashINVOCATION_ID=2076e5eb3c64480985a09438e92520ebJOURNAL_STREAM=9:41650vagrant@vagrant:/etc/default$




2.
node_cpu_seconds_total{cpu="0",mode="idle"} 3251.81
node_cpu_seconds_total{cpu="0",mode="iowait"} 5.96
node_cpu_seconds_total{cpu="0",mode="irq"} 0
node_cpu_seconds_total{cpu="0",mode="nice"} 12.42
node_cpu_seconds_total{cpu="0",mode="softirq"} 7.5
node_cpu_seconds_total{cpu="0",mode="steal"} 0
node_cpu_seconds_total{cpu="0",mode="system"} 67.54
node_cpu_seconds_total{cpu="0",mode="user"} 6.39

# HELP node_disk_io_time_seconds_total Total seconds spent doing I/Os.
# TYPE node_disk_io_time_seconds_total counter
node_disk_io_time_seconds_total{device="dm-0"} 54.424
node_disk_io_time_seconds_total{device="dm-1"} 0.46
node_disk_io_time_seconds_total{device="sda"} 55.58
# HELP node_disk_read_bytes_total The total number of bytes read successfully.
# TYPE node_disk_read_bytes_total counter
node_disk_read_bytes_total{device="dm-0"} 3.5654144e+08
node_disk_read_bytes_total{device="dm-1"} 3.342336e+06
node_disk_read_bytes_total{device="sda"} 3.70340864e+08
# HELP node_disk_read_time_seconds_total The total number of seconds spent by all reads.
# TYPE node_disk_read_time_seconds_total counter
node_disk_read_time_seconds_total{device="dm-0"} 44.212
node_disk_read_time_seconds_total{device="dm-1"} 0.452
node_disk_read_time_seconds_total{device="sda"} 29.505

# HELP node_memory_MemAvailable_bytes Memory information field MemAvailable_bytes.
# TYPE node_memory_MemAvailable_bytes gauge
node_memory_MemAvailable_bytes 7.45787392e+08
# HELP node_memory_MemFree_bytes Memory information field MemFree_bytes.
# TYPE node_memory_MemFree_bytes gauge
node_memory_MemFree_bytes 3.44559616e+08
# HELP node_memory_MemTotal_bytes Memory information field MemTotal_bytes.
# TYPE node_memory_MemTotal_bytes gauge
node_memory_MemTotal_bytes 1.028694016e+09

# HELP node_network_receive_bytes_total Network device statistic receive_bytes.
# TYPE node_network_receive_bytes_total counter
node_network_receive_bytes_total{device="eth0"} 9.665855e+06
node_network_receive_bytes_total{device="lo"} 237886
# HELP node_network_receive_compressed_total Network device statistic receive_compressed.
# TYPE node_network_receive_compressed_total counter
node_network_receive_compressed_total{device="eth0"} 0
node_network_receive_compressed_total{device="lo"} 0
# HELP node_network_receive_drop_total Network device statistic receive_drop.
# TYPE node_network_receive_drop_total counter
node_network_receive_drop_total{device="eth0"} 0
node_network_receive_drop_total{device="lo"} 0
# HELP node_network_receive_errs_total Network device statistic receive_errs.
# TYPE node_network_receive_errs_total counter
node_network_receive_errs_total{device="eth0"} 0
node_network_receive_errs_total{device="lo"} 0



3. https://github.com/seorlov/devops-netology/blob/main/Task3.4.3.jpg

4. vagrant@vagrant:~$ dmesg | grep -i virtual
[    0.000000] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
[    0.015067] CPU MTRRs all blank - virtualized system.
[    0.121789] Booting paravirtualized kernel on KVM
[   23.419319] systemd[1]: Detected virtualization oracle.


5. vagrant@vagrant:~$ sysctl -n fs.nr_open
1048576
Лимит на кол-во открытых дескрипторов

ulimit -n	the maximum number of open file descriptors

6. В одном терминале выполнил:
root@vagrant:/# unshare -f --pid --mount-proc sleep 2m
А в другом:
root@vagrant:/# ps -e | grep sleep
  15478 pts/1    00:00:00 sleep
root@vagrant:/# nsenter --target 15478 --mount --uts --ipc --net --pid ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   8076   520 pts/1    S+   05:13   0:00 sleep 2m
root           2  0.0  0.3  11492  3324 pts/2    R+   05:13   0:00 ps aux

7. на bash'e запускает очень много шелов
это что-то типа fork-bomb

root@vagrant:/# dmesg | grep fork
[ 2170.377660] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-4.scope

limit -u	the maximum number of user processes
Например limit -u 10 - будет 10 процессов на пользователя