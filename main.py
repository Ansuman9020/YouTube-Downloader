from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


file_size=0
def startdwn():
    global file_size
    try:
        url=urlField.get()
        dBtn.config(text='Please wait...')
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        ob = YouTube(url)
        # strm=ob.streams.all()
        # for s in strm:
        #   print(s)
        strm = ob.streams.first()
        strm.download(path_to_save_video)
        print("done....")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded Successfully")
        urlField.delete(0,END)

    except Exception as e:
        print(e)
        print("error while downloading")

main=Tk()

main.title("YouTube Downloader")
main.iconbitmap('download.ico')

main.geometry("500x600")
file=PhotoImage(file="images.png")
headingIcon=Label(main,image=file)
headingIcon.pack(side=TOP)
urlField=Entry(main,font=("verdana",18),justify=CENTER)
urlField.pack(side=TOP,fill=X, padx=10)
dBtn=Button(main, text="Start Download",font=("verdana",15),command=startdwn)
dBtn.pack(side=TOP,pady=10)

main.mainloop()

