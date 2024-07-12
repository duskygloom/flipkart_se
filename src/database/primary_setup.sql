create user 'flipkart_org'@'localhost' identified by 'flipkart_org';

create database flipkart;

grant all on flipkart.* to 'flipkart_org'@'localhost';
