#!/usr/bin/env bash
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
