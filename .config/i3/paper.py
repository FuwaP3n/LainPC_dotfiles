import os
import random

papers = os.listdir("/home/USERNAME/.wallpaper/lain")
while True:
    paper_name = "/home/USERNAME/.wallpaper/lain/" + random.choice(papers)
    if paper_name != "/home/USERNAME/.wallpaper/lain/main.py":
        break

command = "feh --bg-scale " + paper_name

os.system(command)
