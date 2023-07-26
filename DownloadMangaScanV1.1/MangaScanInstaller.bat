@echo off

mkdir "C:\ScansManga"
mkdir "C:\ScansMangaExecutable"


xcopy "%cd%\manga_scan.py" "C:\ScansMangaExecutable" /Q
xcopy "%cd%\msicon.ico" "C:\ScansMangaExecutable" /Q
xcopy "%cd%\Batch" "C:\ScansMangaExecutable" /Q

set lnk=%userprofile%\desktop\Manga_ScanV1.0.lnk
set tgpath=C:\ScansMangaExecutable\startMS.bat
set icon="C:\ScansMangaExecutable\msicon.ico"
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

echo ~~~~~~~~BEFORE USING THE APP YOU MUST START C:\ScansMangaExecutable\lib.bat~~~~~~~~

Pause