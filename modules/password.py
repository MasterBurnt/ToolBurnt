#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# @name   : PassList
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt

#Libraries
from concurrent.futures import ThreadPoolExecutor
import datetime,os,sys,random,time
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


list = []
out =[]

#Run
def __start__():
    try:
        #Banner
        def banner():
            clear()
            a = c5+f"""
___  ____ ____ ____  _    _ ____ ___
|__] |__| [__  [__   |    | [__   |
|    |  | ___] ___]  |___ | ___]  | {c1}Maker\n"""

            for x in a:
                print(x,end = "")
                sys.stdout.flush()
                time.sleep(0.007)

        def banner1():
            print(f"""
{c3}{"*" * 41}{c7}       
@name   : PassList
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 41}
        """)
        banner();banner1()
        print(c2+f"""
[*] {c1}Enter words, characters, target color, date of birth, etc..
{c2}[*] {c1}To pass (Press Enter...)\n""")

        #Entries
        for x in range(1,101):
            i = input(c2+f"{c1}words #~{c7} ")
            list.append(i)

            #B
            if i == "":
                banner();banner1()
                #File Name
                file = input(c2+f'\n[?] {c1}Select The File Name To Save :{c7} ')
                if file == "":
                    file = "passlist"
                else:
                    pass
                break
            else:
               continue 

        #X+Y
        def task():
            for i in range(1,50):
                    out1 = random.choice(list)
                    out2 = random.choice(list)
                    out3 = random.choice(list)
                    out4 = random.choice(list)
                    out5 = random.choice(list)
                    a = str(out1)+str(out2)
                    b = str(out1)+str(out2)+str(out3)
                    c = str(out1)+str(out2)+str(out3)+str(out4)
                    d = str(out1)+str(out2)+str(out3)+str(out4)+str(out5)
                    if a not in out and len(a) >= 4:
                        out.append(a)
                    elif b not in out and len(b) >= 4:
                        out.append(b)
                    elif c not in out and len(c) >= 4:
                        out.append(c)
                    elif d not in out and len(d) >= 4:
                        out.append(d)
                    else:
                        pass



        def main():
         with ThreadPoolExecutor(max_workers=30) as executor:
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)
           future = executor.submit(task)

        banner()
        print(f"""
{c3}{"*" * 41}
{c2}[*] {c1}Output : {c7}{file}.txt
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 41}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n{c3}p{c4}l{c5}e{c6}a{c7}s{c1}e {c2}w{c3}a{c4}i{c5}t{c6}{c7}{c1}. {c2}.{c3}.\n""")

        main()

        #Mkdir Folder
        try:
            os.mkdir('Pass-History')
        except:
            pass

        #cd Pass-History
        os.chdir('Pass-History')

        #Open output file
        f = open(f'{file}.txt', 'a')

        #Output
        for hit in out:
            f.write(hit+'\n')
        #File Size
        size = f.seek(0, 2)

        #Close output file
        f.close()

        print(c2+f"[s] {c1}Password number : {len(out)}\n{c2}[s] {c1}Saved to file : Pass-History \n{c2}[s] {c1}File Name : {file}.txt\n{c2}[s] {c1}File Size : {size // 1000 / 1000}")

    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
