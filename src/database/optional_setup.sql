-- insert users
insert into accounts (username, password) values ('catsays', 'meow');
insert into accounts (username, password) values ('dogsays', 'woof');
insert into accounts (username, password) values ('parrotsays', 'hooman');
insert into accounts (username, password) values ('ducksays', 'quack');
insert into accounts (username, password) values ('mousesays', 'squeak');
insert into accounts (username, password) values ('frogsays', 'ribbit');

-- insert products
insert into products (product_id, name, keywords, description, price, discount) values (1, 'Fireboltt Rise', 'fireboltt,firebolt,firebolt smart watch,fireboltt smart watch,smart watch', 'Fire-Boltt Rise BT Calling 47mm (1.85), Voice Assistance & 123 Sports Single BT Connection Smartwatch (Black Strap, Free Size)', 11999.0, 10600.0);
insert into transactions (product_id, seller_name, sold_time) values (1, 'frogsays', '2024-07-13 14:45:27');
insert into products (product_id, name, keywords, description, price, discount) values (2, 'Fireboltt Hurricane', 'firebolt,fireboltt,firebolt hurricane,fireboltt hurricane,firebolt smart watch,fireboltt smart watch,smart watch', 'Fire-Boltt Hurricane 33.02mm (1.3) Curved Glass Display with 360 Health, 100+ Sports Modes Smartwatch (Black Strap, Free Size)', 8999.0, 7700.0);
insert into transactions (product_id, seller_name, sold_time) values (2, 'frogsays', '2024-07-13 15:09:25');