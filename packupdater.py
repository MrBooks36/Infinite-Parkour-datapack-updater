from tkinter import Tk, Button, Entry, Label, messagebox, END
from os import getlogin, path, chdir, system, walk, remove
from shutil import rmtree, which
from fnmatch import fnmatch
from json import dump, load
print(path.dirname(path.abspath(__file__)))
chdir(path.dirname(path.abspath(__file__)))
# Setup logging

def check_git():
    if which('git'): return
    else:
        print("Install Git before running this program!")
        def install():
            chdir(f'C:/ProgramData/Microsoft/Windows/Start Menu/Programs')
            system('winget install --id Git.Git -e --source winget')
            messagebox.showinfo("Done", 'Install complete!')
            exit()
        root = Tk()
        root.title("Packupdater")
        root.geometry('250x100')
        root.resizable(False, False)
        Label(root, text="Install Git to use").grid(column=0, row=0)
        btn_run = Button(root, text="Auto install", command=install)
        btn_run.grid(column=0, row=1)
        root.mainloop()

def copy(url):
    root.clipboard_clear()
    root.clipboard_append(url)
    messagebox.showinfo("Copied", 'Copied to Clipboard')

def find_world(root_dir):
    for root, dirs, _ in walk(root_dir):
        for dir_name in dirs:
            if fnmatch(dir_name, '*Infinite-Parkour*'):
                return path.join(root, dir_name)
    messagebox.showerror('Error', "Cannot find world. Check your path or ensure it exists.")
    print("Cannot find world")
    return None

def save_config(custom_path):
    with open(f'C:/Users/{getlogin()}/Documents/parkourconfig.json', 'w', encoding='utf-8') as f:
        dump({"data": custom_path}, f, ensure_ascii=False, indent=4)
        print("config saved")

def load_config():
    chdir(path.dirname(path.abspath(__file__)))
    if path.exists(f'C:/Users/{getlogin()}/Documents/parkourconfig.json'):
        with open(f'C:/Users/{getlogin()}/Documents/parkourconfig.json', 'r') as file:
            print("config loaded")
            return load(file).get('data', '')
    return ''

def remove_old_datapack(datapack_path):
    if path.exists(datapack_path):
        rmtree(datapack_path)
        print("PMC datapack deleted.")


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
        
        datapack_path = path.join(world_path, 'datapacks', 'Infinite-Parkour-datapack')
        old_datapack_path = path.join(world_path, 'datapacks', 'Infinite-Parkour')
        if not path.exists(datapack_path):
         remove_old_datapack(old_datapack_path)
         chdir(path.dirname(datapack_path))
         system('git clone https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack --depth=1')
        else:
         chdir(datapack_path)
         system('git pull https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack --depth=1')
        chdir(datapack_path)
        print(system(f'{datapack_path}/build.bat')) 
        messagebox.showinfo("Done", 'Update complete!')
        print("update done")
    except Exception as e:
        messagebox.showerror('Error', f"{e}/nAn error occurred. Contact MrBooks36 for help. Error copied to clipboard")
        copy(e)
        print(e)

def reset_config():
    if path.exists(f'C:/Users/{getlogin()}/Documents/parkourconfig.json'):
        remove(f'C:/Users/{getlogin()}/Documents/parkourconfig.json')
    txt.delete(0, END)

def debug():
    try:
        print('starting debug')
        custom_path = txt.get().strip()
        saves_path = custom_path if custom_path else f"C:/Users/{getlogin()}/AppData/Roaming/.minecraft/saves"
        world_path = find_world(saves_path)
        if world_path != None:
            datapack_path = path.join(world_path, 'datapacks', 'Infinite-Parkour-datapack')
            old_datapack_path = path.join(world_path, 'datapacks', 'Infinite-Parkour')
            print('PMC pack ' + ('true' if old_datapack_path and path.exists(old_datapack_path) else 'false'))
            print('new pack ' + ('true' if datapack_path and path.exists(datapack_path) else 'false'))
        print('custom path ' + ('true' if custom_path and path.exists(custom_path) else 'false'))
        print('saves path ' + ('true' if saves_path and path.exists(saves_path) else 'false'))
        print('world path ' + ('true' if world_path and path.exists(world_path) else 'false'))
        print('done')
        messagebox.showinfo("Done", 'Debug complete!')
    except Exception as e:
        print(e)
        print('done')
        messagebox.showerror('Error', f"{e}/nAn error occurred")

def update():
   chdir(f'C:/Users/{getlogin()}/Documents/Infinite-Parkour-datapack-updater')
   system('start cmd /c updaterinstaller.exe') 
   exit()


# GUI Setup
check_git()
root = Tk()
root.title("Packupdater")
root.geometry('190x80')
root.resizable(False, False)

Label(root, text="Custom Path").grid(column=2, row=0)

btn_run = Button(root, text="Run", command=run)
btn_run.grid(column=1, row=0)

btn_help = Button(root, text="Help", command=lambda: copy('https://discord.com/users/1327055692179177494'))
btn_help.grid(column=1, row=2)

btn_reset = Button(root, text="Reset Config", command=reset_config)
btn_reset.grid(column=2, row=2)

btn_reset = Button(root, text="DEBUG", command=debug)
btn_reset.grid(column=3, row=2)

btn_reset = Button(root, text="Update", command=update)
btn_reset.grid(column=3, row=3)

# Entry for custom path
txt = Entry(root, width=11)
txt.grid(column=3, row=0)
txt.insert(0, load_config())

root.mainloop()