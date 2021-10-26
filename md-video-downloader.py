"""
Algorithim:
1. Extract the html file of website via curl
2. Look for a string starting with rvideos1.memedroid.com
   and ending with .mp4
3. extract that string, and curl that into a file

Note: dont try to request the same video a lot in a short amount of time or they will change the link
"""

import os
import sys

class GlobalVariables:
	tempFileName = ""
	videoLink = ""
	websiteStr = ""

def ExtractWebsiteName(string):
	string = string.replace("/>", "")
	string = string.replace("<meta property=\"og:video:secure_url\" content=\"", "")
	string = string.replace("\"", "")

	return string
		

def PrintUsageMsg():
	print("Usage: [link to videomeme]")


def ArgHandler(globalVars):
	if len(sys.argv) > 2 or len(sys.argv) < 2:
		print("Error: too many or too few arguements", file=sys.stderr)
		PrintUsageMsg()
		raise SystemExit()
	else:
		#global websiteStr
		globalVars.websiteStr = str(sys.argv[1])




globalVars = GlobalVariables()
ArgHandler(globalVars)

#downloading html file of the website and extracting the video website
os.system("curl " + globalVars.websiteStr + " >> websiteContent.html")
websiteContent = open("websiteContent.html")
websiteLines = websiteContent.readlines()
linkFound = False
for line in websiteLines:
	if ("https://rvideos1.memedroid.com/" in line) and (".mp4" in line):
		linkFound = True
		globalVars.videoLink = line
		print(line)
		break
if linkFound == False:
	print("Error: video link not found")
globalVars.videoLink = ExtractWebsiteName(globalVars.videoLink)
print(globalVars.videoLink)


#os.remove("VideoOutput.mp4")
#downloading the video itself
os.system("curl --output VideoOutput.mp4 " + globalVars.videoLink)

#removing temp file
print("Cleaning up...")
os.remove("websiteContent.html")

print("Video extraction finished")