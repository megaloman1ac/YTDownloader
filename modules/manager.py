from enum import Enum

class Manager:
	"""

	-- Manager (file) --
	Uses for contains the variables that will be use in other files in the project
	The following modules use these variables:
	- Video.py (main file for downloading videos)
	- Display.py (main file for display messages in CLI)
	
	-- Manager (class) --
	Uses for contains and gives access to variables

	"""
	
	
	start=True
	
	video_resolutions=[]
	video=[]
	channel_name = "DEFAULT"
	ipt = ""
	link = ""
	
	
	class Type(Enum):
		def __str__(self):
			return str(self.value.upper())
		
		TTL = "Title"
		RES = "resolution"
		INF = "Info"
		ERR = "error"
		WRN = "warning"
		CMT = "complete"
		INP = "input"
		VID = "Video"
		CNL = "Channel"
		THN = "Thumbnail"
		VIN = "Video Info"
		CIN = "Channel Info"
