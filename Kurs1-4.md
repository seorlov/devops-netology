# Курсовая 1-4


## Задача 1. Создайте виртуальную машину Linux.
1. Создаём Vagrantfile:
```
Vagrant.configure("2") do |config|
	config.vm.box = "bento/ubuntu-20.04"
	config.vm.network "private_network", ip: "10.0.0.4"
	config.vm.provider "virtualbox" do |v4|
	  v4.memory = 2048
	  v4.cpus = 1
	 end
end
```
2. Запускаем ВМ:
```
C:\!VG-kurs_1-4>vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: This machine used to live in C:/!VG-dipl but it's now at C:/!VG-kurs_1-4.
==> default: Depending on your current provider you may need to change the name of
==> default: the machine to run it as a different machine.
==> default: Checking if box 'bento/ubuntu-20.04' version '202107.28.0' is up to date...
==> default: Clearing any previously set forwarded ports...
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: Warning: Connection reset. Retrying...
    default: Warning: Connection aborted. Retrying...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /vagrant => C:/!VG-kurs_1-4
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.
```

## Задача 2. Установите ufw и разрешите к этой машине сессии на порты 22 и 443, при этом трафик на интерфейсе localhost (lo) должен ходить свободно на все порты.
```
vagrant@vagrant:~$ ufw --version
ufw 0.36
Copyright 2008-2015 Canonical Ltd.
vagrant@vagrant:~$ sudo ufw status
Status: inactive
vagrant@vagrant:~$ sudo ufw default deny incoming
Default incoming policy changed to 'deny'
(be sure to update your rules accordingly)
vagrant@vagrant:~$ sudo ufw default allow outgoing
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)
vagrant@vagrant:~$ sudo ufw allow 22
Rules updated
Rules updated (v6)
vagrant@vagrant:~$ sudo ufw allow 443
Rules updated
Rules updated (v6)
vagrant@vagrant:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
vagrant@vagrant:~$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22                         ALLOW IN    Anywhere
443                        ALLOW IN    Anywhere
22 (v6)                    ALLOW IN    Anywhere (v6)
443 (v6)                   ALLOW IN    Anywhere (v6)
```

## Задача 3. Установите hashicorp vault (инструкция по ссылке).
```
vagrant@vagrant:~$ curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
OK

vagrant@vagrant:~$ sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
Get:1 https://apt.releases.hashicorp.com focal InRelease [9,495 B]
Hit:2 http://archive.ubuntu.com/ubuntu focal InRelease
...
Fetched 9,488 kB in 10s (984 kB/s)
Reading package lists... Done

vagrant@vagrant:~$ sudo apt-get update && sudo apt-get install vault
Hit:1 http://security.ubuntu.com/ubuntu focal-security InRelease
Hit:2 http://archive.ubuntu.com/ubuntu focal InRelease
...
Vault TLS key and self-signed certificate have been generated in '/opt/vault/tls'.

vagrant@vagrant:~$ vault
Usage: vault <command> [args]

Common commands:
    read        Read data and retrieves secrets
    write       Write data, configuration, and secrets
...
```

## Задача 4. Cоздайте центр сертификации по инструкции (ссылка) и выпустите сертификат для использования его в настройке веб-сервера nginx (срок жизни сертификата - месяц).

