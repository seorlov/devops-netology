# Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"

>1. Работа c HTTP через телнет.  
В ответе укажите полученный HTTP код, что он означает?

HTTP/1.1 301 Moved Permanently    
cache-control: no-cache, no-store, must-revalidate      
location: https://stackoverflow.com/questions  
x-request-guid: 62e4287c-8cfd-49ad-9097-763341001e1a    
feature-policy: microphone 'none'; speaker 'none'  
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com      
Accept-Ranges: bytes  
Date: Wed, 08 Dec 2021 19:32:53 GMT    
Via: 1.1 varnish  
Connection: close    
X-Served-By: cache-fra19126-FRA    
X-Cache: MISS    
X-Cache-Hits: 0    
X-Timer: S1638991973.294571,VS0,VE92    
Vary: Fastly-SSL  
X-DNS-Prefetch-Control: off    
Set-Cookie: prov=ebf4a135-a81a-ac5d-8087-688622c0573d; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly    
Connection closed by foreign host.  

Ответ означает, что запрашиваемый сайт находится по другому адресу, настроен редирект. В данном случае на зашифрованную страницу по протоколу HTTPS


>2. Повторите задание 1 в браузере, используя консоль разработчика F12.  
укажите в ответе полученный HTTP код.

Ответ сайта в браузере тот же:    
Request URL: http://stackoverflow.com/  
Request Method: GET  
Status Code: 307 Internal Redirect  
Referrer Policy: strict-origin-when-cross-origin  
Location: https://stackoverflow.com/  
Non-Authoritative-Reason: HSTS  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9  
Upgrade-Insecure-Requests: 1  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36  

>>проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?

Страница загрузилась за 794 ms. Дольше всего загружалась главная страница после редиректа на https-страницу

>>приложите скриншот консоли браузера в ответ.

![Скриншот](https://github.com/seorlov/devops-netology/blob/main/Task3.6.2.png "Скриншот")

>3. Какой IP адрес у вас в интернете?

195.9.250.206

>4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois

vagrant@vagrant:~$ whois 195.9.250.206  
......  
descr:          Moscow Local Telephone Network (OAO MGTS)  
origin:         AS25513  

>5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute

vagrant@vagrant:~$ traceroute -I -An 8.8.8.8  
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets  
 1  10.0.2.2 [*]  0.772 ms  0.662 ms  0.592 ms  
 2  192.168.0.21 [*]  2.079 ms  1.822 ms  1.746 ms  
 3  195.9.250.205 [AS25513]  3.379 ms  4.636 ms  5.634 ms  
 4  94.29.127.185 [AS25513]  6.529 ms  7.532 ms  7.888 ms  
 5  94.29.127.186 [AS25513]  8.604 ms  8.537 ms  9.124 ms  
 6  212.188.1.106 [AS8359]  9.054 ms  3.382 ms  3.856 ms  
 7  212.188.1.105 [AS8359]  4.126 ms  4.052 ms  3.970 ms  
 8  212.188.56.13 [AS8359]  8.770 ms  9.049 ms  8.982 ms  
 9  195.34.50.74 [AS8359]  4.357 ms  4.291 ms  4.213 ms  
10  212.188.29.82 [AS8359]  4.054 ms  6.361 ms  6.883 ms  
11  108.170.250.113 [AS15169]  17.765 ms  18.066 ms  4.047 ms  
12  * 142.250.238.12 [AS15169]  21.533 ms  21.403 ms  

13  * * *

14  74.125.253.94 [AS15169]  29.387 ms  29.591 ms  29.522 ms  
15  172.253.70.47 [AS15169]  30.294 ms  30.548 ms  30.481 ms  
..........  
25  8.8.8.8 [AS15169]  24.163 ms  23.538 ms *    

>6. Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?

Наибольшие задержки здесь:  
11. AS15169  108.170.250.113                                                 30.0%    10    4.8  11.3   4.8  37.3  12.0  
12. AS15169  142.250.238.12                                                   0.0%    10   22.5  24.2  21.8  41.0   5.9  
13. AS15169  209.85.143.39                                                   70.0%    10   24.0  27.2  23.9  33.6   5.6  

>7. Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой dig

dns.google.             10800   IN      NS      ns2.zdns.google.  
dns.google.             10800   IN      NS      ns3.zdns.google.  
dns.google.             10800   IN      NS      ns4.zdns.google.  
dns.google.             10800   IN      NS      ns1.zdns.google.  
  
dns.google.             900     IN      A       8.8.4.4  
dns.google.             900     IN      A       8.8.8.8  

>8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой dig

8.8.8.8.in-addr.arpa.   48164   IN      PTR     dns.google.  
4.4.8.8.in-addr.arpa.   86400   IN      PTR     dns.google.  
