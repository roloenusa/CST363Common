-- *************************************************************
-- This script creates all 1 sample databases (cst363)
-- for Murach's MySQL by Joel Murach 
-- *************************************************************

-- ********************************************
-- CREATE THE Flight reservation system DATABASE
-- *******************************************

-- create the database
DROP DATABASE IF EXISTS cst363;
CREATE DATABASE cst363;

-- select the database
USE cst363;

-- create the tables
CREATE TABLE passenger
(
	passenger_ID int(10) PRIMARY key auto_increment,
	first_Name varchar(15),
	last_Name varchar(15),
	email varchar(20)
);

CREATE TABLE airports
(	
	airport_ID int(10) PRIMARY key auto_increment,	
    airport_name varchar(15),
 	city_name varchar(15),
 	country_name varchar(15),	
    airport_code varchar(10)
);

CREATE TABLE flight
(
	flight_ID int(10) PRIMARY key auto_increment,
	departure_time time,
	departure_date date,
	arrival_time time,
	arrival_date date,
	flight_seat int(10),
	ticket_type varchar(10),
	flight_from varchar(15),
	flight_destination varchar(15),
	airport_ID int,
	FOREIGN KEY (airport_ID) REFERENCES airports(airport_ID)
);

CREATE TABLE reservation
(
	reservation_ID int(10) PRIMARY key auto_increment,
    acc_number int(10),
 	flight_ID int,
    passenger_ID int,
	FOREIGN KEY (flight_ID) REFERENCES flight(flight_ID),
    FOREIGN KEY (passenger_ID) REFERENCES passenger(passenger_ID)      
);



CREATE TABLE login
(
	acc_number int(10) PRIMARY key auto_increment,
	first_Name varchar(15),
	last_Name varchar(15),
	email varchar(20),
    user_name varchar(20),
    user_password varchar(20)
    );
	
	
INSERT INTO airports VALUES
(1, 'San Fran Int', 'San Francisco', 'USA', 'SFO'),
(2, 'Conakry Int', 'Conakry', 'Guinea', 'CKY'),
(3, 'Miami Int', 'Miami', 'USA', 'MIA'),
(4, 'John FK Int', 'New York City', 'USA', 'JFK'),
(5, 'Phily Int', 'Phily', 'USA', 'PHL'),
(7, 'H-J ATL Intl', 'Atlanta', 'USA', 'ATL'),
(8, 'BC Intl', 'Bijing', 'China', 'PEK'),
(9, 'T Haneda', 'Tokyo', 'Japan', 'HND'),
(10, 'Indira Gandhi intl', 'Delhi', 'India', 'DEL');

INSERT INTO login VALUES 
(1,'abou','diaw','ad@ad.com','adiaw','1234'),
(2,'papi','diallo','pd@ad.com','papi','1234'),
(3,'cristian','ramirez','cr@ad.com','cpr', '1234'),
(4,'madi','brown','md@ad.com','mb20', '1234');


INSERT INTO flight VALUES
(1,'00:22:00','2019-02-01','13:45:11','2019-03-01',30,'economy','SFO','PHL',1),
(2,'00:22:00','2019-02-01','23:45:11','2019-03-01',30,'economy','SFO','CKY',2),
(3,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY',3);

INSERT INTO passenger VALUES
(1,'keren','silva','ks@sv.com'),
(2,'kahmed','conde','ac@sv.com'),
(3,'bebe','yari','by@sv.com'),
(4,'fanta','coka','fk@sv.com');


INSERT INTO reservation VALUES
(1,2,1,1),
(3,4,1,2),
(2,5,1,4);


