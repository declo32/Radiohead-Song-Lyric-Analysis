import pandas as pd
import time

import getLyrics

df = pd.read_csv("lyrics.csv", index_col=0, encoding="latin1")

titles = {
    "How Do You Do?": "How Do You?",
    "High and Dry": "High & Dry",
    "Packt Like Sardines in a Crushd Tin Box": "Packt Like Sardines in a Crushed Tin Box",
    "Pulk/Pull Revolving Doors": "Pull / Pulk Revolving Doors",
    "Morning Bell/Amnesiac": "Amnesiac / Morning Bell",
}

for i, song in df[df["lyrics"].isnull()].iterrows():  # All null lyrics
    if df.loc[i, "title"] in titles:
        title = titles[df.loc[i, "title"]]
        df.loc[i, "lyrics"] = getLyrics.get_lyrics("Radiohead", title)
        print(df.loc[i])

        print("Waiting 60s...")
        for x in range(60):
            print(x)
            time.sleep(1)
    else:
        df.loc[i, "lyrics"] = ""
        print(df.loc[i])

with open("lyrics.csv", "w", newline="\n") as file:  # I'm on windows :(
    df.to_csv(file)
