#!/usr/bin/python3

import socket
import sys
import time
import threading


RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

usage = f"{YELLOW}python3 port_scanner.py TARGET START_PORT END_PORT{RESET}"


if len(sys.argv) != 4:
    print(usage)
    sys.exit()
else:
    print(CYAN + r"""
  ______   ______  __       __  _______   __        ________          
 /      \ |      \|  \     /  \|       \ |  \      |        \         
|  $$$$$$\ \$$$$$$| $$\   /  $$| $$$$$$$\| $$      | $$$$$$$$         
| $$___\$$  | $$  | $$$\ /  $$$| $$__/ $$| $$      | $$__             
 \$$    \   | $$  | $$$$\  $$$$| $$    $$| $$      | $$  \            
 _\$$$$$$\  | $$  | $$\$$ $$ $$| $$$$$$$ | $$      | $$$$$            
|  \__| $$ _| $$_ | $$ \$$$| $$| $$      | $$_____ | $$_____          
 \$$    $$|   $$ \| $$  \$ | $$| $$      | $$     \| $$     \         
  \$$$$$$  \$$$$$$ \$$      \$$ \$$       \$$$$$$$$ \$$$$$$$$         
                                                                      
                                                                      
                                                                      
 _______    ______   _______  ________                                
|       \  /      \ |       \|        \                               
| $$$$$$$\|  $$$$$$\| $$$$$$$\\$$$$$$$$                               
| $$__/ $$| $$  | $$| $$__| $$  | $$                                  
| $$    $$| $$  | $$| $$    $$  | $$                                  
| $$$$$$$ | $$  | $$| $$$$$$$\  | $$                                  
| $$      | $$__/ $$| $$  | $$  | $$                                  
| $$       \$$    $$| $$  | $$  | $$                                  
 \$$        \$$$$$$  \$$   \$$   \$$                                  
                                                                      
                                                                      
                                                                      
  ______    ______    ______   __    __  __    __  ________  _______  
 /      \  /      \  /      \ |  \  |  \|  \  |  \|        \|       \ 
|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$\ | $$| $$\ | $$| $$$$$$$$| $$$$$$$\
| $$___\$$| $$   \$$| $$__| $$| $$$\| $$| $$$\| $$| $$__    | $$__| $$
 \$$    \ | $$      | $$    $$| $$$$\ $$| $$$$\ $$| $$  \   | $$    $$
 _\$$$$$$\| $$   __ | $$$$$$$$| $$\$$ $$| $$\$$ $$| $$$$$   | $$$$$$$\
|  \__| $$| $$__/  \| $$  | $$| $$ \$$$$| $$ \$$$$| $$_____ | $$  | $$
 \$$    $$ \$$    $$| $$  | $$| $$  \$$$| $$  \$$$| $$     \| $$  | $$
  \$$$$$$   \$$$$$$  \$$   \$$ \$$   \$$ \$$   \$$ \$$$$$$$$ \$$   \$$
                       
          """ + RESET)

    print(CYAN + "-"*30)
    print("⚡ PORT SCANNER")
    print("-"*30 + RESET)


try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print(RED + "Name resolution error" + RESET)
    sys.exit()


try:
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
except ValueError:
    print(RED + "Ports must be numbers" + RESET)
    sys.exit()

if start_port > end_port:
    print(RED + "Start port must be less than end port" + RESET)
    sys.exit()

print(CYAN + f"Scanning target {target}" + RESET)


def scan_port(port):
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan.settimeout(1)
    conn = scan.connect_ex((target, port))
    if conn == 0:
        print(GREEN + f"[OPEN] {port}" + RESET)
    scan.close()


threads = []
start_time = time.time()

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


end_time = time.time()
print(YELLOW + f"\nTime Elapsed: {round(end_time - start_time, 2)} seconds" + RESET)