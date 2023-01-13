import tkinter as tk

# = = = = = = = = = = = =   主視窗   = = = = = = = = = = = =
root = tk.Tk()                  # Main window
root.geometry('720x400')        # Set size to 720x400
root.title('YouTube Clips Downloader')      # Set title

# = = = = = = = = = = = = = =   Frames   = = = = = = = = = = = = = =
# - - -   Frame1：Input video URL & Select storage folder   - - -
f1Height = 150
urlInputFrame = tk.Frame(root, bg='purple', width=720, height=f1Height)
urlInputFrame.pack()    # 排版

# - - -   Frame2：Available resolutions list & Download button   - - -
resListFrame = tk.Frame(root, width=720, height=400-f1Height)
resListFrame.pack()     # 排版


# = = = = = = = = = = = =   Frame1：urlInputFrame   = = = = = = = = = = = =


# = = = = = = = = = = = =   Frame2：urlInputFrame   = = = = = = = = = = = =


# = = = = = =   啟動主視窗   = = = = = =
root.mainloop()