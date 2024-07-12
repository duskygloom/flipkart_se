@echo OFF

set runscript=flipkart.bat

echo Installing requirements...
%CD%\Scripts\pip install -r requirements.txt

echo Writing script...
echo @echo OFF> %runscript%
echo set prevdir=%%CD%%>> %runscript%
echo set appdir=%CD%>> %runscript%
echo cd %%appdir%%\src>> %runscript%
echo %%appdir%%\Scripts\python cli.py %%*>> %runscript%
echo cd %%prevdir%%>> %runscript%
