from os import system, chdir, getlogin, path, listdir, chmod
from shutil import which, rmtree
if  not which('git'): 
        system('winget install --id Git.Git -e --source winget')
        print('done')
        exit()
print(getlogin())
def unlock_git_files(git):
    git_pack_path = path.join(git, '.git', 'objects', 'pack')
    if path.exists(git_pack_path):
        chdir(git_pack_path)
        for file in listdir(git_pack_path):
            chmod(file, 0o777)
        print("Unlocked Git files.")
        chdir('C:/')
    else:
        print("No Git files to unlock.")
        chdir('C:/')
unlock_git_files(f'C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater')
chdir(f'C:/Users/{getlogin()}/Documents')
try:
 rmtree(f'C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater')
except Exception as e:
     print(e)
system('git clone https://github.com/MrBooks36/Infinite-Parkour-datapack-updater')
print('done, press enter')
input()