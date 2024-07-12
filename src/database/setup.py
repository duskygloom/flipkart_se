from utils.sql import *
from utils.config import *
from utils.styles import *
from utils.console import *

from rich.prompt import Prompt

config = get_config()
styles = get_styles()

user_account = "flipkart_org"
user_password = "flipkart_org"
user_database = "flipkart"


def primary_setup() -> bool:
    '''
    Description
    -----------
    Setup from the root mysql account.
    Creates a new account and database for flipkart.

    Returns
    -------
    Returns True if setup successful, else returns False.
    '''
    # get root data
    root_database = "mysql"
    logger.warning("Root mysql account will be used for setup. It is a one time thing.")
    root_username = config['root_username']
    if not root_username:
        root_username = Prompt.ask("MySQL root username")
    root_password = config['root_username']
    if not root_password:
        root_password = Prompt.ask("MySQL root password", password=True)
    # connect to root
    sql = SQL(root_username, root_password, config['mysql_hostname'], root_database)
    if not sql:
        return False
    # check if mysql database exists
    if not sql.execute("select user from user"):
        logger.error("Could not find user table in mysql database.")
        return False
    # create new account
    all_users = sql.fetchall()
    suffix = 1
    account_name = user_account
    while ((account_name,) in all_users):
        account_name = f"{user_account}_{suffix}"
        suffix += 1
    user_hostname = config['mysql_hostname']
    if not user_hostname:
        user_hostname = Prompt.ask("MySQL hostname")
    sql.execute(f"create user '{account_name}'@'{user_hostname}' identified by '{user_password}'", commit=True)
    config['mysql_username'] = account_name
    config['mysql_password'] = user_password
    config['mysql_hostname'] = user_hostname
    save_config(config)
    # create new database
    sql.execute("show databases")
    all_databases = sql.fetchall()
    suffix = 1
    database_name = user_database
    while ((database_name,) in all_databases):
        database_name = f"{user_database}_{suffix}"
        suffix += 1
    if not sql.execute(f"create database {database_name}", commit=True):
        return False
    config['mysql_database'] = database_name
    save_config(config)
    # permissions
    if not sql.execute(f"grant all on {config['mysql_database']}.* to '{config['mysql_username']}'@'{config['mysql_hostname']}'", commit=True):
        return False
    return True


def secondary_setup() -> bool:
    '''
    Description
    -----------
    In this setup, root account is not used.
    The account created in the root setup is used to make tables.

    Returns
    -------
    Returns True if setup successful, else returns False.
    '''
    sql = SQL.get_default()
    if not sql:
        return False
    # products table
    query = '''create table products (
        product_id int PRIMARY KEY AUTO_INCREMENT,
        name varchar(50),
        keywords varchar(1000),
        description varchar(1000),
        price decimal(10, 2),
        discount decimal(10, 2)
    )'''
    # accounts table
    if not sql.execute(query, commit=True):
        return False
    query = '''create table accounts (
        username varchar(50) PRIMARY KEY,
        password varchar(50),
        address varchar(200)
    )'''
    if not sql.execute(query, commit=True):
        return False
    # transactions table
    query = '''create table transactions (
        product_id int PRIMARY KEY,
        seller_name varchar(50),
        sold_time datetime,
        buyer_name varchar(50),
        bought_time datetime,
        bought_price decimal(10, 2),
        foreign key (product_id) references products(product_id),
        foreign key (seller_name) references accounts(username),
        foreign key (buyer_name) references accounts(username)
    )'''
    if not sql.execute(query, commit=True):
        return False
    return True


def optional_setup() -> bool:
    '''
    Description
    -----------
    Fill some dummy values in the database.

    Returns
    -------
    Returns True if setup successful, else returns False.
    '''
    sql = SQL.get_default()
    if not sql:
        return False
    queries = []
    with open("database/optional_setup.sql") as sqlfile:
        query = ""
        line = sqlfile.readline().strip()
        while line != "":
            if line.startswith("--") or line == "":
                line = sqlfile.readline()
                continue
            elif line.endswith(";"):
                query += " " + line
                queries.append(query)
                console.print(query)
            else:
                query += " " + line
            line = sqlfile.readline()
    return True



__all__ = [
    "primary_setup",
    "secondary_setup",
    "optional_setup"
]
