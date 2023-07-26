@echo off
set /p CONFIRMATION="Are you sure you want to uninstall?(y/n)"
if %CONFIRMATION%==y (
	.\uninstall.py
	cd C:\
	del C:\ScansMangaExecutable /Q
	rmdir C:\ScansManga
	rmdir C:\ScansMangaExecutable
	pause
) else (
	echo Uninstall process stopped.
	pause
)
exit