from os import getlogin, path, chmod, chdir, system
from git import Repo
from shutil import rmtree
from win32com.client import Dispatch
try:
 username = getlogin()
 #desktop = r"path to where you wanna put your .lnk file"
 target = path.abspath(__file__)
 shell = Dispatch("WScript.Shell")
 shortcut = shell.CreateShortCut(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/packupdater.lnk')
 shortcut.Targetpath = target
 shortcut.IconLocation = target
 shortcut.save()
 #def paths
 if path.exists('config.txt'):
   with open('config.txt', 'r') as file:
    path = file.read()
    print(f'{path}/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
    p = (f'{path}/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
 else:
   p = (f'C:/Users/{username}/AppData/Roaming/.minecraft/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
   print(p)

 repo_url = 'https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack'

 #give access to pain in the butt to remove files 
 try:
  chmod(f'{p}\.git\objects\pack\pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.idx', 0o777)
 except:
   print('1')
 try:
  chmod(f'{p}\.git\objects\pack\pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.pack', 0o777)
 except:
   print('2')
 try:
  chmod(f'{p}\.git\objects\pack\pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.rev', 0o777)
 except:
    print('3')

 if path.exists(p):
     rmtree(p)
     print(f"Old pack has been deleted.")
 print('installing new pack')
 repo = Repo.clone_from(repo_url, f"{p}")
 chdir(p)
 system(f'{p}/autobuild.bat')
except Exception as e: 
  print(f'{e}\nMessage MrBooks36 for a fix at https://discord.com/users/1327055692179177494 ')
input('press enter to end')