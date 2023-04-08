# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:12:10 2023

@author: akhil_raj_s_
"""
from colorama import init, Fore, Back
init()
print(Fore.BLACK + Back.WHITE + "[#] Youtube Downloader" + Fore.WHITE + Back.BLACK)
print("[#] hold on a second ...")
print()
from pytube import YouTube
from tabulate import tabulate
from pytube.cli import on_progress
import tkinter as tk
from tkinter import filedialog


def my_progress_func(stream, chunk, bytes_remaining):
     # calculate the progress percentage
     progress = (stream.filesize - bytes_remaining) / stream.filesize * 100
     # print the progress percentage
     print(f"Download progress: {progress:.1f}%")

link = input("enter youtube video link /: ")
root = tk.Tk()
root.withdraw()
print("[#] select download location")
path = filedialog.askdirectory(title='Select Download Path')
print("download path : " + str(path))
print("hold on ..")
try:
    yt = YouTube(link, on_progress_callback=my_progress_func)
except Exception as e:
    print("[#] ERROR : " + str(e))
 # get all available streams
streams = yt.streams
# create a list of stream data
stream_data = []
for stream in streams:
     stream_data.append([stream.itag, stream.mime_type, stream.resolution])

# print streams in a table format
print(tabulate(stream_data, headers=["itag", "mime_type", "resolution"]))
itag = input("enter the itag : ")
print("[#] starting download" + Fore.GREEN + Back.BLACK)
try:
    yt = YouTube(link, on_progress_callback=on_progress)
    stream = yt.streams.get_by_itag(itag)
    stream.download(path)
    print(Fore.BLACK + Back.GREEN + "[#] DOWNLOADED ! ! !")
except Exception as e:
    print(Fore.WHITE + Back.RED + "ERROR" + str(e))