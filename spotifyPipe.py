# Name: Gagan Gupta
# Date: 03/18/2020
# Description: Discord Bot Spotify API extension

import json
import subprocess

# Your Client ID
client_id=""
# Your Client Secret
client_secret=""
# Base 64 encoding of client_id:client_secret
clientTag=""
cmd = "curl -X \"POST\" -H \"Authorization: Basic "+clientTag+"\" -d grant_type=client_credentials https://accounts.spotify.com/api/token"
auth=(json.loads(subprocess.check_output(cmd).decode("utf-8")))["access_token"]

# URI Playlist code
playlistcode = ""
limit = 100
offset = 0
cmd = "curl -X \"GET\" \"https://api.spotify.com/v1/playlists/"+playlistcode+"/tracks?market=ES&fields=total%2Citems(track(name%2Cartists))&limit="+str(limit)+"&offset="+str(offset)+"\" -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer "+auth+"\""
data=json.loads(subprocess.check_output(cmd).decode("utf-8"))

songs = []
total = int(data["total"])
left = total
if(total>100):
	limit=100
if(total>0 and total<100):
	limit=total

i=0
while(left>0):
	print("Left:"+str(left)+" Limit:"+str(limit)+" Offset:"+str(offset)+"\n\n")
	cmd = "curl -X \"GET\" \"https://api.spotify.com/v1/playlists/"+playlistcode+"/tracks?market=ES&fields=total%2Citems(track(name%2Cartists))&limit="+str(limit)+"&offset="+str(offset)+"\" -H \"Accept: application/json\" -H \"Content-Type: application/json\" -H \"Authorization: Bearer "+auth+"\""
	data=json.loads(subprocess.check_output(cmd).decode("utf-8"))
	for song in data["items"]:
		songs.append([])
		songs[i].append((song["track"])["name"])
		for artist in (song["track"])["artists"]:
			songs[i].append(artist["name"])
		i+=1
	left=left-limit
	offset=total-left
	if(total>100):
		limit=100
	if(total>0 and total<100):
		limit=left


i=0
for row in songs:
	i+=1
	playChain = "$play " + row[0] + " " + row[1]
	print(playChain)
print(i)
