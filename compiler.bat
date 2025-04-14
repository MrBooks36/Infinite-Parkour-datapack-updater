@echo off
cd C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater
python -m PyInstaller --noconfirm --onefile --windowed --version-file version.rc --icon "C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\pack.ico"  "C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\packupdater.py"
move C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\dist\packupdater.exe  C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater
del C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\packupdater.spec
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\dist
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build\packupdater\localpycs
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build\packupdater
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build
"C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x86\signtool" sign /a /fd SHA256 C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\updaterinstaller.exe

cd C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater
python -m PyInstaller --noconfirm --onefile --windowed --version-file version.rc --icon "C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\pack.ico"  "C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\updaterinstaller.py"
move C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\dist\updaterinstaller.exe  C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater
del C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\updaterinstaller.spec
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\dist
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build\packupdater\localpycs
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build\packupdater
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build
rmdir /s /q C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\build
"C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x86\signtool" sign /a /fd SHA256 C:\Users\%username%\Documents\GitHub\Infinite-Parkour-datapack-updater\packupdater.exe