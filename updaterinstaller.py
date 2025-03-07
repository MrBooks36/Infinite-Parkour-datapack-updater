from os import system, chdir, getlogin, path
from shutil import which
from tkinter import Tk,  Button, messagebox, Label
from pyuac import isUserAdmin, runAsAdmin
if not isUserAdmin():
        print("not admin!")
else:    
        print("Running as admin!")
        system(f'powershell Add-MpPreference -ExclusionPath "C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater"')
        exit()
root = Tk()
root.title("Packupdater")
root.geometry('190x40')
root.resizable(False, False)
def start():
 if not which('git'): 
        system('winget install --id Git.Git -e --source winget')
        print('git install done')
 print(getlogin())
 if path.exists(f'C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater'):
  print('update old install')
  chdir(f'C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater')
  system('git reset --hard HEAD')
  system('git pull https://github.com/MrBooks36/Infinite-Parkour-datapack-updater --depth=1')
 else:
  print('new install')
  chdir(f'C:/Users/{getlogin()}/Documents')
  system(f'git clone https://github.com/MrBooks36/Infinite-Parkour-datapack-updater --depth=1')
  runAsAdmin()
  
 messagebox.showinfo('Done', 'Install complete!')
 exit()
 
btn_reset = Button(root, text="START", command=start)
btn_reset.grid(column=0, row=1)
Label(root, text="Wellcome to the installer").grid(column=1, row=1)

root.mainloop()