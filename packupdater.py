# Import Module
from tkinter import Tk, Button, Entry, Label, messagebox, END
from os import getlogin, path, chmod, chdir, listdir, system, walk, remove
from shutil import rmtree
from git import Repo
from json import dump, load
# create root window
root = Tk()
repo_url = 'https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack'
username = getlogin()



root.title("Packupdater")
# Set geometry(widthxheight)
root.geometry('190x50')

def help():
 root.clipboard_clear()
 root.clipboard_append('https://discord.com/users/1327055692179177494')
 messagebox.showinfo("Copied",'URL copied to Clipboard')


def find_directories_with_name(root_dir ):
    matching_dirs = []
    for dirpath, dirnames, filenames in walk(root_dir):
        for dirname in dirnames:
            if 'infinite-parkour' in dirname:
                matching_dirs.append(path.join(dirpath, dirname))
                matching_dirs = matching_dirs[0]
    return matching_dirs

def run():
  try:
   if len(txt.get()) != 0:
    data = {
    "data" : txt.get()
     } 
    with open('config.json', 'w', encoding='utf-8') as f:
     dump(data, f, ensure_ascii=False, indent=4)
    p = (f"{find_directories_with_name(f'{txt.get()}/saves')}datapacks/Infinite-Parkour-datapack")
    if path.exists(f'{txt.get()}/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour') :
     rmtree(f'{txt.get()}/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour')
    print(f'Folder path at\n{p}')
   else:
    p = (f"{find_directories_with_name(f'C:/Users/{username}/AppData/Roaming/.minecraft/saves')}/datapacks/Infinite-Parkour-datapack")
    print(f'Folder path at\n{p}')
    if path.exists(f"C{find_directories_with_name(f'C:/Users/{username}/AppData/Roaming/.minecraft/saves')}/datapacks/Infinite-Parkour"):
     rmtree(f"{find_directories_with_name(f'C:/Users/{username}/AppData/Roaming/.minecraft/saves')}/datapacks/Infinite-Parkour")
    print(f'Folder path at\n{p}')
    #give access to pain in the butt to remove files 
   try:
    chdir(f'{p}/.git/objects/pack')
    files = listdir(f'{p}/.git/objects/pack')
    files = [f for f in files if path.isfile(f'{p}/.git/objects/pack'+'/'+f)]
    print(*files, sep="\n")
    chmod(files[0], 0o777)
    chmod(files[1], 0o777)
    chmod(files[2], 0o777)
   except:
    print('hmmm')
   if path.exists(p):
     chdir('C:/')
     rmtree(p)
     print(f"Old pack has been deleted.")
   else:
     print("Old datapack didn't exist. This might be a error in your path or it never existed")
     messagebox.showwarning('Warning', "Old datapack didn't exist. This might be a error in your path or it never existed")
   print('downloading')
   Repo.clone_from(repo_url, p)
   print('compiling')
   chdir(p)
   system(f'{p}/autobuild.bat')
   messagebox.showinfo("Done",'Done')
  except Exception as e:
   print(e)
   messagebox.showerror('Error', f"{e}\n An error occurred, DM MrBooks36 for help. Error copied to clipbord")

def reset():
  if path.exists('config.json'):
   remove('config.json')
  txt.delete(0, END)
# inside
def start():
 btn = Button(root, text = "Run", fg = "black", command=run)
 btn.grid(column=1, row=0)
 btn = Button(root, text = "Help", fg = "black", command=help)
 btn.grid(column=1, row=2)

 lbl = Label(root, text = "Custom Path")
 lbl.grid(column=2, row=0)

 btn = Button(root, text = "Reset Config", fg = "black", command=reset)
 btn.grid(column=2, row=2)

# Execute Tkinter
start()
txt = Entry(root, width=11)
txt.grid(column=3, row =0)
if path.exists('config.json'):
 with open('config.json', 'r') as file:
    data = load(file)
    data = data['data']
    txt.insert(0, data)
root.resizable(width=False, height=False)
root.mainloop()