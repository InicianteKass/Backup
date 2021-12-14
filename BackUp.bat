cls
echo off
cls

set ORIGEM= C:\Users\%username%\Desktop\
set ORIGEM2= C:\Users\%username%\Documents\
set ORIGEM3= C:\Users\%username%\Downloads\
set ORIGEM4= C:\Users\%username%\Pictures\

set DESTINO= "CaminhoPastaBackup\%username%\Desktop\"
set DESTINO2= "CaminhoPastaBackup\%username%\Documents\"
set DESTINO3= "CaminhoPastaBackup\%username%\Downloads\"
set DESTINO4= "CaminhoPastaBackup\%username%\Pictures\"

set LOG_DESKTOP= C:\Backup\LOG\LOG_DESKTOP
set LOG_DOCUMENTS= C:\Backup\LOG\LOG_DOCUMENTS
set LOG_DOWNLOADS= C:\Backup\LOG\LOG_DOWNLOADS
set LOG_PICTURES= C:\Backup\LOG\LOG_PICTURES

xcopy %ORIGEM% %DESTINO% /E /Y /C /H
xcopy %ORIGEM2% %DESTINO2% /E /Y /C /H
xcopy %ORIGEM3% %DESTINO3% /E /Y /C /H
xcopy %ORIGEM4% %DESTINO4% /E /Y /C /H

echo # GERANDO LOG DE ARQUIVOS

dir /s %DESTINO% > %LOG_DESKTOP%.txt
dir /s %DESTINO2% > %LOG_DOCUMENTS%.txt
dir /s %DESTINO3% > %LOG_DOWNLOADS%.txt
dir /s %DESTINO4% > %LOG_PICTURES%.txt

C:\Backup\dist\zipPath\zipPath.exe

C:\Backup\dist\emailPath\emailPath.exe

pause