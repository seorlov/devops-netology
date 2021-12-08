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

Скриншот: ![Альтернативный текст](https://github.com/seorlov/devops-netology/blob/main/Task3.6.2.png)

3. Какой IP адрес у вас в интернете?

4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois

5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute

6. Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?

7. Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой dig

8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой dig
9. 