@echo OFF

set appdir=%CD%
set runscript=flipkart.bat

echo Installing requirements...
%appdir%\Scripts\pip install -r requirements.txt

echo:
echo Database setup...
cd src
copy empty_config.json config.json
%appdir%\Scripts\python cli.py setup required

cd %appdir%

echo:
echo Writing script...
echo @echo OFF> %runscript%
echo set prevdir=%%CD%%>> %runscript%
echo set appdir=%appdir%>> %runscript%
echo cd %%appdir%%\src>> %runscript%
echo %%appdir%%\Scripts\python cli.py %%*>> %runscript%
echo cd %%prevdir%%>> %runscript%

echo:
echo Done.
