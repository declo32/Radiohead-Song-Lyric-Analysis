import pandas as pd
import re


def rep(s):
    """Fix repetition"""
    return_val = ""
    regex = re.compile(r"^(?P<content>.+)\s<i>\[x?(?P<num>\d+)x?\]</i>$")  # Blah <i>[x10]</i>

    for line in s.splitlines():
        match = re.match(regex, line)
        if match:
            return_val += (match.group("content") + " ") * int(match.group("num"))
        else:
            return_val += line
        return_val += "\n"

    return return_val


df = pd.read_csv("lyrics.csv", index_col=0, encoding="latin1")

for i, song in df[df["lyrics"].notnull()].iterrows():  # Only notnull lyrics
    df.loc[i, "lyrics"] = rep(song["lyrics"])

with open("lyrics.csv", "w", newline="\n") as file:  # I'm on windows :(
    df.to_csv(file)
