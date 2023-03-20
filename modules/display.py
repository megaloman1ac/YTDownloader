from modules.manager import *
from colorama import Fore, Back, Style
import os

def clear():
	os.system("clear")

def display_message(bkg_color, msg_type, message, ends_with):
	
	if bkg_color == "blk":
		print(Back.BLACK + f"[ {str( msg_type ).center(12)} ]" + Back.BLACK + " : {0}".format(message), end=ends_with )
	if bkg_color == "ylw":
		print(Back.YELLOW + f"[ {str( msg_type ).center(12)} ]" + Back.BLACK + " : {0}".format(message), end=ends_with )
	if bkg_color == "rd":
		print(Back.RED + f"[ {str( msg_type ).center(12)} ]" + Back.BLACK + " : {0}".format(message), end=ends_with )
	if bkg_color == "grn":
		print(Back.GREEN + f"[ {str( msg_type ).center(12)} ]" + Back.BLACK + " : {0}".format(message), end=ends_with )
	if bkg_color == "wht":
		print(Back.WHITE + f"[ {str( msg_type ).center(12)} ]" + Back.BLACK + " : {0}".format(message), end=ends_with )
