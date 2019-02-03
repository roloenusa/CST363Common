`-- *************************************************************
-- This script creates all 1 sample databases (cst363)
-- for Murach's MySQL by Joel Murach 
-- *************************************************************

-- ********************************************
-- CREATE THE Flight reservation system DATABASE
-- *******************************************
DROP DATABASE IF EXISTS cst363;
CREATE DATABASE cst363;

-- select the database
USE cst363;

-- create the tables
CREATE TABLE passenger
(
	passenger_ID int(10) PRIMARY key auto_increment,
	first_Name varchar(15) NOT NULL,
	last_Name varchar(15) NOT NULL,
	email varchar(20) NOT NULL
);

CREATE TABLE airports
(	
	airport_ID int(10) PRIMARY key auto_increment,	
    airport_name varchar(15) NOT NULL,
 	city_name varchar(15) NOT NULL,
 	country_name varchar(15) NOT NULL,	
    airport_code varchar(10) NOT NULL
);

CREATE TABLE flight
(
	flight_ID int(10) PRIMARY key auto_increment,
	departure_time time,
	departure_date date,
	arrival_time time,
	arrival_date date,
	flight_seat int(10)NOT NULL,
	ticket_type varchar(10) NOT NULL,
    src_airport_code varchar(10) NOT NULL,
    dest_airport_code varchar(10) NOT NULL
	
);

CREATE TABLE login
(
	acc_number int(10) PRIMARY key auto_increment,
	first_Name varchar(15)NOT NULL,
	last_Name varchar(15)NOT NULL,
	email varchar(20)NOT NULL,
    user_name varchar(20)NOT NULL,
    user_password varchar(20) NOT NULL
);
	
CREATE TABLE reservation
(
	reservation_ID int(10) PRIMARY key auto_increment,
    acc_number int NOT NULL,
 	flight_ID int NOT NULL,
    passenger_ID int NOT NULL,
    FOREIGN KEY (acc_number) REFERENCES login(acc_number),
	FOREIGN KEY (flight_ID) REFERENCES flight(flight_ID),
    FOREIGN KEY (passenger_ID) REFERENCES passenger(passenger_ID)      
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
(10, 'IG intl', 'Delhi', 'India', 'DEL');

INSERT INTO login VALUES 
(1,'abou','diaw','ad@ad.com','adiaw','1234'),
(2,'papi','diallo','pd@ad.com','papi','1234'),
(3,'cristian','ramirez','cr@ad.com','cpr', '1234'),
(4,'madi','brown','md@ad.com','mb20', '1234');


INSERT INTO flight VALUES
(1,'00:22:00','2019-02-01','13:45:11','2019-03-01',30,'economy','SFO','PHL'),
(2,'00:22:00','2019-02-01','23:45:11','2019-03-01',30,'economy','SFO','CKY'),
(3,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(4,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(5,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(6,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(7,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(8,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(9,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(10,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(11,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(12,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(13,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(14,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(15,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(16,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(17,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY'),
(18,'00:22:00','2019-04-01','26:45:11','2019-03-01',30,'business','JFK','CKY');

INSERT INTO passenger VALUES
(1,'keren','silva','ks@sv.com'),
(2,'kahmed','conde','ac@sv.com'),
(3,'bebe','yari','by@sv.com'),
(4,'fanta','coka','fk@sv.com');


