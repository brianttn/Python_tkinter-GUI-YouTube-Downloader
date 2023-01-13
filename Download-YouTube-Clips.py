import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

# = = = = = = = = = = = =   主視窗   = = = = = = = = = = = =
root = tk.Tk()                  # Main window
root.geometry('720x400')        # Set size to 720x400
root.title('YouTube Clips Downloader')      # Set title

# = = = = = = = = = =   Global Variables   = = = = = = = = = =
# - - -   要取得「StringVar()：值」，必需使用「method：get()」   - - -
youTubeURL = tk.StringVar()         # Entry1的「字串」變數：youTubeURL
clipResolution = tk.StringVar()     # Button1的「字串」變數：clipResolution
download_Path = tk.StringVar()      # Button2的「字串」變數：download_Path

# = = = = = = = = = = = = = =   Frames   = = = = = = = = = = = = = =
# - - -   Frame1：Input video URL & Select storage folder   - - -
f1Height = 150
urlInputFrame = tk.Frame(root, bg='purple', width=720, height=f1Height)
urlInputFrame.pack()    # 排版

# - - -   Frame2：Available resolutions list & Download button   - - -
resListFrame = tk.Frame(root, width=720, height=400-f1Height)
resListFrame.pack()     # 排版


# = = = = = = = = = = = =   Frame1：urlInputFrame   = = = = = = = = = = = =
# = = = = = = = = = = = =   Label1   = = = = = = = = = = = =
label1 = tk.Label(
    urlInputFrame,
    bg='purple',
    fg='white',
    text='請輸入YouTube Clips網址：',
    font=('微軟正黑體', 14)
)

label1.place(relx=0.5, rely=0.2, anchor='center')   # 排版

# = = = = = = = = = = = =   Entry1   = = = = = = = = = = = =
entry1 = tk.Entry(
    urlInputFrame,
    textvariable=youTubeURL,
    font="14",
    width=45        # 寬度：45個char
)

entry1.place(relx=0.5, rely=0.45, anchor='center')      # 排版

# = = = = = = = = = = = =   Label2   = = = = = = = = = = = =
label2 = tk.Label(
    urlInputFrame,
    bg='purple',
    fg='white',
    text='儲存目的地：',
    font=('微軟正黑體', 14)
)

label2.place(relx=0.28, rely=0.75, anchor='center')     # 排版

# = = = = = = = = = = = =   Entry2   = = = = = = = = = = = =
entry2 = tk.Entry(
    urlInputFrame,
    textvariable=download_Path,
    font="14",
    width=30
)

entry2.place(relx=0.53, rely=0.75, anchor='center')     # 排版

# = = = = = = = = = = = =   Button2   = = = = = = = = = = = =
# - - - - - -   Button2的callback   - - - - - -
def btn2ClickFunc():
    download_Directory = filedialog.askdirectory(
        title="儲存影片",
        initialdir=r'D:'        # 初始資料夾位置
    )

    download_Path.set(download_Directory)       # Set the file storage path

# - - - - - -   建立：Button2元件   - - - - - -
btn2 = tk.Button(
    urlInputFrame,
    text='瀏 覽',
    font=('微軟正黑體', 12),
    command=btn2ClickFunc,
    fg='Black'
)

btn2.place(relx=0.76, rely=0.75, anchor='center')     # 排版


# = = = = = = = = = = = =   Frame2：urlInputFrame   = = = = = = = = = = = =
# = = = = = = = = = = = =   Button1   = = = = = = = = = = = =
# - - - - - -   Button1的callback   - - - - - -
def btn1ClickFunc():
    # Retrieve 「StringVar()：youTubeURL」 value
    urlStr = youTubeURL.get()

    # - - -   測試：pytube是否支援此網址、網址是否正確   - - -
    try:
        youTubeObj = YouTube(urlStr)
    except:
        messagebox.showerror('URL錯誤', '不支援此影片格式或網址錯誤!!')
        return

# - - - - - -   建立：Button1元件   - - - - - -
btn1 = tk.Button(
    resListFrame,
    text='取得影片解析度清單',
    font=('微軟正黑體', 12),
    command=btn1ClickFunc,
    bg='#FFD700',
    fg='Black'
)

btn1.grid(row=0, pady=10)     # 排版


# = = = = = =   啟動主視窗   = = = = = =
root.mainloop()