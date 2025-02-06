# Import Module
from tkinter import Tk, Button, Entry, Label, messagebox
from os import getlogin, path, chmod, chdir,  remove, listdir, system
from shutil import rmtree
from git import Repo
# create root window
root = Tk()
repo_url = 'https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack'
username = getlogin()



root.title("Packupdater")
# Set geometry(widthxheight)
root.geometry('180x50')

def help():
 root.clipboard_clear()
 root.clipboard_append('https://discord.com/users/1327055692179177494')
 messagebox.showinfo("Copied",'URL copied to Clipboard')

def reset():
 try:
  remove("config.json")
  messagebox.showinfo("Config Reset",'Config Reset')
 except:
  print("config didn't exist")
  messagebox.showinfo("Config Reset",'Config Reset')
# function to display text when
# button is clicked

def run():
  try:
   if len(txt.get()) != 0:
    p = (f'{txt.get()}/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
    print(f'Folder path at\n{p}')
   else:
    p = (f'C:/Users/{username}/AppData/Roaming/.minecraft/saves/infinite-parkour-alpha-v0.1.2/datapacks/Infinite-Parkour-datapack')
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
   messagebox.showerror('Error', f"{e}\n An error occurred, DM MrBooks36 for help. Error copied to clipbord")
  except Exception as e:
   print(e)
# inside


btn = Button(root, text = "Run" ,
             fg = "black", command=run)
btn.grid(column=1, row=0)
btn = Button(root, text = "Help" ,
             fg = "black", command=help)
btn.grid(column=1, row=2)

lbl = Label(root, text = "Custom Path")
lbl.grid(column=2, row=0)

txt = Entry(root, width=10)
txt.grid(column=3, row =0)
# Execute Tkinter
root.resizable(width=False, height=False)
root.mainloop()