#!/usr/bin/env python3


def Project_Loader(Created_By="Ruben Leonardo Sigalingging"):
	from os import system
	system("pip install tqdm")
	system("clear")
	from tqdm import tqdm,trange


	menunggu=int(input("[!] Mau Menunggu Berapa Detik: "))
	if menunggu>=50:
		for kesabaran in trange(menunggu):
			print("[!] Sabar Ya!, Kebahagiaan Membutuhkan Proses!\n")
			from time import sleep
			sleep(0.3)


	elif menunggu<=50:
		for kesabaran in trange(menunggu):
			print("[!] Sabar Ya!, Kebahagiaan Membutuhkan Proses!\n")
			from time import sleep
			sleep(0.3)
Project_Loader()