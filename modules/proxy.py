#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Proxy
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt

#Libraries
try:
    import requests
except ImportError as e:
    print(e)
import datetime,os,time,sys
from time import sleep
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
___  ____ ____ _  _ _   _  _    _ ____ ___ 
|__] |__/ |  |  \/   \_/   |    | [__   |  
|    |  \ |__| _/\_   |    |___ | ___]  | {c1}Download\n"""
            for x in a:
                print(x,end = "")
                sys.stdout.flush()
                time.sleep(0.03)

        def banner1():
            print(f"""
{c3}{"*" * 50}{c7}       
@name   : ProxyList
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 50}
        """) 
   
        banner()
        #Items
        while True:
            banner1()     
            type = input(f'''    
{c2}[1] {c1}Getting proxy http
{c2}[2] {c1}Getting proxy https
{c2}[3] {c1}Getting proxy socks4
{c2}[4] {c1}Getting proxy socks5
{c2}[0] {c1}exit
            
{c2}[?] {c1}Please select an item :{c7} ''').strip()
            if type == "1":
                type = "http"
                break
            elif type == "2":
                type = "https"
                break
            elif type == "3":
                type = "socks4"
                break
            elif type == "4":
                type = "socks5"
                break
            elif type == "0":
                print(c7+f'\n[BYE] {c6}B{c5}e{c4}s{c3}t{c2} {c1}w{c2}i{c3}s{c4}h{c5}e{c6}s')
                sleep(2)
                clear()
                exit(0)                  
            else:
                print(c4+f"\n[!] {c1}Out of bounds!")
                sleep(2)
                banner()
                continue
        banner()        
        while True:
            banner1()
            anon = input(f'''
{c2}[1] {c1}anonymous
{c2}[2] {c1}elite
{c2}[3] {c1}you can skip this step (enter or 3)
{c2}[0] {c1}exit    
        
{c2}[?] {c1}Please select an item : {c7}''').strip()
            if anon == "1":
                anon = "anonymous"
                break 
            elif anon == "2":
                anon = "elite"
                break 
            elif anon == "3" or anon == "":
                anon = ""
                break 
            elif anon == "0":
                print(c7+f'\n[BYE] {c6}B{c5}e{c4}s{c3}t{c2} {c1}w{c2}i{c3}s{c4}h{c5}e{c6}s')
                sys.exit()
            else:
                print(c4+f"\n[!] {c1}Out of bounds!")
                sleep(2)
                banner()
                continue 
                
        api = "https://www.proxy-list.download/api/v1/get" 
               
        if anon == "":
            api = f"{api}?type={type}"
        else: 
            api = f"{api}?type={type}&anon={anon}"     
        try:
            response = requests.get(api, timeout = 3).text
        except:
            print(c4+f"""\n[!] {c1}Please check your internet connection.\nAlso, if your country is under sanctions,\nturn on vpn and try again!""")
            sys.exit(1)
        
        banner()
        print(f"""
{c3}{"*" * 50}
{c2}[*] {c1}Proxy : {type}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 50}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n""") 
        
        if response == "":
            print(c4+f"[!] {c1}it is empty!") 
            sys.exit()
        
        #Save    
        else:
            try:
                os.mkdir('Proxy-History')
            except:
                    pass
                          
            os.chdir('Proxy-History')
            
            file = open(type+".txt", "wt")
            file.write(response)
            print(c2+f"[s] {c1}{type}.txt Saved to folder Proxy-History")
            file.close()
               
    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
