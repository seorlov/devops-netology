#Домашнее задание к занятию "4.1. Командная оболочка Bash: Практические навыки"

>Обязательная задача 1  
Есть скрипт:  
a=1  
b=2  
c=a+b  
d=$a+$b  
e=$(($a+$b))  
Какие значения переменным c,d,e будут присвоены? Почему?  

Переменная	Значение	Обоснование  
c	a+b Переменной с присваивается строка "a+b", а не сумма переменных.  
d	1+2	Переменной d присваивается стока с подстановкой значений переменных a и b.  
e	3	В переменной уже полностью соблюдён синтаксис для вычисления арифметической операции 1+2  

>Обязательная задача 2  
На нашем локальном сервере упал сервис и мы написали скрипт, который постоянно проверяет его доступность, записывая дату проверок до тех пор, пока сервис не станет доступным. В скрипте допущена ошибка, из-за которой выполнение не может завершиться, при этом место на Жёстком Диске постоянно уменьшается. Что необходимо сделать, чтобы его исправить:  
while ((1==1)  
do  
	curl https://localhost:4757  
	if (($? != 0))  
	then  
		date >> curl.log  
	fi  
done  

Исправлены ошибки синтаксиса, добавлена пауза 5 сек:  
while ((1==1))  
do  
	curl https://localhost:4757  
	if (($? != 0))  
    then  
    	date >> curl.log  
	fi  
    sleep 5  
done  

>Необходимо написать скрипт, который проверяет доступность трёх IP: 192.168.0.1, 173.194.222.113, 87.250.250.242 по 80 порту и записывает результат в файл log. Проверять доступность необходимо пять раз для каждого узла.  
 
n=1  
array_ip=(192.168.0.1 173.194.222.113 87.250.250.242)  
while ((n<=5))    
do    
	for s in ${array_ip[@]}  
	do  
		curl -v http://$s:80  
		echo http://$s:80" - "$? >> curl3.log  
	done  
	let "n+=1"  
done      

>Обязательная задача 3  
Необходимо дописать скрипт из предыдущего задания так, чтобы он выполнялся до тех пор, пока один из узлов не окажется недоступным. Если любой из узлов недоступен - IP этого узла пишется в файл error, скрипт прерывается.  

array_ip=(192.168.0.1 173.194.222.113 87.250.250.242)  
while ((1==1))    
do    
	for s in ${array_ip[@]}  
	do  
		curl -v http://$s:80  
		if (($?!=0))  
		then  
			echo $s >> error.log  
			exit  
		fi  
	done  
done    
