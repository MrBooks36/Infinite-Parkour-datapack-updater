from os import path, chdir, listdir, chmod, system, getlogin
from shutil import rmtree
chdir(path.dirname(path.abspath(__file__)))
def unlock_git_files(path):
    git_pack_path = f"{path}/.git"
    try:
        if path.exists(git_pack_path):
            chdir(git_pack_path)
            for file in listdir(git_pack_path):
                chmod(file, 0o777)
            print("Unlocked Git files.")
        else:
            print("No Git files to unlock.")
    except Exception as e:
     print(e)
unlock_git_files(path.dirname(path.abspath(__file__)))
rmtree(chdir(path.dirname(path.abspath(__file__))))
system(f'del C:/Users/{getlogin()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Infinite-Parkour-datapack-updater.lnk')
