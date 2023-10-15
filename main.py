import os, threading, time, uuid, random, json, ctypes, string, sys, string, re, webbrowser, json, base64

import requests
import colorama
import tls_client 
import pystyle
import datetime

from websocket import WebSocket
from colorama import *
from pystyle import *

red = Fore.RED
blue = Fore.BLUE
cyan = Fore.CYAN
yellow = Fore.YELLOW
lightcyan = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
orange = Fore.RED + Fore.YELLOW
green = Fore.GREEN
white = Fore.WHITE
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
reset = Fore.RESET

Joined = 0
Token_checked = 0
Tokens_withnitro = 0
valid_tokens = 0
verified_tokens = 0
Message_send = 0
Deleted = 0
vc_joined = 0
pfp_changed = 0
nickname_changed = 0
bio_changed = 0
with open('tokens.txt', 'r') as t:
    lol = sum(len(line.strip().split()) for line in t)
with open('proxies.txt', 'r') as t:
    l = t.readlines()
    proxies = sum(len(line.strip().split()) for line in l)

    
ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} ")

def Server_Joiner_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Joined : {Joined}")
    
def Token_Checker_title():
    global Joined,Token_checked,valid_tokens,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Tokens Checked : {Token_checked} ~ Valid Tokens : {valid_tokens} ~ Verified Tokens: {verified_tokens} ~ Nitro Tokens : {Tokens_withnitro}")

def Server_Spammer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Messages Send : {Message_send}")

def Webhook_Deleter_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Webhooks Deleted : {Deleted}")

def Webhook_Spammer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Messages Send : {Message_send}")

def VC_joiner_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Vc Joined : {vc_joined}")

def Pfp_Changer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Pfp Changed : {pfp_changed}")

def Nickname__bio_Changer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed,bio_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Nicknames Changed : {nickname_changed} ~ Bios Changed : {bio_changed}")

def Member_Spammer_title():
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    ctypes.windll.kernel32.SetConsoleTitleW(f"『 Z3R0Raid 』 By ~Z3R003~ / Tokens: {lol} | Messages Send : {Message_send}")

def load_proxies():
    with open('proxies.txt','r') as p:
        proxies = p.read().splitlines()
    return proxies
def get_time():
    date = datetime.datetime.now()
    current_time = date.strftime('%H:%M:%S')
    return current_time
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def check_useproxies():
    session = tls_client.Session(
        client_identifier="chrome_113",
        random_tls_extension_order=True
    )
    with open('config.json','r') as d:
        data = json.load(d)
        check_proxies = data['use_proxies']
    if check_proxies == 'y' or check_proxies == 'yes' or check_proxies == 'Y' or check_proxies == 'YES':
        proxies = load_proxies()
        proxy = random.choice(proxies)
        session.proxies = {
                'http':f'http://{proxy}',
                'https':f'https://{proxy}'
            }
    else:
        pass
    return session

