; Products table values

insert into Products (name, keywords, description, price, discount)
values (
	"Adidas 12345",
	"shoes,sports shoes,white shoes,adidas",
	"The brand new Adidas 12345 sports shoes!",
	2500,
	1000
);

; Accounts table values

insert into Accounts values (
	"duckbuys@flipkart",
	"12345678"
);

insert into Accounts values (
	"catbuys@flipkart",
	"fishlove<3"
);

; Transactions table values

insert into Transactions values (
	1,
	"duckbuys@flipkart",
	"catbuys@flipkart",
	1000
);
