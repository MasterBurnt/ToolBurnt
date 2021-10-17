#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : IpLocation 
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt 

#Libraries
try:
    import requests
    import ipapi
except ImportError as e:
    print(e)
import datetime,os,sys,time
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
_ ___  _    ____ ____ ____ ___ _ ____ _  _    
| |__] |    |  | |    |__|  |  | |  | |\ |    
| |    |___ |__| |___ |  |  |  | |__| | \| {c1}info\n"""
                for x in a:
                    print(x,end = "")
                    sys.stdout.flush()
                    time.sleep(0.03)
       
        banner()
        print(f"""
{c3}{"*" * 47}{c7}       
@name   : IpLocation
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 47}
        """) 
    
        ip = input(c2+f'[?] {c1}Please Enter Ip Target :{c7} ').strip()      
         
        #check out & Request 
        try:
            banner()
            print(f"""
{c3}{"*" * 47}
{c2}[*] {c1}Target : {c7}{ip}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 47}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n""")

            for x,y in ipapi.location(ip=ip).items():
                print(c2+f"[+] {c6} {x} : {c1} {y}")
              
        except:
            print(c4+f'[!] {c1}Please check your Internet connection or Target IP address ')
              
    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
