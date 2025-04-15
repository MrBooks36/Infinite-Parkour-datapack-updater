from tkinter import Tk, Button, Entry, Label, messagebox, END
from os import getlogin, system, walk, remove, makedirs, chdir
from os.path import exists, join, dirname
from shutil import rmtree
from zipfile import ZipFile
from sys import exit
from fnmatch import fnmatch
from json import dump, load
from urllib.request import urlretrieve
# Setup logging

def copy(url, shutup=False):
    root.clipboard_clear()
    root.clipboard_append(url)
    if not shutup:
     messagebox.showinfo("Copied", 'URL Copied to Clipboard')

def find_world(root_dir):
    for root, dirs, _ in walk(root_dir):
        for dir_name in dirs:
            if fnmatch(dir_name, '*Infinite-Parkour*'):
                return join(root, dir_name)
    messagebox.showerror('Error', "Cannot find world. Check your path or ensure it exists.")
    print("Cannot find world")
    return None

def save_config(custom_path):
    with open(f'C:/Users/{getlogin()}/Documents/parkourconfig.json', 'w', encoding='utf-8') as f:
        dump({"data": custom_path}, f, ensure_ascii=False, indent=4)
        f.close()
        print("config saved")

def load_config():
    if exists(f'C:/Users/{getlogin()}/Documents/parkourconfig.json'):
        with open(f'C:/Users/{getlogin()}/Documents/parkourconfig.json', 'r') as file:
            print("config loaded")
            ret = load(file).get('data', '')
            file.close()
            return ret
    return ''


def run():
    print("starting updater")
    try:
        custom_path = txt.get().strip()
        saves_path = custom_path if custom_path else f"C:/Users/{getlogin()}/AppData/Roaming/.minecraft/saves"
        world_path = find_world(saves_path)
        if not world_path:
            return
        
        if custom_path:
            save_config(custom_path)
        
        datapack_path = join(world_path, 'datapacks', 'Infinite-Parkour-datapack-main')
        
        rmtree(dirname(datapack_path))
        makedirs(dirname(datapack_path))

        urlretrieve('https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack/archive/refs/heads/main.zip', f'{dirname(datapack_path)}/temp.zip')
        with ZipFile(f'{dirname(datapack_path)}/temp.zip', mode="r") as zip:
         #Extract all files to the current directory
         zip.extractall(dirname(datapack_path))
         zip.close()

        remove(f'{dirname(datapack_path)}/temp.zip')
        print(datapack_path)
        chdir(datapack_path)
        system(f'{datapack_path}\\build.bat') 

        messagebox.showinfo("Done", 'Update complete!')
        print("update done")

    except Exception as e:
        print(e)
        messagebox.showerror('Error', f"{e}\nAn error occurred. Contact MrBooks36 for help. Error copied to clipboard")
        copy(e, True)

def reset_config():
    if exists(f'C:/Users/{getlogin()}/Documents/parkourconfig.json'):
        remove(f'C:/Users/{getlogin()}/Documents/parkourconfig.json')
    txt.delete(0, END)


def update():
   system('start cmd /c updaterinstaller.exe headless') 
   exit()


# GUI Setup
root = Tk()
root.title("Packupdater")
root.geometry('190x55')
root.resizable(False, False)

Label(root, text="Custom Path").grid(column=2, row=0)

btn_run = Button(root, text="Run", command=run)
btn_run.grid(column=1, row=0)

btn_help = Button(root, text="Help", command=lambda: copy('https://discord.com/users/1327055692179177494'))
btn_help.grid(column=1, row=2)

btn_reset = Button(root, text="Reset Config", command=reset_config)
btn_reset.grid(column=2, row=2)


btn_reset = Button(root, text="Update", command=update)
btn_reset.grid(column=3, row=2)

# Entry for custom path
txt = Entry(root, width=11)
txt.grid(column=3, row=0)
txt.insert(0, load_config())

root.mainloop()