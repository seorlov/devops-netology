#Домашнее задание к занятию "3.9. Элементы безопасности информационных систем"

>1. Установите Bitwarden плагин для браузера. Зарегестрируйтесь и сохраните несколько паролей.  

https://github.com/seorlov/devops-netology/blob/main/Task3.9.png  

>2. Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.

Давно пользуюсь Microsoft authenticator. На скриншоте запос кода из Bitwarden. Microsoft authenticator скриншоты делать не позволяет:    
https://github.com/seorlov/devops-netology/blob/main/Task3.9.2.png


>3. Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS.

vagrant@vagrant:~$ sudo apt install apache2  
vagrant@vagrant:~$ sudo a2enmod ssl  
vagrant@vagrant:~$ sudo systemctl restart apache2  
vagrant@vagrant:~$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \  
 -keyout /etc/ssl/private/apache-selfsigned.key \
-out /etc/ssl/certs/apache-selfsigned.crt \  
 -subj "/C=RU/ST=Moscow/L=Moscow/O=Company Name/OU=Org/CN=localhost"    
Generating a RSA private key  
.................................................................+++++  
.+++++  
writing new private key to '/etc/ssl/private/apache-selfsigned.key'  
-----    
vagrant@vagrant:/var/www$ sudo mkdir serg    
vagrant@vagrant:/var/www$ cd serg  
vagrant@vagrant:/var/www/serg$ sudo vim index.html  
  `<h1>it worked!</h1>`    
vagrant@vagrant:/var/www/serg$ sudo a2ensite serg.conf  
Enabling site serg.  
To activate the new configuration, you need to run:  
  systemctl reload apache2  
vagrant@vagrant:/var/www/serg$ sudo apache2ctl configtest  
Syntax OK  
vagrant@vagrant:/var/www/serg$ sudo systemctl reload apache2  

> 4. Проверьте на TLS уязвимости произвольный сайт в интернете (кроме сайтов МВД, ФСБ, МинОбр, НацБанк, РосКосмос, РосАтом, РосНАНО и любых госкомпаний, объектов КИИ, ВПК ... и тому подобное).

vagrant@vagrant:/$ sudo git clone --depth 1 https://github.com/drwetter/testssl.sh.git  
Cloning into 'testssl.sh'...  
vagrant@vagrant:/$ cd testssl.sh  
vagrant@vagrant:/testssl.sh$ ./testssl.sh -e --fast --parallel https://www.google.com/  

testssl.sh       3.1dev from https://testssl.sh/dev/  
(6da72bc 2021-12-10 20:16:28 -- )  
..................  

> 5. Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.



> 6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.



>7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.


