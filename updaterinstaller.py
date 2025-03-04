from os import system, chdir, getlogin, path
from shutil import which
import win32com.client

if  not which('git'): 
        system('winget install --id Git.Git -e --source winget')
        print('git install done')
print(getlogin())
if path.exists(f'C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater'):
 print('update old install')
 chdir(f'C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater')
 system('git pull https://github.com/MrBooks36/Infinite-Parkour-datapack-updater main')
else:
 print('new install')
 chdir(f'C:/Users/{getlogin()}/Documents')
 system(f'git clone https://github.com/MrBooks36/Infinite-Parkour-datapack-updater')
 path = f'C:/Users/{getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Infinite-Parkour-datapack-updater.lnk'
 target = f"C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater/packupdater.exe"
 icon = f"C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater/pack.png"
 shell = win32com.client.Dispatch("WScript.Shell")
 shortcut = shell.CreateShortCut(path)
 shortcut.Targetpath = target
 shortcut.IconLocation = icon
 shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
 shortcut.save()
print('done, press enter to exit')
input()