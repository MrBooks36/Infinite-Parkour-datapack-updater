@echo off
cd C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater
python -m PyInstaller --noconfirm --onefile --windowed --icon "C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\pack.ico"  "C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\packupdater.py"
move C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\dist\packupdater.exe  C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater
del C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\packupdater.spec
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\dist
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build\packupdater\localpycs
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build