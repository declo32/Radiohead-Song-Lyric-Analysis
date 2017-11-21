import pandas as pd
import time

import getLyrics

df = pd.read_csv("lyrics.csv", index_col=0, encoding="latin1")  # Yes latin1 is necessary

for i, song in df[df["album"] == "Hail to the Thief"].iterrows():
    title = df.loc[i, "title"].split(" (")[0]  # Get the first title, before parentheses
    df.loc[i, "lyrics"] = getLyrics.get_lyrics("Radiohead", title)
    print(df.loc[i])

    print("\nWaiting 60s...")  # Don't want to get locked out
    for x in range(60):
        print(x)
        time.sleep(1)

with open("lyrics.csv", "w", newline="\n") as file:  # I'm on windows :(
    df.to_csv(file)
