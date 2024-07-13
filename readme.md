## Windows installation

Install **python <= 3.10** from [**python.org**](https://www.python.org/downloads/)

Install venv to avoid installing dependencies system-wide by using pip.
```batch
python -m pip install virtualenv
```

Install mysql from [**mysql.com**](https://dev.mysql.com/downloads/installer/) or mariadb from [**mariadb.org**](https://mariadb.org/download/)

Create a root account in mysql/mariadb with grant privileges (*or use the root account created during installation*) and remember the login credentials. It will be required during the initial setup.
```sql
create user 'newroot'@'localhost' identified by 'password';
grant all on *.* to 'newroot'@'localhost' with grant option;
```

Clone the project repository from github.
```batch
git clone https://github.com/duskygloom/flipkart_se
```

In case git is not installed, download the zip from the [**github**](https://github.com/duskygloom/flipkart_se) and extract it.

Go into the project directory and create a virtual environment by using venv.
```batch
cd flipkart_se
python -m venv .
```

Now run the installation batch script.
```batch
.\install.bat
```

To run the application run the newly created batch file.
```batch
.\flipkart.bat
```


## Linux installation

Install **python <= 3.10** from your package manager.

Install venv to avoid installing dependencies system-wide from your package manager.

Install mysql or mariadb from your package manager.
*Note: names of packages may be different for different package managers, make sure to install the proper packages.*

Create a root account in mysql/mariadb with grant option and remember the login credentials. It will be required during the initial setup.
```sql
create user 'newroot'@'localhost' identified by 'password';
grant all on *.* to 'newroot'@'localhost' with grant option;
```

Clone the project repository from github.
```sh
git clone https://github.com/duskygloom/flipkart_se
```
In case git is not installed, download the zip from the [**github**](https://github.com/duskygloom/flipkart_se) and extract it.

Go into the project directory and create a virtual environment by using venv.
```sh
cd flipkart_se
python -m venv .
```

Now run the installation shell script.
```sh
chmod +x ./install.sh
./install.sh
```

To run the application run the newly created bash script.
```sh
./flipkart
```
