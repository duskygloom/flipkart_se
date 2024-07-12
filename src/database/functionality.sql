-- creating new user

insert into accounts values (
	"catbuys@flipkart",
	"fishlove<3"
);


-- seller adds a product

insert into products (name, keywords, description, price, discount)
values (
	"Adidas 12345",
	"shoes,sports shoes,white shoes,adidas",
	"The brand new Adidas 12345 sports shoes!",
	2500,
	1000
);

insert into transactions (product_id, seller_name, sold_time)
values (
	1,
	"catbuys@flipkart",
	"..."
);


-- buyer buys a product

update transactions set buyer_name = "duckbuys@flipkart", sold_time = "...", bought_price = 1200 where product_id = 1;


-- searching a product

select * from products natural join transactions where buyer_name = NULL and 
(keywords like "shoes" or keywords like "shoes,%" or keywords like "%,shoes" or keywords like "%,shoes,%");


-- logging in

select username from accounts where username == "duckbuys@flipkart" and password == "12345678";
-- update config['current_user'] in config file


-- logging out

-- set config['current_user'] = "" in config file
