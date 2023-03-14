from os import system
from modules.playlist import *
from modules.video import *

def checking(link):
	def_link = "https://www.youtube.com/"
	
	if len(link) <= len(def_link):
		print("Too small...")
	else:
		if "watch" in link:
			buff(link)

system("clear")

link = input("[ LINK ] > ")

checking(link)
