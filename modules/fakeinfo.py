#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Fake-info
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt 


#Library
try:
    import urllib.request 
except ImportError as e:
    print(e)
import datetime,os,sys
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
        #Banner
        def banner():
            clear()
            a = c5+f"""
____ ____ _  _ ____  _ _  _ ____ ____ 
|___ |__| |_/  |___  | |\ | |___ |  | 
|    |  | | \_ |___  | | \| |    |__| {c1}Generator\n"""
            for x in a:
                print(x,end = "")
                sys.stdout.flush()
                sleep(0.03) 
            
        
        #Format
        def format(x):
            json = "https://randomuser.me/api/?format=json"
            csv = "https://randomuser.me/api/?format=csv"
            yaml = "https://randomuser.me/api/?format=yaml"
            xml = "https://randomuser.me/api/?format=xml"
            
            if x == "1":
                return json
            elif x == "2":
               return csv 
            elif x == "3":
                return yaml
            elif x == "4":
                return xml 
            elif x == "0":        
                print(c7+f'[BYE] {c6}B{c2}e{c3}s{c4}t{c5} {c6}w{c1}i{c2}s{c3}h{c4}e{c5}s{c7} =)')
                sleep(2)
                clear()
                exit(0)
            else:
                print(c4+f'\n[!] {c1}Out of bounds! ')
                sleep(2)
                Feature()
        #Feature
        def Feature():
            while True:
                banner()
                print(f"""
{c3}{"*" * 47}{c7}       
@name   : FakeInformation
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 47}
        """) 
                print(f"""
{c2}[1]{c1} Get fake information file : format-Json
{c2}[2]{c1} Get fake information file : format-Csv
{c2}[3]{c1} Get fake information file : format-Yaml
{c2}[4]{c1} Get fake information file : format-Xml
{c2}[0]{c1} Exit! 
        """)
                call = input(c2+f"[?]{c1} Please select an option :{c7} ").strip()
                if call not in ["1","2","3","4","0"]:
                    print(c4+f'\n[!] {c1}Out-of-bounds option! ')
                    sleep(2)
                    pass
                else:
                    return format(call)
                    break    
        
        #Request
        def output():
                url = Feature()
                try:
                    r = urllib.request.urlopen(url).read().decode()
                except :
                    print(c4+f"\n[!] {c1}Please check your connection to the Internet! ")
                    exit(1)
                
                #Save
                try:
                    os.mkdir('FakeInfo-History')
                except:
                    pass
                         
                os.chdir('FakeInfo-History')
                            
                File_Extension = url[34:] 
                file = open(f"fakeinfo.{File_Extension}", "wt")
                file.write(r)
                file.close()
                banner()
                print(f"""
{c3}{"*" * 47}
{c2}[*] {c1}OutPut : {c7}fakeinfo.{File_Extension}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 47}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n""")
                print(c2+f"[s] {c1}Folder : FakeInfo-History\n{c2}[s]{c1} file saved : fakeinfo.{File_Extension}")
                sys.exit(0)
                return output()
        output()
    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
