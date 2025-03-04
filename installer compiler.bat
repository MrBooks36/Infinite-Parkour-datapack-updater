@echo off
cd C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater
python -m PyInstaller --noconfirm --onefile --console --icon "C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater\pack.png"  "C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater\updaterinstaller.py"
move C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater\dist\updaterinstaller.exe  C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater
del C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater\updaterinstaller.spec
rmdir /s /q C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater\dist
rmdir /s /q C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater\build\packupdater\localpycs
rmdir /s /q C:\Users\ofk20\Documents\GitHub\Infinite-Parkour-datapack-updater\build