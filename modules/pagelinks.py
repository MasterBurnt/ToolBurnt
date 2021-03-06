#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : ExtractPageLinks
# @url    : http://github.com/MasterBurnt
# @author : MasterBurnt 

#Libraries
try:
    import requests
    from bs4 import BeautifulSoup
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
___  ____ ____ ____  _    _ _  _ _  _ ____    
|__] |__| | __ |___  |    | |\ | |_/  [__     
|    |  | |__] |___  |___ | | \| | \_ ___] {c1}Extract        
        """
            for x in a:
                print(x,end = "")
                sys.stdout.flush()
                time.sleep(0.03)        
        
        banner()
        print(f"""
{c3}{"*" * 50}{c7}       
@name   : PageLinks
@url    : http://github.com/MasterBurnt
@author : MasterBurnt
{c3}{"*" * 50}
        """)
            
        url = input(c2+f'[?] {c1}Please Enter Url :{c7} ').strip()
        
        #Link Correction
        if "https://" in url or "http://" in url:
            pass
        else:
            url = "http://"+url
            
        #Requests    
        try:
            response = requests.get(url,timeout=3) 
        except:
            print(c4+f'\n[!] {c1}Please check your Internet connection or link address')
            sys.exit(1)
            
        banner()
        print(f"""
{c3}{"*" * 50}
{c2}[*] {c1}Target : {c7}{url}
{c2}[*] {c1}started at : {c7}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{c3}{"*" * 50}
\n{c1}R{c2}E{c3}V{c4}I{c5}E{c6}W\n""") 

        #parse html page
        html_page = BeautifulSoup(response.text, "html.parser")
        
        #get all <a> tags
        all_urls = html_page.findAll("a")
        internal_urls = set()
        external_urls =set()
        for link in all_urls:
            href=link.get('href')
            
            if href:
                if url in href:
                    #internal link    
                    internal_urls.add(href)
                #same page target link
                elif href[0]=="#":    
                    internal_urls.add(f"{url}{href}")
                    
                else:
                    external_urls.add(href)
                    
        #Internal link            
        print(c2+f"[$I] {c6}Total Internal URLs: {c1}{len(internal_urls)}\n")
        for url in internal_urls:
            print(c2+f"[+] {c6}Internal URL {c1}{url}")
        
        #external link
        print(c2+f"\n\n[$E] {c6}Total External URLs: {c1}{len(external_urls)}\n")
        for url in external_urls:
            print(c2+f"[+] {c6}External URL {c1}{url}")

    except (KeyboardInterrupt,EOFError, Exception):
        clear()
        sys.exit()
