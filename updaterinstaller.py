from os import system, chdir, getlogin, path, listdir, chmod
from shutil import which, rmtree
if  not which('git'): 
        system('winget install --id Git.Git -e --source winget')
        print('done')
        exit()
print(getlogin())
if path.exists(f'C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater'):
 print('update old install')
 chdir(f'C:/Users/{getlogin()}/Documents')
 system('git pull https://github.com/MrBooks36/Infinite-Parkour-datapack-updater main')
else:
 print('new install')
 chdir(f'C:/Users/{getlogin()}/Documents')
 system('git clone https://github.com/MrBooks36/Infinite-Parkour-datapack-updater')
print('done, press enter to exit')
input()