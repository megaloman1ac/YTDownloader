from pytube import YouTube
import os

def buff(video_link):	
	video, video_resolution = sort(video_link)
	download(video, video_resolution)

def sort(video_link):
	yt = YouTube(video_link)
	
	print(f"\n[ Video ] : {yt.title}")
	print(f"[ Thumbnail ] : {yt.thumbnail_url}")

	
	while True:
		thumb = input("Save the thumbnail? (Y(y)/N(n))\n")
		if thumb == "y" or thumb == "Y":
			ext='jpg'
			system(f"bash ./modules/get_thumbnail.sh {yt.thumbnail_url} {yt.title.replace(' ','_')} {ext}")
			break;
		elif thumb == "n" or thumb == "N":
			print("ss")
			break;
		else:
			print("Uncorrect")
	
	video_resolutions=[]
	video=[]
	
	for stream in yt.streams.filter(audio_codec='mp4a.40.2').order_by('resolution'):
		video_resolutions.append(stream.resolution)
		video.append(stream)
	
	return video, video_resolutions

def download(video, video_resolutions):
	
	while True:
		i=1
		for resolution in video_resolutions:
			print(f'{i}. {resolution}')
			i += 1
		
		try:
			choice = int(input('Enter a number of resolution to download > '))
			
			if 1 <= choice < i:
				resolution=video_resolutions[choice-1]
				
				print(f"{resolution} is now downloading...")
				
				video[choice - 1].download(filename=f"{resolution}_{video[choice - 1].title}")
				
				print("DONE!")
				
			
		except ValueError:
			print('Number, not a string or something else...')

	
