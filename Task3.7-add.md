
#Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"
##Доработка 4 и 5  

>Задание 4. Тип агрегации немного больше чем два. Уточните?

Linux поддерживает несколько типов агрегации интерфейсов:  
  
0 (balance-rr) — round-robin распределение пакетов между интерфейсами. Обеспечивает отказоустойчивость и повышение пропускной способности.  
1 (active-backup) — в каждый момент времени работает только один интерфейс, в случае его выхода из строя, mac-адрес назначается второму интерфейсу и трафик переключается на него.  
2 (balance-xor) — обеспечивает балансировку между интерфейсами на основании MAC-адресов отправителя и получателя.  
3 (broadcast) — отправляет пакеты через все интерфейсы одновременно, обеспечивает отказоустойчивость.  
4 (802.3ad) — обеспечивает агрегацию на основании протокола 802.3ad.  
5 (balance-tlb) — в этом режиме входящий трафик приходит только на один «активный» интерфейс, исходящий же распределяется по всем интерфейсам.  
6 (balance-alb) — балансирует исходящий трафик как tlb, а так же входящий IPv4 трафик используя ARP.  
  


>5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.  
>Задание 5. Покажите расчеты  

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

8 IP-адресов в сети с маской /29 (6 хостовых)  

vagrant@vagrant:~$ ipcalc 10.10.10.0/24  
Address:   10.10.10.0           00001010.00001010.00001010. 00000000  
Netmask:   255.255.255.0 = 24   11111111.11111111.11111111. 00000000  
Wildcard:  0.0.0.255            00000000.00000000.00000000. 11111111  
=>  
Network:   10.10.10.0/24        00001010.00001010.00001010. 00000000  
HostMin:   10.10.10.1           00001010.00001010.00001010. 00000001  
HostMax:   10.10.10.254         00001010.00001010.00001010. 11111110  
Broadcast: 10.10.10.255         00001010.00001010.00001010. 11111111  
Hosts/Net: 254                   Class A, Private Internet  

256 IP-адресов в сети с маской /24  
256/8=32 - 32 подсети в сети с маской /24

Примеры сетей:   
Network:   10.10.10.0/29         00001010.00001010.00001010.00000 000 (Class A)  
Broadcast: 10.10.10.7            00001010.00001010.00001010.00000 111  
HostMin:   10.10.10.1            00001010.00001010.00001010.00000 001  
HostMax:   10.10.10.6            00001010.00001010.00001010.00000 110  
Hosts/Net: 6                     (Private Internet)  
  
  
Network:   10.10.10.8/29         00001010.00001010.00001010.00001 000 (Class A)  
Broadcast: 10.10.10.15           00001010.00001010.00001010.00001 111  
HostMin:   10.10.10.9            00001010.00001010.00001010.00001 001  
HostMax:   10.10.10.14           00001010.00001010.00001010.00001 110  
Hosts/Net: 6                     (Private Internet)  
  
  
Network:   10.10.10.16/29        00001010.00001010.00001010.00010 000 (Class A)  
Broadcast: 10.10.10.23           00001010.00001010.00001010.00010 111  
HostMin:   10.10.10.17           00001010.00001010.00001010.00010 001  
HostMax:   10.10.10.22           00001010.00001010.00001010.00010 110  
Hosts/Net: 6                     (Private Internet)  




