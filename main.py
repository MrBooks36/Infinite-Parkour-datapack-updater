import os
from git import Repo
import shutil

#get username
username = os.getlogin()
#def paths
path = f'C:/Users/{username}/AppData/Roaming/.minecraft/saves/infinite-parkour-alpha-v0.1.1/datapacks/Infinite-Parkour-datapack'
repo_url = 'https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack'

#give access to pain in the but to remove files 
try:
 os.chmod(f'{path}\.git\objects\pack\pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.idx', 0o777)
except:
   print('1')
try:
 os.chmod(f'{path}\.git\objects\pack\pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.pack', 0o777)
except:
   print('2')
try:
 os.chmod(f'{path}\.git\objects\pack\pack-bf62a5020e26a1196cbf38be806c5194d4ff52b8.rev', 0o777)
except:
   print('3')

if os.path.exists(path):
    shutil.rmtree(path)
    print(f"Old pack has been deleted.")
print('installing new pack')
repo = Repo.clone_from(repo_url, f"{path}")
os.chdir(path)
os.system(f'{path}/autobuild.bat')
input('press enter to end')