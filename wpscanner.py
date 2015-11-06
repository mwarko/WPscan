import urllib.request
import sys
import os
import tkinter

fenetre = tkinter.Tk()
fenetre.title("WPscanner By Marc-Antoine FOURNIER")

def scanwp(adresse):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,} 
	chaine = "wordpress"
	request = urllib.request.Request('http://' + adresse,None,headers)
	response = urllib.request.urlopen(request)
	content = response.read()
	fichier = open("source.txt","a")
	fichier.writelines(str(content).lower())
	fichier.close()
	fichier = open("source.txt","r")
	for string in fichier:
		if chaine in string:
			lbl.configure(text="Ce site est probablement fait avec wordpress")
			break
		else:
			lbl.configure(text="Ce site n'est probablement pas un site wordpress")
	fichier.close()
	os.remove("source.txt")


def main():
	addr = texte.get()
	scanwp(addr)


def exxit():
	sys.exit()

lbl = tkinter.Label(fenetre, text="Rentrez le nom du site ici (exemple : google.com)")
texte = tkinter.Entry(fenetre)
btn = tkinter.Button(fenetre, text="OK", command=main)
btnquit = tkinter.Button(fenetre, text="Quitter", command=exxit)
lbl.pack()
btn.pack()
fenetre.pack()

