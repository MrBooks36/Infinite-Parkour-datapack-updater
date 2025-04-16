from tkinter import Tk, Label, messagebox, END, Text, Scrollbar, Toplevel
from tkinter import ttk
from tkinter.filedialog import askopenfilename, askdirectory
from os import getlogin, system, walk, remove, makedirs, chdir
from os.path import exists, join, dirname, basename
from shutil import rmtree
from zipfile import ZipFile
from sys import exit
from fnmatch import fnmatch
from json import dump, load
from urllib.request import urlretrieve
from tarfile import open as opentar


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
    log_message("Cannot find world")
    
    return None


def save_config(custom_path):
    f = open(f'C:/Users/{getlogin()}/Documents/parkourconfig.json', 'w', encoding='utf-8')
    dump({"data": custom_path}, f, ensure_ascii=False, indent=4)
    f.close()
    print("config saved")
    log_message("Config saved")


def load_config():
    if exists(f'C:/Users/{getlogin()}/Documents/parkourconfig.json'):
        file = open(f'C:/Users/{getlogin()}/Documents/parkourconfig.json', 'r')
        print("config loaded")
        log_message("Config loaded")
        ret = load(file).get('data', '')
        file.close()
        return ret
    return ''


def get_custom_path():
    custom_path = txt.get().strip()
    saves_path = custom_path + "/saves" if custom_path else f"C:/Users/{getlogin()}/AppData/Roaming/.minecraft/saves"
    world_path = find_world(saves_path)
    return world_path


def select_file(folder=''):
    file_path = askopenfilename(initialdir=folder)
    if file_path:
        return file_path
    else:
        return None


def select_directory():
    folder_path = askdirectory(title="Select Minecraft Folder")
    if folder_path:
        txt.delete(0, END)
        txt.insert(0, folder_path)  # Update the entry field with selected directory
        save_config(folder_path)  # Save the folder path to the config


def log_message(message):
    if log_window:
        log_text.config(state="normal")
        log_text.insert(END, message + "\n")
        log_text.see(END)  # Scroll to the end
        log_text.config(state="disabled")


def updatepack():
    log_message("Starting updater...")
    try:
        custom_path = txt.get().strip()
        saves_path = custom_path + "/saves" if custom_path else f"C:/Users/{getlogin()}/AppData/Roaming/.minecraft/saves"
        world_path = find_world(saves_path)
        if not world_path:
            return

        if custom_path:
            save_config(custom_path)

        datapack_path = join(world_path, 'datapacks', 'Infinite-Parkour-datapack-main')

        rmtree(dirname(datapack_path))
        makedirs(dirname(datapack_path))

        urlretrieve(
            'https://github.com/Big-Con-Gaming/Infinite-Parkour-datapack/archive/refs/heads/main.zip',
            f'{dirname(datapack_path)}/temp.zip'
        )

        log_message(f"Downloaded zip file to {dirname(datapack_path)}/temp.zip")

        zip = ZipFile(f'{dirname(datapack_path)}/temp.zip', mode="r")
        zip.extractall(dirname(datapack_path))
        zip.close()

        remove(f'{dirname(datapack_path)}/temp.zip')
        log_message(f"Extracted datapack to {datapack_path}")

        chdir(datapack_path)
        system(f'{datapack_path}\\build.bat')

        messagebox.showinfo("Done", 'Update complete!')
        log_message("Update complete!")

    except Exception as e:
        print(e)
        messagebox.showerror('Error', f"{e}\nAn error occurred. Contact MrBooks36 for help. Error copied to clipboard")
        copy(e, True)
        log_message(f"Error: {e}")


def reset_config():
    if exists(f'C:/Users/{getlogin()}/Documents/parkourconfig.json'):
        remove(f'C:/Users/{getlogin()}/Documents/parkourconfig.json')
    txt.delete(0, END)
    log_message("Config reset.")


def update():
    system('start cmd /c updaterinstaller.exe headless')
    exit()


