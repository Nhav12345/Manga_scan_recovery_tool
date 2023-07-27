@echo off
set /p CONFIRMATION="Are you sure you want to uninstall?(y/n)"
if %CONFIRMATION%==y (
	cd C:\ScansMangaExecutable\batches
	.\uninstall.py
	cd C:\
	del C:\ScansMangaExecutable\app\_pycache_ /Q
	del C:\ScansMangaExecutable\app /Q
	del C:\ScansMangaExecutable\batches /Q
	del C:\ScansMangaExecutable\img /Q
	del C:\ScansMangaExecutable /Q
	rmdir C:\ScansManga
	rmdir C:\ScansMangaExecutable\app
	rmdir C:\ScansMangaExecutable\img
	rmdir C:\ScansMangaExecutable\batches
	rmdir C:\ScansMangaExecutable
	pause
) else (
	echo Uninstall process stopped.
	pause
)
exit