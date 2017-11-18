import pandas as pd

import getLyrics

df = pd.read_csv("lyrics.csv", encoding="latin1")  # Yes latin1 is necessary

httt = df[df["album"] == "Hail to the Thief"]
for row in httt.iterrows():
    input(row)
    print()

# print(df[df["album"] == "Hail to the Thief"])
