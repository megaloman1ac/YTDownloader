from pytube import YouTube
from modules.manager import *
from pytube import Channel
from modules.display import *
import time
import os
import re

def buff():
	
	sort()
	download()
	
def sort():
	
	yt = YouTube(Manager.link)
	channel=Channel(yt.channel_url)
	
	display_message("wht", Manager.Type.CIN, "", "\n")
	
	display_message("blk", Manager.Type.CNL, f"{channel.channel_name}", "\n")
	
	display_message("wht", Manager.Type.VIN, "", "\n")
	
	Manager.channel_name = re.sub(r'[►]','_', channel.channel_name)
	Manager.channel_name = re.sub(r'\s','_', Manager.channel_name)
	Manager.channel_name = re.sub(r'_+','_', Manager.channel_name)
	Manager.channel_name = Manager.channel_name.lower()
	
	

	display_message("blk", Manager.Type.TTL, f"{yt.title}", "\n")
	display_message("blk", Manager.Type.THN, f"{yt.thumbnail_url}", "\n")
	
	"""
	while True:
		
		thumb = input("Save the thumbnail? (Y(y)/N(n))\n")
		if thumb == "y" or thumb == "Y":
			ext='jpg'
			
			os.system(f"bash ./modules/get_thumbnail.sh {yt.thumbnail_url} {yt.title.replace(' ','_')} {ext}")
			break;
		elif thumb == "n" or thumb == "N":
			print("ss")
			break;
		else:
			print("Uncorrect")
		"""
	
	
	for stream in yt.streams.filter(audio_codec='mp4a.40.2').order_by('resolution'):
		Manager.video_resolutions.append(stream.resolution)
		Manager.video.append(stream)

def download():
	
	while True:
		i=1
		for resolution in Manager.video_resolutions:
			display_message("blk", Manager.Type.RES, f'{i}. {resolution}', "\n")
			i += 1
		
		display_message("blk", Manager.Type.INF, f"There is {i - 1} video resolution to download.", "\n")
		display_message("blk", Manager.Type.INF, f"Manual download (m) or download all of them (a)?", "\n")
		display_message("blk", Manager.Type.INP, "", "")
		
		Manager.ipt = input()
		
		if Manager.ipt == "!next":
			Manager.start = False
			break;
		
		try:			
			
			yt = YouTube(Manager.link)
			
			if(Manager.ipt.lower() == "a"):
				
				choice = 1
				while choice < i:
					vid_title = re.sub(r'\s', '_', yt.title)
					vid_title = re.sub(r'[►]','_', vid_title)
					vid_title = re.sub(r'[:]','-', vid_title)
					resolution=Manager.video_resolutions[choice - 1]
					display_message("ylw", Manager.Type.INF, f"{resolution} is now downloading...", "\n")				
					Manager.video[choice - 1].download(output_path = f"./data/{Manager.channel_name}/{vid_title}/", filename=f"{resolution}_{vid_title}.mp4")
					display_message("grn", Manager.Type.CMT, f"{resolution} downloaded !", "\n")
					desc = os.path.isfile(f"./data/{Manager.channel_name}/{vid_title}/description.txt")
					if desc != True:
						os.system(f"echo \"{yt.description}\" > \"./data/{Manager.channel_name}/{vid_title}/description.txt\"")
					choice += 1
					
				display_message("grn", Manager.Type.CMT, f"All videos have been downloaded", "\n")
				
				time.sleep(1.5)
				
				Manager.start = False
				
				break;
				
			
			elif Manager.ipt.lower() == "m":
				
				display_message("blk", Manager.Type.INF, f"Enter a number of resolution", "\n")
				display_message("blk", Manager.Type.INP, "", "")
				
				choice = int(input())
				
				vid_title = re.sub(r'\s', '_', Manager.video[choice - 1].title)
				vid_title = re.sub(r'\s', '_', yt.title)
				vid_title = re.sub(r'[►]','_', vid_title)
				vid_title = re.sub(r'[:]','-', vid_title)
				
				resolution=Manager.video_resolutions[choice-1]
				
				display_message("ylw", Manager.Type.INF, f"{resolution} is now downloading...", "\n")
				
				Manager.video[choice - 1].download(output_path = f"./data/{Manager.channel_name}/{vid_title}/", filename=f"{resolution}_{vid_title}.mp4")
				
				desc = os.path.isfile(f"./data/{Manager.channel_name}/{vid_title}/description.txt")
				
				if desc != True:
					os.system(f"echo \"{yt.description}\" > \"./data/{Manager.channel_name}/{vid_title}/description.txt\"")
			
				display_message("grn", Manager.Type.CMT, f"{resolution} downloaded !", "\n")
				
				display_message("wht", Manager.Type.INF, f"You can download another video. Write \"!next\"", "\n")
			else:
				display_message("rd", Manager.Type.ERR, f"Write only a(all) or m(manual)", "\n")
			
		except ValueError:
			display_message("rd", Manager.Type.ERR, f"Only numbers", "\n")

	
