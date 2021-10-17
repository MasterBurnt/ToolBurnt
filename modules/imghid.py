#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Steganography
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt 


#Library
try:
    import stepic
    from PIL import Image
    from colorama import Fore,init,Style
except ImportError as e:
    print(e)
import imghdr
import datetime,os,sys
from time import sleep

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
____ ___ ____ ____ ____ _  _ ____ ____ ____ ____ ___  _  _ _   _ 
[__   |  |___ | __ |__| |\ | |  | | __ |__/ |__| |__] |__|  \_/  
___]  |  |___ |__] |  | | \| |__| |__] |  \ |  | |    |  |   |  {c1}png\n"""
            for x in a:
                    print(x,end = "")
                    sys.stdout.flush()
                    sleep(0.02)
        def banner1():
            print(f"""
{c3}{"*" * 67}{c7}       
@name   : PngSecret 
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 67}
        """)        
        def encode(file):
            try:
                #This Function Will Put data on picture
                img = Image.open(file)
                banner();banner1()
                text = input(f"{c2}[?] {c1}Secret Text : ")
                img_stegano = stepic.encode(img,text.encode())
                
                name = input(f"{c2}[?] {c1}Output file Name <Png format only> : ")
                try:
                    os.mkdir('Secret-History/')
                except:
                    pass
                os.chdir('Secret-History') 
                img_stegano.save(name)
                banner()
                print(f"""
{c3}{"*" * 67}
{c2}[*] {c1}Output : {c7}{name}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 67}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n""")
                print(f'{c2}[s] {c1}Photos Folder : Secret-History\n{c2}[s] {c1}Photo Name : {name} ')     
            except ValueError as e:
                print(f"{c4}[!]{c1} {e}")
                exit(1)
        def decode(file):
            banner()
            try:
                # This Function Will get data from picture
                img = Image.open(file)
                decoded = stepic.decode(img)
            except ValueError as e:
                print(f"{c4}[!] {c1}{e}")
                exit(1)
            return decoded
        try:
            banner();banner1()
            file  = input(c2+f"[?] {c1}Image File <png> : ")
            #file = f'../{file}'
            format = imghdr.what(file)
            if format == "png":   
                pass
            else:
                print(c4+f'\n[!]{c1} format : {format}! Please just try for png format photos! ')
                exit(1)
        except FileNotFoundError as e:
            print(f'\n{c4}[!] {c1}{e}')
            exit(1) 
        while True:
            banner();banner1()
            mode = input(f"""{c2}[1]{c1} Encode Sec
{c2}[2]{c1} Decode Sec
        
{c2}[?] {c1}Please enter the name of a photo in 'png' format : """ )
            if mode == "1":        
                encode(file)          
                break
            elif mode == "2":
                text = decode(file)
                print(f"""
{c3}{"*" * 67}
{c2}[*] {c1}Output : {c7}{file}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 67}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n""")
                print(c2+f"[W] {c1}Decoded Text : {text}")      
                break
            else:
                print(f"\n{c4}[!] {c1}Out of bounds!")
                exit(1)
           
    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
