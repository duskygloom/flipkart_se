-- products table values

insert into products (name, keywords, description, price, discount)
values (
	"Adidas 12345",
	"shoes,sports shoes,white shoes,adidas",
	"The brand new Adidas 12345 sports shoes!",
	2500,
	1000
);

insert into products (name, keywords, description, price, discount)
values (
	"SKYBAGS 34L",
	"bag,school bag,blue bag,skybag,skybags",
	"The brand new Skybag 34L, specially for student!",
	1500,
	500
);

insert into products (name, keywords, description, price, discount)
values (
	"Boat Stone 352",
	"speaker,boat,stone,bluetooth speaker",
	"The brand new bluetooth speaker Boat Stone 352 10W RMS speaker",
	3490,
	2091
);

insert into products (name, keywords, description, price, discount)
values (
	"Samsung S24 Ultra",
	"mobile,5g mobile,samsung,s24 ultra,flagship smartphone,samsung s24 ultra",
	"Behold the Samsung Galaxy S24 Ultra smartphone, an exceptional amalgamation of incredible technology and superior sophistication. Whether you're typing up a storm or jotting something down, Note Assist makes a long story short. New AI-powered editing options let you get the photo you want, like relocating objects and intelligently filling in the space they left behind. With a durable shield of titanium built right into the frame and better scratch resistance with Corning Gorilla Armor, your IP68 water and dust-resistant Galaxy S24 Ultra is ready for adventure. Write, tap, and navigate with the precision your fingers wish they had on the new, flat display.",
	144999,
	5000
);

insert into products (name, keywords, description, price, discount)
values (
	"MILTON Thermosteel 1000 ml Flask",
	"milton,water bottle,steel water bottle,thermosteel bottle",
	"The brand new Milton Thermosteel 1000 ml waterbottle!",
	1205,
	206
);

insert into products (name, keywords, description, price, discount)
values (
	"Lenovo Legion Intel Core i7 14th Gen 14650HX",
	"laptop,lenovo,legion",
	"The brand new Lenovo Legion Intel core i7 14th Gen with 16 GB/1 TB SSD/Windows 11 Home/8 GB Graphics/NVIDIA GeForce RTX 4060",
	196590,
    51606
);

-- accounts table values

insert into accounts values (
	"duckbuys@flipkart",
	"12345678"
);

insert into accounts values (
	"catbuys@flipkart",
	"fishlove<3"
);

insert into accounts values (
	"bagbuys@flipkart",
	"987654321"
);

insert into accounts values (
	"schoolbagbuys@flipkart",
	"fishlove<3"
);

insert into accounts values (
	"speakerbuys@flipkart",
	"352"
);

insert into accounts values (
	"bluetoothspeakerbuys@flipkart",
	"fishlove<3"
);

insert into accounts values (
	"mobilebuys@flipkart",
	"24"
);

insert into accounts values (
	"samsungmobilebuys@flipkart",
	"fishlove<3"
);

insert into accounts values (
	"bottlebuys@flipkart",
	"1000"
);

insert into accounts values (
	"miltonbottlebuys@flipkart",
	"fishlove<3"
);

insert into accounts values (
	"laptopbuys@flipkart",
	"196590"
);

insert into accounts values (
	"lenovolaptopbuys@flipkart",
	"fishlove<3"
);

-- transactions table values

insert into transactions values (
	1,
	"duckbuys@flipkart",
	"catbuys@flipkart",
	1000
);

insert into transactions values (
	2,
	"bagbuys@flipkart",
	"schoolbagbuys@flipkart",
	500
);

insert into transactions values (
	3,
	"speakerbuys@flipkart",
	"bluetoothspeakerbuys@flipkart",
	2091
);

insert into transactions values (
	4,
	"mobilebuys@flipkart",
	"samsungmobilebuys@flipkart",
	5000
);

insert into transactions values (
	5,
	"bottlebuys@flipkart",
	"miltonbottlebuys@flipkart",
	206
);

insert into transactions values (
	6,
	"laptopbuys@flipkart",
	"lenovolaptopbuys@flipkart",
	51606
);
