@echo off
:start
cls

set python_ver=39

cd \
cd C:\Program Files\python%python_ver%\Scripts\
pip install lxml
pip install beautifulsoup4
pip install requests
pip install art
pip install termcolor
pip install pillow
pip install customtkinter
pause
