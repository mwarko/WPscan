import urllib.request
import sys
import os

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

chaine = "wordpress"
adresse = str(input("Nom du site: "))
request = urllib.request.Request('http://' + adresse,None,headers)
response = urllib.request.urlopen(request)
content = response.read()
fichier = open("source.txt","a")
fichier.writelines(str(content).lower())
fichier.close()
fichier = open("source.txt","r")
for string in fichier:
	if chaine in string:
		print("Ce site est probablement fait avec wordpress")
		break
	else:
		print("Ce site n'est probablement pas un site wordpress")
fichier.close()
os.remove("source.txt")

quit = str(input("Tapez sur une touche pour quitter..."))