def importpack():
    pack = select_file()
    if pack is None:
        return
    if '.jumpack' not in pack:
        return
    chdir(get_custom_path() + '/data')
    file = opentar(pack)
    file.extractall(filter='fully_trusted')
    file.close()
    messagebox.showinfo('Done', 'Your jumpack has been imported. Add it with the book in your hotbar in the world')
    log_message(f"Imported pack: {pack}")
    


def exportpack():
    pack = select_file(folder=get_custom_path()+'/data')
    print(pack)
    log_message(pack)
    if pack == None: return
    print(dirname(pack))
    log_message(dirname(pack))
    chdir(dirname(pack))
    if pack is None:
        return
    if 'command_storage' not in pack:
        print(False)
        return
    tar = opentar(f'C:/Users/{getlogin()}/Downloads/My.jumpack', 'w:gz')
    tar.add(basename(pack))
    tar.close()
    messagebox.showinfo('Done', 'Done! You can find your jumpack in your downloads folder.')
    log_message(f"Exported pack to: C:/Users/{getlogin()}/Downloads/My.jumpack")


def toggle_log_window():
    global log_window
    if log_window.winfo_ismapped():
        log_window.withdraw()  # Hide the log window
    else:
        log_window.deiconify()  # Show the log window


# GUI Setup
root = Tk()
root.title("Packupdater")
root.geometry('270x205')  # Set window size to 255x150
root.resizable(False, False)  # Make the window non-resizable

# Create widgets with ttk for a modern look
Label(root, text="Custom Path").grid(column=0, row=0, padx=5, pady=5)
btn_select_folder = ttk.Button(root, text="Select Custom Minecraft Folder", command=select_directory)
btn_select_folder.grid(column=1, row=0, padx=5, pady=5, sticky="ew")

btn_run = ttk.Button(root, text="Run", command=updatepack)
btn_run.grid(column=0, row=1, padx=5, pady=5, sticky="ew")

btn_help = ttk.Button(root, text="Help", command=lambda: copy('https://discord.com/users/1327055692179177494'))
btn_help.grid(column=1, row=1, padx=5, pady=5, sticky="ew")

btn_reset = ttk.Button(root, text="Reset Config", command=reset_config)
btn_reset.grid(column=0, row=2, padx=5, pady=5, sticky="ew")

btn_import = ttk.Button(root, text="Import", command=importpack)
btn_import.grid(column=1, row=3, padx=5, pady=5, sticky="ew")

btn_export = ttk.Button(root, text="Export", command=exportpack)
btn_export.grid(column=0, row=3, padx=5, pady=5, sticky="ew")

btn_update = ttk.Button(root, text="Update", command=update)
btn_update.grid(column=1, row=2, padx=5, pady=5, sticky="ew")

# Entry for custom path
txt = ttk.Entry(root, width=40)
txt.grid(column=0, row=4, columnspan=2, padx=5, pady=5)
txt.insert(0, load_config())

# Create log window (Toplevel window for logs)
log_window = Toplevel(root)
log_window.title("Terminal Log")
log_window.geometry('500x200')  # Resize the log window
log_window.withdraw()  # Start hidden
log_label = ttk.Label(log_window, text="Terminal Log:")
log_label.grid(row=0, column=0, sticky="w", padx=8, pady=5)

log_text = Text(log_window, wrap="word", width=60, height=10, state="disabled")
log_text.grid(row=1, column=0, columnspan=4, padx=8, pady=5)

scrollbar = Scrollbar(log_window, command=log_text.yview)
scrollbar.grid(row=1, column=4, sticky="ns", pady=5)
log_text.config(yscrollcommand=scrollbar.set)

# Button to toggle log window visibility
btn_toggle_log = ttk.Button(root, text="Toggle Log Viewer", command=toggle_log_window)
btn_toggle_log.grid(column=0, row=5, columnspan=2, padx=5, pady=5, sticky="ew")

root.mainloop()