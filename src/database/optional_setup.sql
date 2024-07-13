-- insert users
insert into accounts (username, password) values ('catsays', 'meow');
insert into accounts (username, password) values ('dogsays', 'woof');
insert into accounts (username, password) values ('parrotsays', 'hooman');
insert into accounts (username, password) values ('ducksays', 'quack');
insert into accounts (username, password) values ('mousesays', 'squeak');
insert into accounts (username, password) values ('frogsays', 'ribbit');

-- insert products
insert into products (name, keywords, description, price, discount) values ('Fireboltt Rise', 'fireboltt,firebolt,firebolt smart watch,fireboltt smart watch,smart watch', 'Fire-Boltt Rise BT Calling 47mm (1.85), Voice Assistance & 123 Sports Single BT Connection Smartwatch (Black Strap, Free Size)', 11999.0, 10600.0);
insert into transactions (product_id, seller_name, sold_time) values (1, 'frogsays', '2024-07-13 14:45:27');
insert into products (name, keywords, description, price, discount) values ('Fireboltt Hurricane', 'firebolt,fireboltt,firebolt hurricane,fireboltt hurricane,firebolt smart watch,fireboltt smart watch,smart watch', 'Fire-Boltt Hurricane 33.02mm (1.3) Curved Glass Display with 360 Health, 100+ Sports Modes Smartwatch (Black Strap, Free Size)', 8999.0, 7700.0);
insert into transactions (product_id, seller_name, sold_time) values (2, 'frogsays', '2024-07-13 15:09:25');
insert into products (name, keywords, description, price, discount) values ('SanDisk E61', 'sandisk,sandisk ssd,ssd,usb 3.2 ssd,1 tb ssd', 'SanDisk E61 1050 Mbps, Window, Mac OS, Android, Portable, Type C Enabled, 5 Years Warranty, USB 3.2 1 TB Wired External Solid State Drive (SSD) (Black, Red, Mobile Backup Enabled)', 28512.0, 17713.0);
insert into transactions (product_id, seller_name, sold_time) values (3, 'dogsays', '2024-07-13 16:23:40');
insert into products (name, keywords, description, price, discount) values ('BERSACHE Crocs', 'crocs,bersache,shoes,gray crocs,gray shoes', 'BERSACHE Mens Crocs (Gray, 8)', 1999.0, 1600.0);
insert into transactions (product_id, seller_name, sold_time) values (4, 'ducksays', '2024-07-13 20:23:36');