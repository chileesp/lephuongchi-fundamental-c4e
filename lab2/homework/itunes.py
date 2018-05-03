from urllib .request import urlopen
from bs4 import BeautifulSoup


url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)

raw_data = conn.read()

text = raw_data.decode('utf8')

soup = BeautifulSoup(text, "html.parser")
section = soup.find("section","section chart-grid")
ul = section.find("ul")

li_list = ul.find_all("li")

item_list = []

for li in li_list:
    song = li.h3.a
    songname = song.string
    artist = li.h4.a
    artistname = artist.string
    item = {
        "Songs": songname,
        "Artist": artistname
    }
    item_list.append(item)



import pyexcel
pyexcel.save_as(records=item_list, dest_file_name="itunestop.xlsx")
