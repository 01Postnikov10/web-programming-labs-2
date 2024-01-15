CREATE TABLE if not exists users (
	id serial primary key,
	username varchar(30) UNIQUE NOT NULL,
	password varchar(250) not null
);

create table if not exists articles (
	id serial primary key,
	user_id int not null,
	title varchar(50),
	article_text text,
	is_favorite bool,
	is_public bool,
	likes int,
	foreign key (user_id) references users (id)
);

insert into users (username, password) values ('alex1', '123');

