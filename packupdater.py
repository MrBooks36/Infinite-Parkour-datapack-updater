from tkinter import Tk, Button, Entry, Label, messagebox, END
from os import getlogin, path, chmod, chdir, listdir, system, walk, remove
from shutil import rmtree, which
from fnmatch import fnmatch
from json import dump, load
import logging
if path.exists('log.log'):
 remove('log.log')
logging.basicConfig(filename='log.log', level=logging.DEBUG)

def check_git():
    if  which('git'):
      return
    else:
        logging.debug("Install Git before running this program!")
        def install():
            chdir(f'C:/Users/{getlogin()}/Downloads')
            system('winget install --id Git.Git -e --source winget')
            messagebox.showinfo("Done", 'Install complete!')
            exit()
        root = Tk()
        root.title("Packupdater")
        root.geometry('95x50')
        root.resizable(False, False)
        Label(root, text="Install Git to use").grid(column=0, row=0)
        btn_run = Button(root, text="Auto install ", command=install)
        btn_run.grid(column=0, row=1)
        root.mainloop()



def copy(url):
    root.clipboard_clear()
    root.clipboard_append(url)
    messagebox.showinfo("Copied", 'URL copied to Clipboard')

def find_world(root_dir):
    for root, dirs, _ in walk(root_dir):
        for dir_name in dirs:
            if fnmatch(dir_name, '*Infinite-Parkour*'):
                return path.join(root, dir_name)
    messagebox.showerror('Error', "Cannot find world. Check your path or ensure it exists.")
    logging.debug("Cannot find world")
    return None

def save_config(custom_path):
    with open('config.json', 'w', encoding='utf-8') as f:
        dump({"data": custom_path}, f, ensure_ascii=False, indent=4)
        logging.debug("config saved")

def load_config():
    chdir(path.dirname(path.abspath(__file__)))
    if path.exists('config.json'):
        with open('config.json', 'r') as file:
            return load(file).get('data', '')
        logging.debug("config loaded")
    return ''

def remove_old_datapack(datapack_path, old):
    if path.exists(datapack_path):
        rmtree(datapack_path)
        logging.debug("Old datapack deleted.")
    elif old != True:
        logging.debug("Old datapack not found.")
        messagebox.showwarning('Warning', "Old datapack not found.")

def unlock_git_files(datapack_path):
    git_pack_path = path.join(datapack_path, '.git')
    try:
     if path.exists(git_pack_path):
        chdir(git_pack_path)
        for file in listdir(git_pack_path):
            chmod(file, 0o777)
        logging.debug("Unlocked Git files.")
        chdir('C:/')
     else:
        logging.debug("No Git files to unlock.")
        chdir('C:/')
    except Exception as e:
       logging.debug(e)

def run():
    logging.debug("starting updater")
    try:
        custom_path = txt.get().strip()
        saves_path = custom_path if custom_path else f"C:/Users/{getlogin()}/AppData/Roaming/.minecraft/saves"
        world_path = find_world(saves_path)
        if not world_path:
            return
        
        save_config(custom_path) if custom_path else None
        
        datapack_path = path.join(world_path, 'datapacks', 'Infinite-Parkour-datapack')
        old_datapack_path = path.join(world_path, 'datapacks', 'Infinite-Parkour')
        
        remove_old_datapack(old_datapack_path, True)
        unlock_git_files(datapack_path)
        remove_old_datapack(datapack_path, False)
        
        chdir(path.dirname(datapack_path))
        system(f'git clone https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack')
        
        chdir(datapack_path)
        system(f'{datapack_path}/build.bat')
        messagebox.showinfo("Done", 'Update complete!')
        logging.debug("update done")
    except Exception as e:
        messagebox.showerror('Error', f"{e}\nAn error occurred. Contact MrBooks36 for help. Error copied to clipboard")
        copy(e)
        logging.debug(e)

def reset_config():
    chdir(path.dirname(path.abspath(__file__)))
    if path.exists('config.json'):
        remove('config.json')
    txt.delete(0, END)
def debug():
    try:
     logging.debug('starting debug')
     custom_path = txt.get().strip()
     saves_path = custom_path if custom_path else f"C:/Users/{getlogin()}/AppData/Roaming/.minecraft/saves"
     world_path = find_world(saves_path)
     if world_path != None:
         datapack_path = path.join(world_path, 'datapacks', 'Infinite-Parkour-datapack')
         old_datapack_path = path.join(world_path, 'datapacks', 'Infinite-Parkour')
         if old_datapack_path and path.exists(old_datapack_path):
          logging.debug('PMC pack true')
         else:
          logging.debug('PMC pack false')
         if datapack_path and path.exists(datapack_path):
          logging.debug('new pack true')
         else:
            logging.debug('new pack false')
     if custom_path and path.exists(custom_path):
        logging.debug('custom path true')
     else:
          logging.debug('custom path false')
     if saves_path and path.exists(saves_path):
        logging.debug('saves path true')
     else:
        logging.debug('saves path false')
     if world_path and path.exists(world_path):
        logging.debug('world path true')
     else:
        logging.debug('world path false')
     logging.debug('done')
     messagebox.showinfo("Done", 'Debug complete!')
    except Exception as e:
        logging.debug(e)
        logging.debug('done')
        messagebox.showerror('Error', f"{e}\nAn error occurred")
def update():
   system('START updaterinstaller.exe')
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