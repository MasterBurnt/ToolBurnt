#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : ‌TcpPortScannar
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt

#Libraries
import threading
import socket
import datetime,os,time,sys
from colorama import Fore,init,Style 

#C&B&I
init()
c1 = Style.BRIGHT + Fore.LIGHTWHITE_EX 
c2 = Style.BRIGHT + Fore.LIGHTGREEN_EX 
c3 = Style.BRIGHT + Fore.LIGHTCYAN_EX 
c4 = Style.BRIGHT + Fore.LIGHTRED_EX 
c5 = Style.BRIGHT + Fore.LIGHTYELLOW_EX 
c6 = Style.BRIGHT + Fore.LIGHTBLUE_EX 
c7 = Fore.RESET 

#Clear Console 
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') 


def __start__():
    try:
        def banner():
            clear()
            a = c5+f"""
___  ____ ____ ___  ____ ____ ____ _  _ 
|__] |  | |__/  |   [__  |    |__| |\ | 
|    |__| |  \  |   ___] |___ |  | | \| {c1}TCP\n"""
            for x in a:
                print(x,end = "")
                sys.stdout.flush()
                time.sleep(0.03)
       
        banner()
        print(f"""
{c3}{"*" * 43}{c7}       
@name   : PortScan
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 43}
        """)        
        #Entries
        target = input(c2+f'[?] {c1}Please Enter Target :{c7} ').strip()
        try:
            range1,range2= map(int,input(c2+f'[?] {c1}specify the port review range(example : 1,1024) : {c7}').split(','))
        except ValueError as e:
            print(c4+f"\n[!] {c1}{e}")
            sys.exit(1)
            
        
        try:
            target = socket.gethostbyname(target)
        except socket.gaierror as e: 
                print(c4+f"\n[!] {c1}Hostname Could Not Be Resolved !")
                sys.exit(1)
        
           
        banner()
        print(f"""
{c3}{"*" * 43}
{c2}[*] {c1}Target : {c7}{target}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 43}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n{c3}p{c4}l{c5}e{c6}a{c7}s{c1}e {c2}w{c3}a{c4}i{c5}t{c6}{c7}{c1}. {c2}.{c3}.\n""")
        
        
        #Connect
        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #timeout
            s.settimeout(0.5)
            
            try:
                con = s.connect((target,port))
                service = socket.getservbyport(port,"tcp") 
                print(c2+f'[+]{c6} Port : {c1} {port}\t{c6}service :{c1} {service}')
                con.close()    
            except:
                pass                           
        #Output       
        for port in range(range1,range2+1):
                t = threading.Thread(target=portscan, kwargs={'port':port})
                t.start()
          
        
    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
    
