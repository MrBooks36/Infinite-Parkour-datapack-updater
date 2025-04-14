from os import getlogin, remove, chdir
from tkinter import Tk,  Button, messagebox, Label
from sys import argv, exit
from zipfile import ZipFile
from urllib.request import urlretrieve
root = Tk()
root.title("Installer")
root.geometry('190x40')
root.resizable(False, False)
def start():
 chdir(f'C:/Users/{getlogin()}/Documents')
 urlretrieve('https://github.com/MrBooks36/Infinite-Parkour-datapack-updater/archive/refs/heads/main.zip', f'C:/Users/{getlogin()}/Documents/temp.zip')
 with ZipFile(f'C:/Users/{getlogin()}/Documents/temp.zip', mode="r") as zip:
  #Extract all files to the current directory
  zip.extractall()
  zip.close()
 remove(f'C:/Users/{getlogin()}/Documents/temp.zip')

 if not len(argv) > 1: messagebox.showinfo('Done', 'Install complete!')
 exit()

if len(argv) > 1:
 start()
 
btn_reset = Button(root, text="START", command=start)
btn_reset.grid(column=0, row=1)
Label(root, text="Wellcome to the installer").grid(column=1, row=1)

root.mainloop()