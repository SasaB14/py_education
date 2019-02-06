import re #regular expression
import urllib.request
import json


def daj_ip():
	url = "http://checkip.dyndns.org"
	with urllib.request.urlopen(url) as response:
   		html = response.read().decode('utf8')

	ip_adresa = html[-30:-16]

	return ip_adresa

def daj_longitude(ip_adresa):
	pocetak = "http://api.ipstack.com/" 
	treci_deo = "?access_key="
	kljuc = "c5c4d1e600448d3cc02e418b5f0ba2b2"

	url = pocetak + ip_adresa + treci_deo + kljuc

	with urllib.request.urlopen(url) as response:
   		html = response.read().decode('utf8')

   	

	data = html[-345:-338]

	return data

def daj_latitude(ip_adresa):
	pocetak = "http://api.ipstack.com/" 
	treci_deo = "?access_key="
	kljuc = "c5c4d1e600448d3cc02e418b5f0ba2b2"

	url = pocetak + ip_adresa + treci_deo + kljuc

	with urllib.request.urlopen(url) as response:
   		html = response.read().decode('utf8')

   	

	data = html[-365:-358]

	return data

def daj_vreme(latitude,longitude):
	pocetak = "http://api.openweathermap.org/data/2.5/weather?lat=" 
	sredina = str(latitude)+'&lon='+str(longitude)
	kraj = '&appid=f0f38fe9c2bc1d274c48a91b9f75862f&units=metric'

	url = pocetak + sredina + kraj
	
	with urllib.request.urlopen(url) as response:
   		html = response.read().decode('utf8')

	temp = html[150:154]
	min_temp = html[196]
	max_temp = html[209]

	return temp,min_temp,max_temp
	
'''
print(daj_ip())
print(daj_longitude('109.198.11.165'))
print(daj_latitude('109.198.11.165'))
print(daj_vreme(44.8186,20.4681))
'''
latitude = daj_latitude(daj_ip())
longitude = daj_longitude(daj_ip())

tren_temp, min_temp, max_temp = daj_vreme(latitude,longitude)
print("\nTrenutna temperatura je: ", tren_temp,"stepeni celzijusa")
print("\n\tMaksimalna ocekivana temperatura za danas je: ",max_temp)
print("\n\tMinimalna ocekivana temperatura za danas je: ",min_temp)