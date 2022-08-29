-- createdb -U postgres vkinder
-- posword: nlo7

CREATE TABLE IF NOT exists users (
	id_vk INTEGER check(id_vk >= 1 and id_vk <= 9999999999) PRIMARY KEY,
	first_name VARCHAR(20) NOT null,
	last_name VARCHAR(20),
	age INTEGER check(age >= 18 and age <= 99) DEFAULT 18,
	id_sity INTEGER DEFAULT 45,
	tokens varchar(150) NOT NULL 
);


CREATE TABLE IF NOT EXISTS filters (
	id SERIAL PRIMARY KEY, 
	code_filter varchar(50)
);

CREATE TABLE IF NOT EXISTS status (
	id SERIAL PRIMARY KEY,
	type_status varchar(11) NOT NULL DEFAULT 'def_list'
);


CREATE TABLE IF NOT EXISTS elected_users (
	id_user INTEGER REFERENCES users(id_vk),
	id_elected_user INTEGER check(id_elected_user >= 1 and id_elected_user <= 9999999999),
	id_status INTEGER REFERENCES status(id)
)