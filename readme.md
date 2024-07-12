## Windows installation

1. Install `python <= 3.10` from [python.org](https://www.python.org/downloads/)
2. Install venv to avoid installing dependencies system-wide by using pip.
`python -m pip install virtualenv`
3. Install mysql from [mysql.com](https://dev.mysql.com/downloads/installer/) or mariadb from [mariadb.org](https://mariadb.org/download/)
4. Create a root account in mysql/mariadb and remember the login credentials. It will be required during the initial setup.
5. Clone the project repository from github.
`git clone https://github.com/duskygloom/flipkart_se`
In case git is not installed, download the zip from the [github](https://github.com/duskygloom/flipkart_se) and extract it.
6. Go into the project directory and create a virtual environment by using venv.
`python -m venv .`
7. Now run the installation batch script.
`.\install.bat`
8. To run the application run the newly created batch file.
`.\flipkart.bat`


## Linux installation

1. Install `python <= 3.10` from your package manager.
2. Install venv to avoid installing dependencies system-wide from your package manager.
3. Install mysql or mariadb from your package manager. Note that the names of packages may be different for different package managers, make sure to install the proper packages.
4. Create a root account in mysql/mariadb and remember the login credentials. It will be required during the initial setup.
5. Clone the project repository from github.
`git clone https://github.com/duskygloom/flipkart_se`
In case git is not installed, download the zip from the [github](https://github.com/duskygloom/flipkart_se) and extract it.
6. Go into the project directory and create a virtual environment by using venv.
`python -m venv .`
7. Now run the installation shell script.
`chmod +x ./install.sh && ./install.sh`
8. To run the application run the newly created bash script.
`./flipkart`
