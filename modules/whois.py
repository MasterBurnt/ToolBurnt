#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# @name   : whois
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt

#Libraries
import datetime,os,socket,sys,time
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
        #Banner
        def banner():
            clear()
            a = c5+f"""
_ _ _ _  _ ____   _ ____   __.   
| | | |__| |  |   | [__     _]   
|_|_| |  | |__|   | ___]    .  {c1}Protocol
"""
            for x in a:
                print(x,end = "")
                sys.stdout.flush()
                time.sleep(0.03)

        banner()
        print(f"""
{c3}{"*" * 39}{c7}       
@name   : ComboList
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 39}
        """)
        out = str()
    
        #Input
        domain = input(c2+f"[?] {c1}Enter Domain Address [Google.com] : ").lower().replace("http://","").replace("https://","").replace("www.","").strip()
    
        #Partial check of domain correctness
        domain_find = domain.find('.')
        if domain_find == -1 or domain == '' or domain == '127.0.0.1':
            print(c4+f'\n[!] {c1}Please enter the domain address correctly!')
            exit(0)
    
        #Guided
        elif domain[-3:] in ["com", "net", "org"]:
            whois_server = "whois.internic.net"
        else:
            whois_server =  "whois.iana.org"
    
        #Connect
        try :
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((whois_server,43))
            s.send((domain+"\r\n").encode())
        except socket.error:
            print(c4+f'\n[!] {c1}Check your connection to the Internet')
            exit(1)
            
        #Filter & Show
        msg = s.recv(1000000)
        msg = msg.decode()
        if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
            out = msg[:-2405]
        else:
            out = msg[136:-181]
        if out == "":
            print(c4+f"\n[!]{c1} Failed! Check that the domain address is correct\nAlso Check your connection to the Internet!  ")
            exit(0)
        else:
            banner()
            print(f"""
{c3}{"*" * 39}
{c2}[*] {c1}Target : {c7}{domain}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 39}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n""") 
    
            #Save
            try:
                os.mkdir('Whois-History')
            except:
                pass
               
            os.chdir('Whois-History')
            
            file = open(domain[0:domain_find]+".txt", "wt")
            file.write(out)
            
            print(c2+f"[s] {c1}{domain[0:domain_find]}.txt Saved to folder Whois-History")
            file.close() 
    
    
    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
