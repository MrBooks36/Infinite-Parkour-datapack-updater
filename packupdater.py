try:
 from os import getlogin, path, chmod, chdir, system
 from git import Repo
 from shutil import rmtree
 username = getlogin()
 print(f'Hi {username}')

 def startup():
  from win32com.client import Dispatch
  target = path.abspath(__file__)
  shell = Dispatch("WScript.Shell")
  shortcut = shell.CreateShortCut(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/packupdater.lnk')
  shortcut.Targetpath = target
  shortcut.IconLocation = target
  shortcut.save()

 
 if not path.exists(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/packupdater.lnk'):
  response = input("Do you want to open updater on PC startup? Y/n ").strip().lower()
  while True:
   if response == 'y':
    print("Adding to startup ")
    startup()
    break
   elif response == 'n':
    print("ok")
    break

 #def paths
 if path.exists('config.txt'):
   with open('config.txt', 'r') as file:
    path = file.read()
    p = (f'{path}/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
    print(f'Folder path at\n{p}')
 else:
   p = (f'C:/Users/{username}/AppData/Roaming/.minecraft/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
   print(f'Folder path at\n{p}')

 repo_url = 'https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack'

 #give access to pain in the butt to remove files 
 try:
  chmod(f'{p}/.git/objects/pack/pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.idx', 0o777)
  print('removed pain in the butt file 1 ')
 except:
   print("pain in the butt file 1 didn't exist")
 try:
  chmod(f'{p}/.git/objects/pack/pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.pack', 0o777)
  print('removed pain in the butt file 2 ')
 except:
   print("pain in the butt file 2 didn't exist")
 try:
  chmod(f'{p}/.git/objects/pack/pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.rev', 0o777)
  print('removed pain in the butt file 3 ')
 except:
   print("pain in the butt file 3 didn't exist")

 if path.exists(p):
     rmtree(p)
     print(f"Old pack has been deleted.")
     print('installing new pack')
 else:
   print("Old datapack didn't exist. This might be a error in your config.txt or it never existed  ")
 print('installing pack')
 repo = Repo.clone_from(repo_url, f"{p}")
 print('pack installed')
 chdir(p)
 system(f'{p}/autobuild.bat')
except NotADirectoryError or FileNotFoundError :
  print("Your config.txt isn't set up correctly")
except Exception as e: 
  print(f'{e}\nMessage MrBooks36 for a fix at https://discord.com/users/1327055692179177494')
  input('press enter to end')