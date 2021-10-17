#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# @name   : ComboList
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt

#Libraries
import datetime,os,sys,time
from concurrent.futures import ThreadPoolExecutor
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
____ ____ _  _ ___  ____  _    _ ____ ___ 
|    |  | |\/| |__] |  |  |    | [__   |  
|___ |__| |  | |__] |__|  |___ | ___]  | {c1}Maker\n"""
           for x in a:
                print(x,end = "")
                sys.stdout.flush()
                time.sleep(0.03) 
        banner()
        print(f"""
{c3}{"*" * 46}{c7}       
@name   : ComboList
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 46}
        """)
        
        #Entries
        username_file = input(c2+f'[?]{c1} Please enter the username file :{c7} ').strip()
        password_file = input(c2+f'[?]{c1} Please enter the password file :{c7} ').strip()
        file_name = input(c2+f'[?]{c1} Please select a file name to save :{c7} ').strip()
        
        #Check output name
        if file_name == "":
            file_name = "combo"
        else:
            pass
            
        #Open Files 
        try:
            username = open(username_file, "r").read().splitlines()
        except IOError as e:
            print(c4+f"\n[!] {c1}Username file not found! =( ")
            exit(1)
        try:
            password = open(password_file, "r").read().splitlines()
        except IOError as e:
            print(c4+f"\n[!] {c1}password list file not found! =( ")
            exit(2)
            
        #Append    
        combo = [] 
        def task():
            for user in set(username):
                for passs in set(password):
                    if user == "" or passs == "":
                        pass
                    else:
                        combo.append(f"{str(user)}:{str(passs)}\n")
        
        
        #Task
        def main():
         with ThreadPoolExecutor(max_workers=5) as executor:
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
        
        banner()
        print(f"""
{c3}{"*" * 46}
{c2}[*] {c1}Output : {c7}{file_name}.txt
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 46}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n{c3}p{c4}l{c5}e{c6}a{c7}s{c1}e {c2}w{c3}a{c4}i{c5}t{c6}{c7}{c1}. {c2}.{c3}.\n""")

        main()
        
        #Save
        try:
            os.mkdir('Combo-History')
        except:
            pass
            
        os.chdir('Combo-History') 
        out = open(f"{file_name}.txt","a")
        
        for w in set(combo):
            out.write(w)
            
        size = out.seek(0, 2)
        
        out.close()
        
        print(c2+f"{c2}[s] {c1}Saved to file : Combo-History\n{c2}[s] {c1}File Name : {file_name}.txt\n{c2}[s] {c1}File Size : {size // 1000 / 1000}")
        
    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
