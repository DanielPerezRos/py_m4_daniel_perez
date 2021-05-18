DROP DATABASE IF EXISTS taller;

CREATE SCHEMA taller DEFAULT CHARACTER SET utf8;

create table taller.motor
(
	id int auto_increment,
	cc int null,
	cv int null,
	peso int null,
	constraint motor_pk primary key (id)
);

create table taller.vehicle
(
	id int auto_increment,
	fabricante varchar(50) not null,
	modelo varchar(50) null,
	color varchar(50) null,
	id_motor int null,
	constraint vehicle_pk primary key (id),
	constraint vehicle_motor_id_fk foreign key (id_motor) references motor (id) on delete set null
);
