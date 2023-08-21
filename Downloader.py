from tkinter import *
from pytube import YouTube
from pytube import Playlist
import os

# Window Creation
window = Tk()
window.geometry("800x450")
window.resizable(0, 0)
window.title('YouTube Downloader')
window.configure(bg="#eee")

def download():
    url = str(urlInput.get())
    fileType = str(FileClick.get())
    if (fileType == "File Type:"):
        fileType = "mp4"

    audioQuality = str(AudioClick.get())
    if (audioQuality == "Audio Quality:"):
        audioQuality = "High Quality"

    videoQuality = str(VideoClick.get())
    if (videoQuality == "Video Quality:"):
        videoQuality = "High quality"
    video = ""

    destination = str(filePathInput.get())
    if ("playlist" in url):
        url = Playlist(url)
        for url in url.videos:
            if (fileType == "mp3"):
                if (audioQuality == "High Quality"):
                    video = url.streams.filter(only_audio=True).order_by('abr').desc().first()
                elif (audioQuality == "Low Quality"):
                    video = url.streams.filter(only_audio=True).order_by('abr').desc().last()
            elif (fileType == "mp4"):
                if (videoQuality == "High Quality"):
                    video = url.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').desc().first()
                elif (videoQuality == "Low Quality"):
                    video = url.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').desc().last()
            outFile = video.download(output_path=destination)
            if (outFile != ""):
                base, ext = os.path.splitext(outFile)
                newFile = base + "." + fileType
                os.rename(outFile, newFile)
    else:
        url = YouTube(url)
        if (fileType == "mp3"):
            if (audioQuality == "High Quality"):
                video = url.streams.filter(only_audio=True).order_by('abr').desc().first()
            elif(audioQuality == "Low Quality"):
                video = url.streams.filter(only_audio=True).order_by('abr').desc().last()
        elif (fileType == "mp4"):
            if (videoQuality == "High Quality"):
                video = url.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').desc().first()
            elif (videoQuality == "Low Quality"):
                video = url.streams.filter(file_extension="mp4", progressive=True).order_by('resolution').desc().last()
        outFile = video.download(output_path=destination)
        if (outFile != ""):
            base, ext = os.path.splitext(outFile)
            newFile = base + "." + fileType
            os.rename(outFile, newFile)


# Elements
Label(text="Enter YouTube video/playlist url", font=40, fg="black").pack()
Label(text="Click DOWNLOAD to start", font=35, fg="black").pack()

urlInput = Entry(window, width=32)
urlInput.pack()

Label(text="Enter complete file output path:", font=35, fg="black").pack()

filePathInput = Entry(width=32)
filePathInput.pack()

fileOptions = ["mp3","mp4"]
FileClick = StringVar()
FileClick.set("File Type:")
FileDrop = OptionMenu(window, FileClick, *fileOptions)
FileDrop.pack()

audioOptions = ["High Quality", "Low Quality"]
AudioClick = StringVar()
AudioClick.set("Audio Quality:")
AudioDrop = OptionMenu(window, AudioClick, *audioOptions)
AudioDrop.pack()

videoOptions = ["High Quality", "Low Quality"]
VideoClick = StringVar()
VideoClick.set("Video Quality:")
VideoDrop = OptionMenu(window, VideoClick, *videoOptions)
VideoDrop.pack()

button = Button(text="Download", command=download, width=8, height=2, fg="red").pack(pady=20)

window.mainloop()
