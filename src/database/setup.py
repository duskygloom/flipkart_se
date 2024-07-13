from utils.sql import *
from utils.config import *
from utils.console import *

from rich.prompt import Prompt

user_account = "flipkart_org"
user_password = "flipkart_org"
user_database = "flipkart"


def get_queries(filepath: str) -> list[str]:
    '''
    Description
    -----------
    Get each query from file and returns a list of
    all the queries.
    '''
    queries = []
    with open(filepath) as sqlfile:
        query = ""
        line = sqlfile.readline()
        while line != "":
            line = line.strip()
            if line.startswith("--") or line == "":
                line = sqlfile.readline()
                continue
            query += " " + line
            if line.endswith(";"):
                queries.append(query)
                query = ""
            line = sqlfile.readline()
    return queries


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
    config = get_config()
    # get root data
    root_database = "mysql"
    logger.warning("Root mysql account will be used for setup. It is a one time thing.")
    root_username = config['root_username']
    if not root_username:
        root_username = Prompt.ask("MySQL root username")
    root_password = config['root_username']
    if not root_password:
        root_password = Prompt.ask("MySQL root password", password=True)
    user_hostname = config['mysql_hostname']
    if not user_hostname:
        user_hostname = Prompt.ask("MySQL hostname")
    # connect to root
    sql = SQL(root_username, root_password, user_hostname, root_database)
    if not sql:
        return False
    # finding suffix
    if not sql.execute("select user from user"):
        logger.error("Could not find user table in mysql database.")
        return False
    all_users = sql.fetchall()
    sql.execute("show databases")
    all_databases = sql.fetchall()
    suffix = 1
    database_name = user_database
    while ((database_name,) in all_databases or (account_name,) in all_users):
        account_name = f"{user_account}_{suffix}"
        database_name = f"{user_database}_{suffix}"
        suffix += 1
    # create database
    if not sql.execute(f"create database {database_name}", commit=True):
        return False
    # create account
    if not sql.execute(f"create user '{account_name}'@'{user_hostname}' identified by '{user_password}'", commit=True):
        return False
    # permissions
    if not sql.execute(f"grant all on {database_name}.* to '{account_name}'@'{user_hostname}'", commit=True):
        return False
    # saving config
    config['mysql_username'] = account_name
    config['mysql_password'] = user_password
    config['mysql_hostname'] = user_hostname
    config['mysql_database'] = database_name
    save_config(config)
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
    queries = get_queries("database/secondary_setup.sql")
    for query in queries:
        if not sql.execute(query):
            return False
    sql.commit()
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
    queries = get_queries("database/optional_setup.sql")
    for query in queries:
        if not sql.execute(query):
            sql.rollback()
            return False
    sql.commit()
    return True


def reset_data(table: str = "") -> bool:
    sql = SQL.get_default()
    if not sql:
        return False
    sql.execute("show tables")
    all_tables = sql.fetchall()
    if table and (table,) in all_tables:
        if not sql.execute(f"delete from {table[0]}"):
            sql.rollback()
            return False
    elif not table:
        if not sql.execute(f"delete from transactions"):
            sql.rollback()
            return False
        if not sql.execute(f"delete from accounts"):
            sql.rollback()
            return False
        if not sql.execute(f"delete from products"):
            sql.rollback()
            return False
    sql.commit()
    return True


__all__ = [
    "primary_setup",
    "secondary_setup",
    "optional_setup",
    "reset_data"
]
