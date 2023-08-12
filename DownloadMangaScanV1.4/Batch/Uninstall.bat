@echo off
set /p CONFIRMATION="Are you sure you want to uninstall?(y/n)"
if %CONFIRMATION%==y (
	cd C:\
	rmdir C:\ScansManga /s /q
	rmdir C:\ScansMangaExecutable /s /q
	pause
) else (
	echo Uninstall process stopped.
	pause
)
exit