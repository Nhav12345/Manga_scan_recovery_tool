@echo off

mkdir "C:\ScansManga"
mkdir "C:\ScansMangaExecutable\app"
mkdir "C:\ScansMangaExecutable\img"
mkdir "C:\ScansMangaExecutable\batches"



xcopy "%cd%\app" "C:\ScansMangaExecutable\app" /Q
xcopy "%cd%\img" "C:\ScansMangaExecutable\img" /Q
xcopy "%cd%\Batch\Uninstall.bat" "C:\ScansMangaExecutable" /Q
xcopy "%cd%\Batch" "C:\ScansMangaExecutable\batches" /Q
del "C:\ScansMangaExecutable\batches\Uninstall.bat" /Q
xcopy "%cd%\readmeV1.4.txt" "C:\ScansMangaExecutable" /Q

set lnk=%userprofile%\desktop\Manga_ScanV1.2.lnk
set tgpath=C:\ScansMangaExecutable\batches\startMS.bat
set icon="C:\ScansMangaExecutable\img\msicon.ico"
::set startLocation=C:\

set command=^
$objshell = New-object -ComObject WScript.Shell;^
$lnk = $objshell.CreateShortcut('%lnk%');^
$lnk.TargetPath = '%tgpath%';^
$lnk.WorkingDirectory = '%startLocation%';^
$lnk.Arguments = '%arg%';
if not "%icon%"=="" set command=%command%$lnk.IconLocation ^= '%icon%';
set command=%command%$lnk.Save();

powershell -command "& {%command%}"
set /p INSTALLPYORNOT="Do you want to install python3 ?(if python is not installed on this computer, the app will not work)(y/n)"
IF %INSTALLPYORNOT%==y (
echo. 
echo. 
echo.
echo ~~~~~~~~~~NOW INSTALLATING PYTHON~~~~~~~~~~
echo. 
echo. 
echo. 
cd Batch
call intallpy.bat
) ELSE (echo python installation cancelled.)

echo ~~~~~~~~BEFORE USING THE APP YOU MUST START C:\ScansMangaExecutable\batches\lib.bat~~~~~~~~

Pause