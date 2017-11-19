import yaml
import re
import urllib.request
from bs4 import BeautifulSoup
import time
import pandas as pd


# Taken from https://www.quora.com/Whats-a-good-api-to-use-to-get-song-lyrics
def get_lyrics(artist, song_title):
    print("Fetching lyrics for \"{} - {}\":\n".format(artist, song_title))

    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):  # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/" + artist + "/" + song_title + ".html"

    try:
        content = urllib.request.urlopen(url).read()
    except Exception as e:
        print(e)
        return None
    soup = BeautifulSoup(content, 'html.parser')
    lyrics = str(soup)
    # lyrics lies between up_partition and down_partition
    up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
    down_partition = '<!-- MxM banner -->'
    lyrics = lyrics.split(up_partition)[1]
    lyrics = lyrics.split(down_partition)[0]
    lyrics = lyrics.replace('<br>', '').replace('</br>', '').replace('</div>', '').strip()
    return lyrics


if __name__ == '__main__':
    with open("Radiohead-Discography.yaml", "rb") as file:
        radioheadDiscography = yaml.load(file)

    df = pd.DataFrame()

    for album in radioheadDiscography:
        for key in album:
            for title in album[key]:
                l = get_lyrics("Radiohead", title)
                df = df.append({"artist": "Radiohead", "album": key, "title": title, "lyrics": l}, ignore_index=True)

                print(l)
                print("\nWaiting 60s")
                for x in range(60):  # Don't wan't to get locked out
                    print(x)
                    time.sleep(1)

    df.to_csv("lyrics.csv")
