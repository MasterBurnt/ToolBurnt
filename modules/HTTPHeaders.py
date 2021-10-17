#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# @name   : HTTPheaders
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt

#Libraries
try:
    import requests
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
_  _ ___ ___ ___   _  _ ____ ____ ___  ____ ____ ____ 
|__|  |   |  |__]  |__| |___ |__| |  \ |___ |__/ [__  
|  |  |   |  |     |  | |___ |  | |__/ |___ |  \ ___] {c1}Reviewing \n"""
            for x in a:
                print(x,end = "")
                sys.stdout.flush()
                time.sleep(0.03)
    
        banner()
        print(f"""
{c3}{"*" * 63}{c7}       
@name   : HTTPHeaders
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 63}
        """)
                                                    
        url = input(c2+f'[?] {c1}Please enter web address :{c7} ')
        
        #Link Correction
        if "https://" in url or "http://" in url:
            pass
        else:
            url = f"http://{url}"
        
        #Requests  
        try:
            response = requests.get(url,timeout= 1)
        except :
            print(c4+f"\n[!] {c1}Check your domain address and Internet connection")
            exit(1)
        
        banner()
        print(f"""
{c3}{"*" * 63}
{c2}[*] {c1}Target : {c7}{url}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 63}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n""") 
 
        out = response.headers
        
        for x,y in out.items():
            print(c2+f"[+] {c6}{x} :{c1} {y}")
            
    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
