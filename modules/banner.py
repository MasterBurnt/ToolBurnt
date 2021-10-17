#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# @name   : Banner
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt

from colorama import Fore,Style,init
import sys,time,os

#C&B
init()
WHITE  =  Style.BRIGHT + Fore.LIGHTWHITE_EX 
GREEN  =  Style.BRIGHT + Fore.LIGHTGREEN_EX
RED    =  Style.BRIGHT + Fore.LIGHTRED_EX 



#Clear Console
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')    

#Banners       
def banner(x):
    if x == 1:
        clear()
        a = GREEN+f"""

 ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
 
                       
"""
        for x in a:
            print(x,end = "") 
            sys.stdout.flush()
            time.sleep(0.005)
    elif x == 2:
        clear()
        a = GREEN +  '''
.  _  .   .__  .  .  __,--'
  (_)    '/__\ __,--'
'  .  ' . | o|'     MySystem
         [IIII]`--.__
          |  |       `--.__
          | :|             `--.__
          |  |                   `--.__
._,,.-,.__.'__`.___.,.,.-..,_.,.,.,-._..`--..-.,._.,,._,-,.\n'''
        for x in a:
            print(x,end = "")
            sys.stdout.flush()
            time.sleep(0.007)
    elif x == 3:
        clear()
        a = GREEN +  '''
____
\   `.
 \    `.
  \ \   `.
   \ Burnt`.
   :. . . . `._______________________.-~|~~-._
   \                                 ---'-----`-._
    /-------/             _...---------..         ~-._________
   //     .`_________  .-`           \ .-~           /
  //    .'       ||__.~             .-~_____________/
 //___.`           .~            .-~
                 .~           .-~
               .~         _.-~
               `-_____.-~'         
\n'''
        for x in a:
            print(x,end = "")
            sys.stdout.flush()
            time.sleep(0.007)
        a = '  ~Name : ToolBurnt\n  ~Url : https://github.com/MasterBurnt\ToolBurnt\n  ~Version : 0.0.1\n  ~Author : MasterBurnt\n  ~Contact & Bug Report : t.me/TheBurnt\n\n  <Copyright © 2021 "ToolBurnt".All rights reserved =)>\n '
        for x in a:
            print(x,end = "")
            sys.stdout.flush()
            time.sleep(0.05)
    elif x == 4:
        clear()
        a = RED +  '''
        
-=███████╗██████╗ ██████╗  ██████╗ ██████╗     
-=██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗    
-=█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝    
-=██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗    
-=███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║    
-=╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ 

'''
        for x in a:
            print(x,end = "")
            sys.stdout.flush()
            time.sleep(0.005)
