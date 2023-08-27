from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
import os

# Window Creation
window = Tk()
window.geometry("800x450")
window.resizable(0, 0)
window.title('YouTube Downloader')
window.configure(bg="#eee")

directory = ""

def open_directory():
    directory = filedialog.askdirectory()
    if directory:
        selectedFolder.config(text="Selected Folder: " + directory)


def download():
    url = str(urlInput.get())
    fileType = str(FileClick.get())
    if (fileType == "File Type:"):
        fileType = "mp4"

    quality = str(qualityDefault.get())

    destination = str(selectedFolder.cget("text")).split(": ")[1]

    def downloadURL(url):
        if (fileType == "mp3"):
            if (quality == "High Quality"):
                video = url.streams.filter(
                    only_audio=True).order_by('abr').desc().first()
            elif (quality == "Low Quality"):
                video = url.streams.filter(only_audio=True).order_by('abr').desc().last()
        elif (fileType == "mp4"):
            if (quality == "High Quality"):
                video = url.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').desc().first()
            elif (quality == "Low Quality"):
                video = url.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').desc().last()
        outFile = video.download(output_path=destination)
        if (outFile != ""):
            base, ext = os.path.splitext(outFile)
            newFile = base + "." + fileType
            os.rename(outFile, newFile)

    if (destination != ""):
        if ("playlist" in url):
            playlist = Playlist(url)
            for url in playlist.videos:
                downloadURL(url)
        else:
            url = YouTube(url)
            downloadURL(url)


# Elements
Label(text="Enter YouTube video/playlist url", font=40, fg="black").pack()
Label(text="Click DOWNLOAD to start", font=35, fg="black").pack()

urlInput = Entry(window, width=32)
urlInput.pack()

selectedFolder = Label(window, text="Selected Folder: ", font=40, fg="black")
selectedFolder.pack(pady=(10,0))
openFolder = Button(window, text="Open Folder", command=open_directory, font=30, fg="blue")
openFolder.pack(pady=(0, 10))

fileOptions = ["mp3", "mp4"]
FileClick = StringVar()
FileClick.set("File Type:")
FileDrop = OptionMenu(window, FileClick, *fileOptions)
FileDrop.pack()

qualityOptions = ["High Quality", "Low Quality"]
qualityDefault = StringVar()
qualityDefault.set("High Quality")
qualityDrop = OptionMenu(window, qualityDefault, *qualityOptions)
qualityDrop.pack()

Button(text="Download", command=download, width=8, height=2, fg="red", font="bold").pack(pady=20)

window.mainloop()
