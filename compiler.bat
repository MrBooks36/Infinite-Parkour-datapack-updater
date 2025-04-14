@echo off
cd C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater
python -m nuitka --follow-imports --enable-plugin=tk-inter --standalone --onefile --remove-output --windows-console-mode=attach --mingw64 --windows-icon-from-ico=pack.ico packupdater.py


python -m nuitka --follow-imports --enable-plugin=tk-inter --standalone --onefile --remove-output --windows-console-mode=disable --mingw64 --windows-icon-from-ico=pack.ico updaterinstaller.py