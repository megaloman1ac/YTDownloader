from modules.display import *
from modules.manager import *
from modules.playlist import *
from modules.video import *

def checking():
	
	if len(Manager.ipt) <= len("https://www.youtube.com/"):
		display_message("ylw", Manager.Type.INF, "This link is too small", "\n")
	else:
		if "watch" in Manager.ipt:
			Manager.link = Manager.ipt
			buff()


while True:
	
	Manager.video.clear()
	Manager.video_resolutions.clear()
	
	if Manager.start == True:
		clear()

	display_message("blk", Manager.Type.INP, "", "")

	Manager.ipt = input()
	
	if Manager.ipt == "!exit":
		break;
	
	checking()
