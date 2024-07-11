@echo OFF

set prevdir=%CD%
set appdir=%HOMEDRIVE%%HOMEPATH%\Home\Programs\python\flipkart_se
set pydir=Scripts\python

cd %appdir%\src

%appdir%\%pydir% cli.py %*

cd %prevdir%

