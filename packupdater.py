# Import Module
from tkinter import Tk, Button, Entry, Label, messagebox
from os import getlogin, path, chmod, chdir, system, remove
from shutil import rmtree
from git import Repo
from subprocess import check_call


username = getlogin()
# create root window
root = Tk()
repo_url = 'https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack'
# root window title and dimension
root.title("Packupdater")
# Set geometry(widthxheight)
root.geometry('250x50')

def reset():
 try:
  remove("config.txt")
 except:
  print("config didn't exist")
# function to display text when
# button is clicked
def startup():
  from win32com.client import Dispatch
  target = path.abspath(__file__)
  shell = Dispatch("WScript.Shell")
  shortcut = shell.CreateShortCut(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/packupdater.lnk')
  shortcut.Targetpath = target
  shortcut.IconLocation = target
  shortcut.save()
  print('added to startup')

def run():
  try:
   if len(txt.get()) != 0:
    p = (f'{txt.get()}/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
    print(f'Folder path at\n{p}')
    with open('config.txt', 'w') as file:
     file.write(p)
   else:
    p = (f'C:/Users/{username}/AppData/Roaming/.minecraft/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
    print(f'Folder path at\n{p}')
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
   else:
    print("Old datapack didn't exist. This might be a error in your path or it never existed")
    messagebox.showwarning('Warning', "Old datapack didn't exist. This might be a error in your path or it never existed")
   print('downloading')
   repo = Repo.clone_from(repo_url, p)
   print('compiling')
   chdir(p)
   system(f'{p}/autobuild.bat')
   messagebox.showinfo("Done",'Done')
  except Exception as e:
   messagebox.showerror('Error', f"{e}\n An error occurred, DM MrBooks36 for help. URL copied to clipbord")
   root.clipboard_clear()
   root.clipboard_append('https://discord.com/users/1327055692179177494')
# inside
if not path.exists(f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/packupdater.lnk'):
 btn = Button(root, text = "Open on startup" ,
             fg = "black", command=startup)
 btn.grid(column=1, row=2)

btn = Button(root, text = "Reset config" ,
             fg = "black", command=reset)
btn.grid(column=2, row=2)

btn = Button(root, text = "Run" ,
             fg = "black", command=run)
btn.grid(column=1, row=0)

lbl = Label(root, text = "Custom Path")
lbl.grid(column=2, row=0)

txt = Entry(root, width=10)
txt.grid(column=3, row =0)
if path.exists("config.txt"):
    with open('config.txt', 'r') as file:
     config = file.read()
     txt.insert(1,config)
# Execute Tkinter
root.resizable(width=False, height=False)
root.mainloop()