@echo OFF

set runscript=flipkart.bat

echo @echo OFF> %runscript%
echo set prevdir=%%CD%%>> %runscript%
echo set appdir=%CD%>> %runscript%
echo set pydir=Scripts\python>> %runscript%
echo cd %%appdir%%\src>> %runscript%
echo %%appdir%%\%%pydir%% cli.py %%*>> %runscript%
echo cd %%prevdir%%>> %runscript%