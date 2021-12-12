
#Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"

>1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?

vagrant@vagrant:~$ ip -c -br link  
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>  
eth0             UP             08:00:27:73:60:cf <BROADCAST,MULTICAST,UP,LOWER_UP>  

C:\Users\Eflvby>ipconfig  

Настройка протокола IP для Windows  


Адаптер Ethernet Ethernet 3:  

   Состояние среды. . . . . . . . : Среда передачи недоступна.  
   DNS-суффикс подключения . . . . . :  

Адаптер Ethernet Ethernet:  

   DNS-суффикс подключения . . . . . :  
   Локальный IPv6-адрес канала . . . : fe80::11d3:5951:9768:a2a8%12  
   IPv4-адрес. . . . . . . . . . . . : 192.168.0.113  
   Маска подсети . . . . . . . . . . : 255.255.255.0  
   Основной шлюз. . . . . . . . . : 192.168.0.21  

Адаптер Ethernet VirtualBox Host-Only Network:  

   DNS-суффикс подключения . . . . . :  
   Локальный IPv6-адрес канала . . . : fe80::b982:aaf4:264d:ab40%9  
   IPv4-адрес. . . . . . . . . . . . : 192.168.56.1  
   Маска подсети . . . . . . . . . . : 255.255.255.0  
   Основной шлюз. . . . . . . . . :  

Адаптер Ethernet Ethernet 2:  

   Состояние среды. . . . . . . . : Среда передачи недоступна.  
   DNS-суффикс подключения . . . . . :  


>2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?

vagrant@vagrant:~$ sudo apt install lldpd  
vagrant@vagrant:~$ sudo systemctl enable lldpd && sudo systemctl start lldpd  
vagrant@vagrant:~$ lldpctl    
   
LLDP neighbors:

Соседей нет.

>3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.

Технология VLAN

vagrant@vagrant:~$ sudo apt install vlan

vagrant@vagrant:~$ sudo vi /etc/network/interfaces  

auto eth0.1400  
iface eth0.1400 inet static  
        address 192.168.1.1  
        netmask 255.255.255.0  
        vlan_raw_device eth0  

>4. Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.

Типы агрегации:  
● статический (на Cisco mode on);  
● динамический – LACP протокол (на Cisco mode active).  

Опции: modprobe bonding

Пример конфига:  
auto bond0  

iface bond0 inet static  
    address 10.31.1.5  
    netmask 255.255.255.0  
    network 10.31.1.0  
    gateway 10.31.1.254  
    bond-slaves eth0 eth1  
    bond-mode active-backup  
    bond-miimon 100  
    bond-downdelay 200  
    bond-updelay 200  

>5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.

6 IP адресов  

42 подсети

vagrant@vagrant:~$ ipcalc 10.10.10.0/29  
Address:   10.10.10.0           00001010.00001010.00001010.00000 000  
Netmask:   255.255.255.248 = 29 11111111.11111111.11111111.11111 000  
Wildcard:  0.0.0.7              00000000.00000000.00000000.00000 111  
=>  
Network:   10.10.10.0/29        00001010.00001010.00001010.00000 000  
HostMin:   10.10.10.1           00001010.00001010.00001010.00000 001  
HostMax:   10.10.10.6           00001010.00001010.00001010.00000 110  
Broadcast: 10.10.10.7           00001010.00001010.00001010.00000 111  
Hosts/Net: 6                     Class A, Private Internet  

vagrant@vagrant:~$ ipcalc 10.10.10.8/29  
Address:   10.10.10.8           00001010.00001010.00001010.00001 000  
Netmask:   255.255.255.248 = 29 11111111.11111111.11111111.11111 000  
Wildcard:  0.0.0.7              00000000.00000000.00000000.00000 111  
=>  
Network:   10.10.10.8/29        00001010.00001010.00001010.00001 000  
HostMin:   10.10.10.9           00001010.00001010.00001010.00001 001  
HostMax:   10.10.10.14          00001010.00001010.00001010.00001 110  
Broadcast: 10.10.10.15          00001010.00001010.00001010.00001 111  
Hosts/Net: 6                     Class A, Private Internet  

>6. Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.

Можно взять из подсети 100.64.0.0 — 100.127.255.255 (маска подсети: 255.192.0.0 или /10)  
Например 100.64.0.0/26

>7. Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?

В Linux:  
$ arp -a  
  
Interface: 192.168.56.1 --- 0x9  
  Internet Address      Physical Address      Type  
  192.168.56.255        ff-ff-ff-ff-ff-ff     static  
  224.0.0.2             01-00-5e-00-00-02     static  
  224.0.0.22            01-00-5e-00-00-16     static  
  224.0.0.251           01-00-5e-00-00-fb     static  
  224.0.0.252           01-00-5e-00-00-fc     static  
  239.255.255.250       01-00-5e-7f-ff-fa     static  
  255.255.255.255       ff-ff-ff-ff-ff-ff     static  
  
В Windows:  
C:\Users\Eflvby>arp -a  

Интерфейс: 192.168.56.1 --- 0x9  
  адрес в Интернете      Физический адрес      Тип  
  192.168.56.255        ff-ff-ff-ff-ff-ff     статический  
  224.0.0.2             01-00-5e-00-00-02     статический  
  224.0.0.22            01-00-5e-00-00-16     статический  
  224.0.0.251           01-00-5e-00-00-fb     статический  
  224.0.0.252           01-00-5e-00-00-fc     статический  
  239.255.255.250       01-00-5e-7f-ff-fa     статический  
  255.255.255.255       ff-ff-ff-ff-ff-ff     статический  
  
Кэш очищается командой: arp -d  

Удалить конкретный адрес можно командой: arp -d <IP-адрес>
