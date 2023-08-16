from tkinter import *
from pytube import YouTube
from pytube import Playlist
import os
import re

# Window Creation
window = Tk()
window.geometry("800x450")
window.resizable(0, 0)
window.title('YouTube Downloader')
window.configure(bg="#eee")

def download():
    url = str(urlInput.get())
    outFile = ""
    destination = str(filePathInput.get())
    if ("playlist" in url):
        url = Playlist(url)
        for video in url.videos:
            video._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            video = video.streams.filter(only_audio=True).first()
            outFile = video.download(output_path=destination)
            if (outFile != ""):
                base, ext = os.path.splitext(outFile)
                newFile = base + '.mp3'
                os.rename(outFile, newFile)
    else:
        url = YouTube(url)
        video = url.streams.filter(only_audio=True).first()
        outFile = video.download(output_path=destination)
        if (outFile != ""):
            base, ext = os.path.splitext(outFile)
            newFile = base + '.mp3'
            os.rename(outFile, newFile)

# Elements
Label(text="Enter YouTube video/playlist url", font=40, fg="black").pack()
Label(text="Click DOWNLOAD to start", font=35, fg="black").pack()
urlInput = Entry(window, width=32)
urlInput.pack()
Label(text="Enter complete file output path:", font=35, fg="black").pack()
filePathInput = Entry(width=32)
filePathInput.pack()
button = Button(text="Download", command=download, width=8, height=2, fg="red").pack(pady=20)

window.mainloop()