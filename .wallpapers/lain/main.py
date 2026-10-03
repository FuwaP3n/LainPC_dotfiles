import os
papers = os.listdir(os.getcwd() + "/")
i = 0
for paper in papers:
    if paper == "main.py":
        continue
    filename = os.getcwd() + "/" + paper
    new_filename = os.getcwd()+"/wallpaper"+str(i)+".jpg"
    os.rename(filename, new_filename)
    command = "ffmpeg -i " + new_filename + " " + os.getcwd() + "/wallpaper" + str(i) + ".png"
    os.system(command)
    os.remove(new_filename)
    i += 1
