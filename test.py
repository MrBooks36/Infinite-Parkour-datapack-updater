import os
import fnmatch
username = os.getlogin()
def find_directories_with_name(root_dir, name):
    matching_dirs = []
    for root, dirs, files in os.walk(root_dir):
        for dir_name in dirs:
            if fnmatch.fnmatch(dir_name, f'*{name}*'):
                matching_dirs.append(os.path.join(root, dir_name))
    return matching_dirs[0]

# Example usage
root_directory = f'C:/Users/{username}/AppData/Roaming/.minecraft/saves'
name_to_find = 'Infinite-Parkour'
directories = find_directories_with_name(root_directory, name_to_find)

print(directories)