#!/usr/bin/env bash
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
