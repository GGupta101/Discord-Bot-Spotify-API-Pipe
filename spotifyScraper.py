from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36'}

source = requests.get('https://open.spotify.com/playlist/6hWNhuncqey9HVFNZf4QdK?si=dLM5IIIISCOMLZcMaULa3A', headers=headers).text
soup = BeautifulSoup(source, 'lxml')


tracklist = soup.find('ol', attrs={'class': 'tracklist'})
# print(tracklist.prettify())

i=0
songs =[]
for song in soup.find('ol', attrs={'class': 'tracklist'}).find_all("li"):
	songs.append([])
	for name in song.find_all("span"):
		songs[i].append(name.text)
	i+=1

print(soup.prettify())

# for row in songs:
# 	if(len(row)>0):
# 		print(row[0],"by",row[2])