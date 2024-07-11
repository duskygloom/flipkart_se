; creating new user

insert into Accounts values (
	"catbuys@flipkart",
	"fishlove<3"
);

; seller adds a product

insert into Products (name, keywords, description, price, discount)
values (
	"Adidas 12345",
	"shoes,sports shoes,white shoes,adidas",
	"The brand new Adidas 12345 sports shoes!",
	2500,
	1000
);

insert into Transactions (product_id, seller_name)
values (
	1,
	"catbuys@flipkart"
);

; buyer buys a product

update Transactions set buyer_name = "duckbuys@flipkart", selling_price = 1200 where product_id = 1;

; searching a product

select * from Products natural join Transactions where buyer_name = NULL and 
(keywords like "shoes" or keywords like "shoes,%" or keywords like "%,shoes" or keywords like "%,shoes,%");
