create table products (
    product_id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(50),
    keywords varchar(1000),
    description varchar(1000),
    price decimal(10, 2),
    discount decimal(10, 2)
);

create table accounts (
    username varchar(50) PRIMARY KEY,
    password varchar(50),
    address varchar(200) default "Not provided",
    contact varchar(50) default "Not provided"
);

create table transactions (
    product_id int PRIMARY KEY,
    seller_name varchar(50),
    sold_time datetime,
    buyer_name varchar(50),
    bought_time datetime,
    bought_price decimal(10, 2),
    foreign key (product_id) references products(product_id),
    foreign key (seller_name) references accounts(username),
    foreign key (buyer_name) references accounts(username)
);
