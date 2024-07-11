create user "flipkart_org"@"localhost" identified by "flipkart_org";

create database flipkart;

grant all on flipkart.* to flipkart_org;

use flipkart;

create table Products (
    product_id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50),
    keywords varchar(1000),
    description varchar(1000),
    price decimal(10, 2),
    discount decimal(10, 2)
);

create table Accounts (
    username varchar(50) PRIMARY KEY,
    password varchar(50)
);

create table Transactions (
    product_id int PRIMARY KEY,
    buyer_name varchar(50),
    seller_name varchar(50),
    selling_price decimal(10, 2),
    foreign key (product_id) references Products(product_id),
    foreign key (buyer_name) references Accounts(username),
    foreign key (seller_name) references Accounts(username)
);
