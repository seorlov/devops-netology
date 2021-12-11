#Домашнее задание к занятию "3.8. Компьютерные сети, лекция 3"

>1. Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP

route-views>show ip route 195.9.250.206  
Routing entry for 195.9.0.0/16, supernet  
  Known via "bgp 6447", distance 20, metric 0  
  Tag 8283, type external  
  Last update from 94.142.247.3 2d04h ago  
  Routing Descriptor Blocks:  
  * 94.142.247.3, from 94.142.247.3, 2d04h ago  
      Route metric is 0, traffic share count is 1  
      AS Hops 3  
      Route tag 8283  
      MPLS label: none  

route-views>show bgp 195.9.250.206  
BGP routing table entry for 195.9.0.0/16, version 1400654000  
Paths: (23 available, best #19, table default)  
  Not advertised to any peer  
  Refresh Epoch 1  
  3549 3356 8359 25513  
    208.51.134.254 from 208.51.134.254 (67.16.168.191)  
      Origin IGP, metric 0, localpref 100, valid, external  
      Community: 0:199 3356:2 3356:22 3356:100 3356:123 3356:507 3356:903 3356:2111 3549:2581 3549:30840 8359:100 8359:5500 8359:55277  
      path 7FE12F843C30 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  57866 3356 8359 25513  
    37.139.139.17 from 37.139.139.17 (37.139.139.17)  
      Origin IGP, metric 0, localpref 100, valid, external  
      Community: 0:199 3356:2 3356:22 3356:100 3356:123 3356:507 3356:903 3356:2111 8359:100 8359:5500 8359:55277  
      path 7FE0D3003170 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  101 3356 8359 25513  
    209.124.176.223 from 209.124.176.223 (209.124.176.223)  
      Origin IGP, localpref 100, valid, external  
      Community: 0:199 101:20100 101:20110 101:22100 3356:2 3356:22 3356:100 3356:123 3356:507 3356:903 3356:2111 8359:100 8359:5500 8359:55277  
      Extended Community: RT:101:22100  
      path 7FE13E0BCCF0 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  53767 14315 6453 6453 3356 8359 25513  
    162.251.163.2 from 162.251.163.2 (162.251.162.3)  
      Origin IGP, localpref 100, valid, external  
      Community: 14315:5000 53767:5000  
      path 7FE1419B13B0 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  20130 6939 8359 25513  
    140.192.8.16 from 140.192.8.16 (140.192.8.16)  
      Origin IGP, localpref 100, valid, external  
      path 7FE177A0A2C8 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  3356 8359 25513  
    4.68.4.46 from 4.68.4.46 (4.69.184.201)  
      Origin IGP, metric 0, localpref 100, valid, external  
      Community: 0:199 3356:2 3356:22 3356:100 3356:123 3356:507 3356:903 3356:2111 8359:100 8359:5500 8359:55277  
      path 7FE0F95D9268 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  3333 8359 25513  
    193.0.0.56 from 193.0.0.56 (193.0.0.56)  
      Origin IGP, localpref 100, valid, external  
      Community: 0:199 8359:100 8359:5500 8359:55277  
      path 7FDFFD1459C8 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  852 3356 8359 25513  
    154.11.12.212 from 154.11.12.212 (96.1.209.43)  
      Origin IGP, metric 0, localpref 100, valid, external  
      path 7FE16EBB6080 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  2497 3356 8359 25513  
    202.232.0.2 from 202.232.0.2 (58.138.96.254)  
      Origin IGP, localpref 100, valid, external  
      path 7FE0EF49C700 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  6939 8359 25513  
    64.71.137.241 from 64.71.137.241 (216.218.252.164)  
      Origin IGP, localpref 100, valid, external  
      path 7FE14B23FFD8 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  20912 3257 3356 8359 25513  
    212.66.96.126 from 212.66.96.126 (212.66.96.126)  
      Origin IGP, localpref 100, valid, external  
      Community: 3257:8070 3257:30515 3257:50001 3257:53900 3257:53902 20912:65004  
      path 7FE0F8027EC0 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 3  
  3303 8359 25513  
    217.192.89.50 from 217.192.89.50 (138.187.128.158)  
      Origin IGP, localpref 100, valid, external  
      Community: 0:199 3303:1004 3303:1006 3303:1030 3303:3054 8359:100 8359:5500 8359:55277  
      path 7FE0C36BFB60 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  4901 6079 8359 25513  
    162.250.137.254 from 162.250.137.254 (162.250.137.254)  
      Origin IGP, localpref 100, valid, external  
      Community: 65000:10100 65000:10300 65000:10400  
      path 7FE0B5F09018 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  7660 2516 1299 8359 25513  
    203.181.248.168 from 203.181.248.168 (203.181.248.168)  
      Origin IGP, localpref 100, valid, external  
      Community: 2516:1030 7660:9003  
      path 7FE16F8F1D08 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  7018 3356 8359 25513  
    12.0.1.63 from 12.0.1.63 (12.0.1.63)  
      Origin IGP, localpref 100, valid, external  
      Community: 7018:5000 7018:37232  
      path 7FE07D976AB0 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  3561 3910 3356 8359 25513  
    206.24.210.80 from 206.24.210.80 (206.24.210.80)  
      Origin IGP, localpref 100, valid, external  
      path 7FE15BEB1F20 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  3257 3356 8359 25513  
    89.149.178.10 from 89.149.178.10 (213.200.83.26)  
      Origin IGP, metric 10, localpref 100, valid, external  
      Community: 3257:8794 3257:30043 3257:50001 3257:54900 3257:54901  
      path 7FE1834B5D68 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  49788 12552 8359 25513  
    91.218.184.60 from 91.218.184.60 (91.218.184.60)  
      Origin IGP, localpref 100, valid, external  
      Community: 12552:12000 12552:12100 12552:12101 12552:22000  
      Extended Community: 0x43:100:1  
      path 7FE0FC0C72D0 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  8283 8359 25513  
    94.142.247.3 from 94.142.247.3 (94.142.247.3)  
      Origin IGP, metric 0, localpref 100, valid, external, best  
      Community: 0:199 8283:1 8283:101 8359:100 8359:5500 8359:55277  
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x18  
        value 0000 205B 0000 0000 0000 0001 0000 205B  
              0000 0005 0000 0001  
      path 7FE105459870 RPKI State not found  
      rx pathid: 0, tx pathid: 0x0  
  Refresh Epoch 1  
  1221 4637 3356 8359 25513  
    203.62.252.83 from 203.62.252.83 (203.62.252.83)  
      Origin IGP, localpref 100, valid, external  
      path 7FE164D89388 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  701 3356 8359 25513  
    137.39.3.55 from 137.39.3.55 (137.39.3.55)  
      Origin IGP, localpref 100, valid, external  
      path 7FE0351E4A68 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  1351 8359 25513  
    132.198.255.253 from 132.198.255.253 (132.198.255.253)  
      Origin IGP, localpref 100, valid, external  
      path 7FE0E51A69F8 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  Refresh Epoch 1  
  19214 3257 3356 8359 25513  
    208.74.64.40 from 208.74.64.40 (208.74.64.40)  
      Origin IGP, localpref 100, valid, external  
      Community: 3257:8108 3257:30048 3257:50002 3257:51200 3257:51203  
      path 7FE00ADFE728 RPKI State not found  
      rx pathid: 0, tx pathid: 0  
  
>2. Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.

vagrant@vagrant:~$ sudo echo "dummy" >> sudo /etc/modules  
vagrant@vagrant:~$ sudo echo "options dummy numdummies=2" > sudo /etc/modprobe.d/dummy.conf  
vagrant@vagrant:~$ sudo vim /etc/network/interfaces  

auto dummy0  
iface dummy0 inet static  
 address 10.2.2.2/32  
 pre-up ip link add dummy0 type dummy  
 post-down ip link del dummy0  

vagrant@vagrant:~$ sudo ip route add 10.2.2.0/32 dev eth0  
vagrant@vagrant:~$ sudo ip route add 10.2.3.0/32 dev eth0
vagrant@vagrant:~$ sudo ip route show 10.2.2.0/32  
10.2.2.0 dev eth0 scope link  
vagrant@vagrant:~$ cat /etc/iproute2/rt_tables  
  
reserved values  
  
255     local  
254     main  
253     default  
0       unspec  
  
 local  
  
1      inr.ruhep  
  


>3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.

vagrant@vagrant:~$ ss -ltn  
State         Recv-Q        Send-Q               Local Address:Port               Peer Address:Port       Process  
LISTEN        0             4096                       0.0.0.0:111                     0.0.0.0:*  
LISTEN        0             4096                 127.0.0.53%lo:53                      0.0.0.0:*  
LISTEN        0             128                        0.0.0.0:22                      0.0.0.0:*  

111 порт - RPC Portmapper служит для обеспечения сервисов Remote Procedure Call, таких как NIS и NFS.    
53 порт - служба DNS  
22 порт - SSH для подключения к хосту  

>4. Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?

vagrant@vagrant:~$ ss -lun  
State        Recv-Q        Send-Q                Local Address:Port               Peer Address:Port       Process  
UNCONN       0             0                     127.0.0.53%lo:53                      0.0.0.0:*  
UNCONN       0             0                    10.0.2.15%eth0:68                      0.0.0.0:*  
UNCONN       0             0                           0.0.0.0:111                     0.0.0.0:*  

111 и 53 - уже были в TCP  
68 порт - BOOTPC (Bootstrap Protocol Client) — для клиентов бездисковых рабочих станций, загружающихся с сервера BOOTP; также используется DHCP (Dynamic Host Configuration Protocol)  


>5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.

https://github.com/seorlov/devops-netology/blob/main/Untitled%20Diagram.drawio  
