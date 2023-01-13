<h1 align="center">YouTube Clips Downloader</h1>

## Table of contents

- [User Interface](#user-interface)
- [Implementation](#implementation)
  - [tkinter](#tkinter)
  - [pytube](#pytube)
- [How to use](#how-to-use)

## User Interface

![User interface demo image](app-GUI.png)

## Implementation

Use tkinter to create the GUI and use pytube to download video clips.

### tkinter

The 「package：tkinter(Tk interface)」 is the standard Python interface to the Tcl/Tk GUI toolkit.

The tkinter package implements the following interfaces：

- Input interface for Youtube video URL
- Download folder selection interface
- The interface for obtaining and displaying the list of video resolutions
- Video quality selection interface
- Video download interface

### pytube

The 「package：pytube」 is a lightweight, Pythonic, dependency-free, library(and command-line utility) for downloading YouTube Videos.

## How to use

APP usage steps are as follows：

1. Enter the YouTube video URL
2. Select the video storage folder
3. Get the list of video resolutions
4. Select the desired video quality
5. Download the video
