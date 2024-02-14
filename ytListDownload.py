#!/usr/bin/env python3

import psutil,colorama,signal,os,time,sys,pdb
from colorama import Fore, Style, init
init()

def sig_handler(sig, frame):
    print(Fore.RED + "\n\n[!] Saliendo...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

def downloadVideos():
	with open(path,'r') as file :
		line = file.readline().strip()
		otherUrls= file.readlines()
	while line:
		parts = line.split('|')
		url = parts[0].strip()
		format = parts[1].strip()
		if format == "V" :
			os.system(f"python3 youtube-dl.py -f 'best[height<=720]/best[ext=mp4]/best' -o '{folder}/Vídeos/%(title)s-%(channel)s.%(ext)s' --no-warnings {url}")
		else :
			os.system(f"python3 youtube-dl.py -f 'bestaudio[ext=m4a]/bestaudio' -o '{folder}/Podcasts/%(title)s-%(channel)s.%(ext)s' --no-warnings {url}")
		with open(path,'w') as file :
			file.writelines(otherUrls)
		with open(path,'r') as file :
			line = file.readline().strip()
			otherUrls= file.readlines()

if __name__ == "__main__":
	path="/home/user/PATH/links.txt" #ruta absoluta del archivo con los links
	# EJEMPLO DEL CONTENIDO DEL ARCHIVO links.txt (no incluye los paréntesis)
	# https://www.youtube.com/watch?v=example  | P (se descargará en m4a en la subcarpeta "Podcasts")
	# https://www.youtube.com/watch?v=example2 | V (se descargará en mp4 en la subcarpeta "Vídeos")
	folder="/home/usr/PATH/YTDownloads" #ruta absoluta de la carpeta de descargas

	print(f"\n{Fore.YELLOW}[+] Iniciando descargas ... {Style.RESET_ALL}\n")
	downloadVideos()
	print(Fore.GREEN + "\n[#] Todos descargado con éxito" + Style.RESET_ALL)
	time.sleep(1)
	sig_handler(None,None)
