```
vagrant@vagrant:~$ vault server -dev -dev-root-token-id root
==> Vault server configuration:

             Api Address: http://127.0.0.1:8200
....

vagrant@vagrant:~$ export VAULT_ADDR=http://127.0.0.1:8200
vagrant@vagrant:~$ export VAULT_TOKEN=root
vagrant@vagrant:~$ vault secrets enable pki
Success! Enabled the pki secrets engine at: pki/
vagrant@vagrant:~$ vault secrets tune -max-lease-ttl=87600h pki
Success! Tuned the secrets engine at: pki/
vagrant@vagrant:~$ vault write -field=certificate pki/root/generate/internal \
>      common_name="test.example.com" \
>      ttl=87600h > CA_cert.crt
vagrant@vagrant:~$ dir
CA_cert.crt  test
vagrant@vagrant:~$ vault write pki/config/urls \
>      issuing_certificates="$VAULT_ADDR/v1/pki/ca" \
>      crl_distribution_points="$VAULT_ADDR/v1/pki/crl"
Success! Data written to: pki/config/urls
vagrant@vagrant:~$ vault secrets enable -path=pki_int pki
Success! Enabled the pki secrets engine at: pki_int/
vagrant@vagrant:~$ vault secrets tune -max-lease-ttl=43800h pki_int
Success! Tuned the secrets engine at: pki_int/
vagrant@vagrant:~$ vault write -format=json pki_int/intermediate/generate/internal \
>      common_name="test.example.com Intermediate Authority" \
>      | jq -r '.data.csr' > pki_intermediate.csr
-bash: jq: command not found
vagrant@vagrant:~$ sudo apt install jq
Reading package lists... Done
Building dependency tree
.......
vagrant@vagrant:~$ vault write -format=json pki_int/intermediate/generate/internal      common_name="example.com Interme
diate Authority"      | jq -r '.data.csr' > pki_intermediate.csr
vagrant@vagrant:~$ dir
CA_cert.crt  pki_intermediate.csr  test
vagrant@vagrant:~$ vault write -format=json pki/root/sign-intermediate csr=@pki_intermediate.csr \
>      format=pem_bundle ttl="43800h" \
>      | jq -r '.data.certificate' > intermediate.cert.pem
vagrant@vagrant:~$ dir
CA_cert.crt  intermediate.cert.pem  pki_intermediate.csr  test
vagrant@vagrant:~$ vault write pki_int/intermediate/set-signed certificate=@intermediate.cert.pem
Success! Data written to: pki_int/intermediate/set-signed
vagrant@vagrant:~$ vault write pki_int/roles/example-dot-com \
>      allowed_domains="test.example.com" \
>      allow_subdomains=true \
>      max_ttl="720h"
Success! Data written to: pki_int/roles/example-dot-com
vagrant@vagrant:~$ vault write pki_int/issue/example-dot-com common_name="test.example.com" ttl="720h"
Key                 Value
..............
private_key_type    rsa
serial_number       .........d8:95:0d:bb:..........
```
## Задача 5. Установите корневой сертификат созданного центра сертификации в доверенные в хостовой системе.
>![Скриншот](https://github.com/seorlov/devops-netology/blob/main/kurs1.png "Скриншот")



## Задача 6. Установите nginx.
```
vagrant@vagrant:~$ sudo apt update
Get:1 https://apt.releases.hashicorp.com focal InRelease [9,495 B]
...
Fetched 7,033 kB in 7s (1,010 kB/s)
...
vagrant@vagrant:~$ sudo apt -y install nginx
Reading package lists... Done
...
Fetched 3,165 kB in 3s (1,106 kB/s)
...
vagrant@vagrant:~$ sudo systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2022-01-28 21:25:30 UTC; 3s ago
...
```

## Задача 7. По инструкции (ссылка) настройте nginx на https, используя ранее подготовленный сертификат:
```
vagrant@vagrant:/$ cd etc/nginx
vagrant@vagrant:/etc/nginx$ sudo vim nginx.conf
...
Добавляем в файл конфигурацию ssl сервера:
http {
        server {
                listen 443 default ssl;
                server_name         test.test.example.com;
                ssl_certificate     /home/vagrant/test.example.com.crt;
                ssl_certificate_key /home/vagrant/test.example.com.key;
                ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
                ssl_ciphers         HIGH:!aNULL:!MD5;
        }
        ##
        # Basic Settings
        ##
        ....
}
vagrant@vagrant:/etc/nginx$ vagrant@vagrant:/etc/nginx$ sudo service nginx reload
```
## Задача 8. Откройте в браузере на хосте https адрес страницы, которую обслуживает сервер nginx.

>![Скриншот](https://github.com/seorlov/devops-netology/blob/main/kurs2.png "Скриншот")

## Задача 9. Создайте скрипт, который будет генерировать новый сертификат в vault:
```bash
#!/usr/bin/env bash
#Файл autorefresh.sh
cd /home/vagrant
export VAULT_ADDR=http://127.0.0.1:8200
export VAULT_TOKEN=root
vault write -format=json pki_int/issue/example-dot-com common_name="test.test.example.com" ttl="720h" > test.example.com.pem
cat test.example.com.pem | jq -r .data.certificate > test.example.com.crt
cat test.example.com.pem | jq -r .data.issuing_ca >> test.example.com.crt
cat test.example.com.pem | jq -r .data.private_key > test.example.com.key

sudo service nginx reload

```    
## Задача 10. Поместите скрипт в crontab, чтобы сертификат обновлялся какого-то числа каждого месяца в удобное для вас время.
```
vagrant@vagrant:~$ crontab -e
0 0 1 * * /home/vagrant/autorefresh.sh
```