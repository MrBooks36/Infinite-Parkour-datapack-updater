from os import chdir, listdir, chmod, system, getlogin,path
from shutil import rmtree
chdir(path.dirname(path.abspath(__file__)))
def unlock_git_files(datapack_path):
    git_pack_path = path.join(datapack_path, '.git', 'objects')
    try:
        if path.exists(git_pack_path):
            chdir(git_pack_path)
            for file in listdir(git_pack_path):
                chmod(file, 0o777)
            print("Unlocked Git files.")
            chdir('C:/')
        else:
            print("No Git files to unlock.")
            chdir('C:/')
    except Exception as e:
        print(e)
unlock_git_files(path.dirname(path.abspath(__file__)))
path = (path.dirname(path.abspath(__file__)))
rmtree(path)
system(f'del C:/Users/{getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Infinite-Parkour-datapack-updater.lnk')