def Server_Joiner(session,token,invite):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token
    }
    while True:
        try:
            join = session.post(f'https://discord.com/api/v9/invites/{invite}')
            break
        except:
            continue
    if join.status_code == 200:
        with output_lock:
            Joined +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Joined Server{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
    elif join.status_code == 400 and 'captcha_key' in join.text:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {red}Captcha Required {gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {red}ERROR {gray} | ", end="")

def Token_Checker(session,token):
    global Joined,Token_checked,Tokens_withnitro,valid_tokens,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed, verified_tokens
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    }
    
    while True:
        try:
            check = session.get('https://discordapp.com/api/v6/users/@me')
            break
        except:
            continue
    data = check.json()
    if check.status_code == 200:
        with output_lock:
            Token_checked +=1
            valid_tokens+=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Valid Token{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
            open('Tokens_Data/Valid_Tokens', 'a').write(f'{token}\n')
            Token_Checker_title()
            if data['premium_type'] == 2:
                with output_lock:
                    Tokens_withnitro +=1
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}*{gray}) {yellow}Nitro Token{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
                    open('Tokens_Data/Nitro_Tokens', 'a').write(f'{token}\n')
                    Token_Checker_title()  
            if data['email'] and data['verified'] == True:
                with output_lock:
                    verified_tokens +=1
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({blue}/{gray}) {blue}Verified Token{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
                    open('Tokens_Data/Verified_Tokens', 'a').write(f'{token}\n')
                    Token_Checker_title()  
    else:
        with output_lock:
            Token_checked +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {red}Invalid Token{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
            open('Tokens_Data/Invalid_tokens', 'a').write(f'{token}\n')
            Token_Checker_title()
def Server_Spammer(session,token,channel,message,howmany):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    } 
    payload = {
        'content': message
    } 
    for _ in range(int(howmany)):
        while True:
            try:
                send = session.post(f'https://discord.com/api/v9/channels/{channel}/messages', json=payload);break
            except:
                continue
        if send.status_code == 200:
            with output_lock:
                Message_send +=1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Message Send To{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{channel}\n", Colors.red_to_blue, interval=0.000)
        else:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {red}Error Sending Message To{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{channel}\n", Colors.red_to_blue, interval=0.000)

def Webhook_Deleter(session,webhook):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    try:
        delete = session.delete(webhook)
        if delete.status_code == 204:
            with output_lock:
                Deleted +=1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Webhook Deleted{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{str(webhook[:70])}*****\n", Colors.red_to_blue, interval=0.000)
                Webhook_Deleter_title()
        else:
            with output_lock:
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {red}Could't Delete Webhook{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{str(webhook[:70])}*****\n", Colors.red_to_blue, interval=0.000)
                Webhook_Deleter_title() 
    except Exception as e: 
        print(f'Error > {e}')

def Webhook_Spammer(session,webhook, message, times):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    payload = {
        'content':message
    }
    for _ in range(int(times)):
        while True:
            try:
                send = session.post(webhook,json=payload);break
            except:
                continue
        if send.status_code == 204:
            with output_lock:
                Message_send +=1
                time_rn = get_time()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Message Send To{gray} | ", end="")
                sys.stdout.flush()
                Write.Print(f"{str(webhook[:70])}*****\n", Colors.red_to_blue, interval=0.000)
                Webhook_Spammer_title() 
def VC_joiner(token,server_id,channel_id,mute,deaf,stream,video):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}/{gray}) {magenta}Joining Vc{gray} | ", end="")
    joiner = WebSocket()
    joiner.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    joiner.send(json.dumps(
        {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": "windows",
                    "$browser": "Discord",
                    "$device": "desktop"
                }
            }
        }))
    joiner.send(json.dumps({
        "op": 4,
        "d": {
            "guild_id": server_id,
            "channel_id": channel_id,
            "mute": mute,
            "deaf": deaf, 
            "stream": stream, 
            "video": video
        }
    }))
    with output_lock:
        vc_joined +=1
        time_rn = get_time()
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Joined VC{gray} | ", end="")
        sys.stdout.flush()
        Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
        VC_joiner_title
def Pfp_Changer(session,token,image):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    }
    payload = {
        "avatar":f"data:image/png;base64,{image}"
    }
    while True:
        try:
            change_pfp = session.patch('https://discord.com/api/v9/users/@me', json=payload)
            break
        except:
            continue
    if change_pfp.status_code == 200:
        with output_lock:
            pfp_changed +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Pfp Changed{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
    elif change_pfp.status_code == 400 and 'captcha_key' in change_pfp.text:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {yellow}Captcha Required{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {red}Unknown Error{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
def Nickname__bio_Changer(session,token,nickname,bio):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed,bio_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    }
    nickname_payload = {
        "global_name":nickname
    }
    bio_payload = {
        "bio":bio
    }
    while True:
        try:
            change_nickname = session.patch('https://discord.com/api/v9/users/@me', json=nickname_payload);break
        except:
            continue
    if change_nickname.status_code == 200:
        with output_lock:
            nickname_changed +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Nickname Changed{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}", Colors.red_to_blue, interval=0.000)
            Nickname__bio_Changer_title() 
    elif change_nickname.status_code == 400 and 'captcha_key' in change_nickname.text:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {green}Could't Change Nickname{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"Captcha Required", Colors.red_to_blue, interval=0.000)
            Nickname__bio_Changer_title() 
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {green}Unknown Error{gray} | ", end="")
            Nickname__bio_Changer_title()
    while True:
        try:
            change_bio = session.patch('https://discord.com/api/v9/users/%40me/profile', json=bio_payload);break
        except:
            continue
    if change_bio.status_code == 200:
        with output_lock:
            bio_changed +=1
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Bio Changed{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{token}\n", Colors.red_to_blue, interval=0.000)
            Nickname__bio_Changer_title() 
    else:
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {green}Unknown Error{gray} | ", end="")
            Nickname__bio_Changer_title()
def Member_Spammer(session,token,member_id,message, times):
    global Joined,Token_checked,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    output_lock = threading.Lock()
    session = check_useproxies()
    session.headers = {
        'authorization': token,
    }
    grab_channel_payload = {
        'recipients': [
            member_id,
        ],
    }
    while True:
        try:
            grab_channel = session.post('https://discord.com/api/v9/users/@me/channels', json=grab_channel_payload)
            break
        except:
            continue
    if grab_channel.status_code == 200:
        channel_id = grab_channel.json()['id']
        with output_lock:
            time_rn = get_time()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({blue}/{gray}) {blue}Grabbed Channel Id{gray} | ", end="")
            sys.stdout.flush()
            Write.Print(f"{channel_id}\n", Colors.red_to_blue, interval=0.000)
            Member_Spammer_title() 
        paylaod = {
            'content':message
        }
        for _ in range(int(times)):
            while True:
                try:
                    spam = session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', json=paylaod)
                    break
                except:
                    continue
            if spam.status_code == 200:
                with output_lock:
                    Message_send +=1
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {green}Message Send To{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{member_id}\n", Colors.red_to_blue, interval=0.000)
                    Member_Spammer_title() 
            else:
                with output_lock:
                    time_rn = get_time()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {red}Could't Send Message To{gray} | ", end="")
                    sys.stdout.flush()
                    Write.Print(f"{member_id}\n", Colors.red_to_blue, interval=0.000)
                    Member_Spammer_title() 
def Z3R0Raid():
    global Joined,Token_checked,valid_tokens,Message_send,Deleted,vc_joined,pfp_changed,nickname_changed
    with open('config.json','r') as d:
        data = json.load(d)
        threads_num = data['threads']
    Write.Print(f'''
                        ███████╗██████╗ ██████╗  ██████╗ ██████╗  █████╗ ██╗██████╗   ║ Tokens > {lol}
                        ╚══███╔╝╚════██╗██╔══██╗██╔═████╗██╔══██╗██╔══██╗██║██╔══██╗  ║ Proxies > {proxies}
                          ███╔╝  █████╔╝██████╔╝██║██╔██║██████╔╝███████║██║██║  ██║  ║═══════════════
                         ███╔╝   ╚═══██╗██╔══██╗████╔╝██║██╔══██╗██╔══██║██║██║  ██║  ║ Discord:
                        ███████╗██████╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║██║██████╔╝  ║ .gg/Gghebbdf
                        ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝   ╚═══════════════

                                       by ~Z3R003~ | https://github.com/Z3R003
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════                  
                    [01] Server Spammer          [04] Webhook Deleter        [07] Nickname/Bio Changer                
                    [02] Server Joiner           [05] Webhook Spammer        [08] Member Spammer           
                    [03] Token Checker           [06] VC joiner              [09] Pfp Changer  
                   '''                                    
    , Colors.red_to_blue, interval=0.000)
    choice = input(f""" {blue}
┌──{red}(Z3R0Raid@skid){blue} ~ [{red}Ϟ{blue}]
└─> """)
    threads = []
    session = check_useproxies()
    if choice == '01' or choice == '1':
        file = input(f'{red}[{blue}?{red}] Tokens File (tokens.txt) > ')
        choosee = input(f'{red}[{blue}?{red}] Spam One Channel(1) / Spam Many Channels (2) (1,2)> ')
        if choosee == '1':
            channel = input(f'{red}[{blue}?{red}] Channel id (tokens must be in server) > ')
            message = input(f'{red}[{blue}?{red}] Message you want to spam > ')
            howmany = input(f'{red}[{blue}?{red}] How many times each token > ')
            with open(file,'r') as t:
                tokens = t.read().splitlines()
            print('\n')
            for token in tokens:
                t = threading.Thread(target=Server_Spammer, args=(session,token,channel,message,howmany))
                t.start()
                threads.append(t)
            update_title_threads = threading.Thread(target=Server_Spammer_title)
            update_title_threads.start()
            threads.append(update_title_threads)
            for thread in threads:
                thread.join()
        elif choosee == '2':
            input(f'{reset}Pls put all channels id in "channels_ids.txt" file and reopen the tool! if you did it,Enter to continue!')
            message = input(f'{red}[{blue}?{red}] Message you want to spam > ')
            howmany = input(f'{red}[{blue}?{red}] How many times each token > ')
            with open(file,'r') as t:
                tokens = t.read().splitlines()
            with open('channels_ids.txt','r') as c:
                channels = c.read().splitlines()
            print('\n')
            for channel in channels:
                for token in tokens:
                    t = threading.Thread(target=Server_Spammer, args=(session,token,channel,message,howmany))
                    t.start()
                    threads.append(t)
                update_title_threads = threading.Thread(target=Server_Spammer_title)
                update_title_threads.start()
                threads.append(update_title_threads)
                for thread in threads:
                    thread.join()
        print('\n')
        print(f'{red}[{blue}!{red}] {green} Finished!{reset}{blue} Send: {yellow}{Message_send} Messages')
        input(f'{reset}Enter to go back...')
        clear_screen()
        Write.Print('Give it a star or you gay ',Colors.red, interval=0.000)
        time.sleep(2)
        clear_screen()
        Z3R0Raid()
    if choice == '02' or choice == '2':
        file = input(f'{red}[{blue}?{red}] Tokens File (tokens.txt) > ')
        invite = input(f'{red}[{blue}?{red}] Invite Code > https://discord.gg/')
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        start_time1 = time.time()
        print('\n')
        for token in tokens:
            t = threading.Thread(target=Server_Joiner, args=(session,token,invite))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Server_Joiner_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        current_time = time.time()
        elapsed_time = current_time - start_time1
        elapsed_hours = int((elapsed_time % 86400) // 3600)
        elapsed_minutes = int((elapsed_time % 3600) // 60)
        elapsed_seconds = int(elapsed_time % 60)
        print('\n')
        print(f'{red}[{blue}!{red}] {green} Finished!{reset}{blue} Joined: {yellow}{Joined} Tokens {blue}To {red}https://discord.gg/{invite} In {green}{red}{elapsed_hours}h {elapsed_minutes}m {elapsed_seconds}s {reset}')
        input('Enter to go back...')
        clear_screen()
        Write.Print('Give it a star or you gay ',Colors.red, interval=0.000)
        time.sleep(2)
        clear_screen()
        Z3R0Raid()
    if choice == '03' or choice == '3':
        file = input(f'{red}[{blue}?{red}] Tokens File (tokens.txt) > ')
        try:
            os.mkdir('Tokens_Data') 
        except:
            pass
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        print('\n')
        for token in tokens:
            time.sleep(0.3)
            t = threading.Thread(target=Token_Checker, args=(session,token))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Token_Checker_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        print('\n')
        Write.Print('[!] Calculating Stats...', Colors.red_to_blue, interval=0.002)
        invalid_tokens = Token_checked-valid_tokens
        print(f'''                  
{gray}╔════════════════════════════╗
{gray}║     {yellow}Token Checker Stats{reset}  {gray}  ║
{gray}╔════════════════════════════╗
{gray}      {pink}Total Checked {red}  > {pink}{Token_checked}{reset}   
{gray}      {pink}Valid Tokens {red}   > {green}{valid_tokens}{reset}     
{gray}      {pink}Verified Tokens {red}> {blue}{verified_tokens}{reset} 
{gray}      {pink}Nitro Tokens {red}   > {yellow}{Tokens_withnitro}{reset} 
{gray}      {pink}Invalid Tokens {red} > {red}{invalid_tokens}{reset} 
{gray}╚════════════════════════════╝    {reset}   
''')
        Write.Print('[!] Saved The Data In "Tokens_Data" Folder!\n', Colors.red_to_blue, interval=0.009)
        input('Enter to go back...')
        clear_screen()
        Write.Print('Give it a star or you gay ',Colors.red, interval=0.000)
        time.sleep(2)
        clear_screen()
        Z3R0Raid()
    if choice == '04' or choice == '4':
        webhook = input(f'{red}[{blue}?{red}] webhook > ')
        print('\n')
        Webhook_Deleter(webhook)
        input('\nEnter to go back...')
        clear_screen()
        Write.Print('Give it a star or you gay ',Colors.red, interval=0.000)
        time.sleep(2)
        clear_screen()
        Z3R0Raid()
    if choice == '05' or choice == '5':
        webhook = input(f'{red}[{blue}?{red}] Webhook > ')
        message = input(f'{red}[{blue}?{red}] Message > ')
        howmany = input(f'{red}[{blue}?{red}] How many times > ')
        print('\n')
        for _ in range(threads_num):
            t = threading.Thread(target=Webhook_Spammer, args=(session,webhook,message,howmany))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Token_Checker_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
    if choice == '06' or choice == '6':
        file = input(f'{red}[{blue}?{red}] Tokens File (tokens.txt) > ')
        server_id = input(f'{red}[{blue}?{red}] Server_Id > ')
        channel_id = input(f'{red}[{blue}?{red}] Channel_Id > ')
        mute = input(f'{red}[{blue}?{red}] Mute (y,n) > ')
        deaf = input(f'{red}[{blue}?{red}] Deaf (y,n) > ')
        stream = input(f'{red}[{blue}?{red}] Stream (y,n) > ')
        video = input(f'{red}[{blue}?{red}] Video (y,n) > ')
        if mute == 'y' or mute == 'yes':
            mute = True
        else:
            mute == False
        if deaf == 'y' or deaf == 'yes':
            deaf = True
        else:
            deaf == False
        if stream == 'y' or stream == 'yes':
            stream = True
        else:
            stream == False
        if video == 'y' or video == 'yes':
            video = True
        else:
            video == False
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        print('\n')
        for token in tokens:
            t = threading.Thread(target=VC_joiner, args=(server_id,channel_id,mute,deaf,stream,video))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=VC_joiner_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        Write.Print(f'\n [!] Finished! {vc_joined} Tokens Joined Vc!', Colors.red_to_blue, interval=0.009)
        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('Give it a star or you gay ',Colors.red, interval=0.000)
        time.sleep(2)
        clear_screen()
        Z3R0Raid()
    if choice == '07' or choice == '7':
        file = input(f'{red}[{blue}?{red}] Tokens File (tokens.txt) > ')
        nickname = input(f'{red}[{blue}?{red}] Nickname > ')
        bio = input(f'{red}[{blue}?{red}] Bio > ')
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        print('\n')
        for token in tokens:
            t = threading.Thread(target=Nickname__bio_Changer, args=(session,token,nickname,bio))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Nickname__bio_Changer_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        Write.Print(f'\n [!] Finished! Changed : {nickname_changed} Nicknames | Changed : {bio_changed} Bios!', Colors.red_to_blue, interval=0.009)
        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('Give it a star or you gay ',Colors.red, interval=0.000)
        time.sleep(2)
        clear_screen()
        Z3R0Raid()
    if choice == '08' or choice == '8':
        file = input(f'{red}[{blue}?{red}] Tokens File (tokens.txt) > ')
        member_id = input(f'{red}[{blue}?{red}] Member Id You want to spam > ')
        message = input(f'{red}[{blue}?{red}] Message you want to spam > ')
        howmany = input(f'{red}[{blue}?{red}] How many messages you want to send (each token) > ')
        with open(file,'r') as t:
            tokens = t.read().splitlines()
        for token in tokens:
            t = threading.Thread(target=Member_Spammer, args=(session,token,member_id,message,howmany))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Member_Spammer_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        Write.Print(f'\n [!] Finished! Send : {Message_send} To {member_id}', Colors.red_to_blue, interval=0.009)
        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('Give it a star or you gay ',Colors.red, interval=0.000)
        time.sleep(2)
        clear_screen()
        Z3R0Raid()

    if choice == '09' or choice == '9':
        file = input(f'{red}[{blue}?{red}] Tokens File (tokens.txt) > ')
        image_file = input(f'{red}[{blue}?{red}] Image File > ')
        with open('tokens.txt','r') as t:
            tokens = t.read().splitlines()
        with open(image_file, 'rb') as i:
            image_data = i.read()
        encoded_image = base64.b64encode(image_data)
        print('\n')
        for token in tokens:
            t = threading.Thread(target=Pfp_Changer, args=(session, token,encoded_image))
            t.start()
            threads.append(t)
        update_title_threads = threading.Thread(target=Pfp_Changer_title)
        update_title_threads.start()
        threads.append(update_title_threads)
        for thread in threads:
            thread.join()
        Write.Print(f'\n [!] Finished! Changed Pfp To : {pfp_changed} Tokens', Colors.red_to_blue, interval=0.009)
        input(f'{reset}\n Enter to go back!')
        clear_screen()
        Write.Print('Give it a star or you gay ',Colors.red, interval=0.000)
        time.sleep(2)
        clear_screen()
        Z3R0Raid()
    else:
        clear_screen()
        print(f'{cyan}[{red}!{cyan}]{red} Invalid choice', end=' ')
        [print('.', end='', flush=True) or time.sleep(0.7) for _ in range(3)]
        clear_screen()
        Z3R0Raid()

if __name__ == '__main__':
    Z3R0Raid()
