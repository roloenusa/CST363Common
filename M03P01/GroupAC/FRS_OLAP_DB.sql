

-- create the tables

CREATE DATABASE frs_olap_db;

-- select the database
use frs_olap_db;

-- create tables 

CREATE TABLE airports
(	
	airport_ID int(10) PRIMARY key auto_increment,	
    airport_name varchar(15) NOT NULL,
 	city_name varchar(15) NOT NULL,
 	country_name varchar(15) NOT NULL,	
    airport_code varchar(10) NOT NULL
);

CREATE TABLE passenger
(
	passenger_ID int(10) PRIMARY key auto_increment,
	passenger_name varchar(30) NOT NULL,	
	email varchar(20) NOT NULL
	
);

CREATE TABLE flight
(
	flight_ID int(10) PRIMARY key auto_increment,
	departure_date date NOT NULL,
    arrival_date date NOT NULL,
	src_airport_code varchar(10) NOT NULL,
    dest_airport_code varchar(10) NOT NULL,
    ticket_type varchar (10) NOT NULL
	
);

CREATE TABLE flight_reservations(
	reservation_id int NOT NULL,
	flight_ID int NOT NULL,
    passenger_ID int NOT NULL,
    FOREIGN KEY (flight_ID) REFERENCES flight(flight_ID),
    FOREIGN KEY (passenger_ID) REFERENCES passenger(passenger_ID)      
);


/*Load airport information*/

INSERT INTO frs_olap_db.airports (airport_ID, airport_name, city_name,country_name, airport_code)
SELECT airport_id, airport_name, city_name,country_name,airport_code
from cst363.airports;



/*Load passenger information*/
INSERT INTO frs_olap_db.passenger(passenger_ID,passenger_name,email)
SELECT passenger_ID, concat(trim(first_name),' ',trim(last_name)),email
FROM cst363.passenger;




/*Load flight information*/

INSERT INTO frs_olap_db.flight(flight_ID,departure_date, arrival_date,src_airport_code,dest_airport_code, ticket_type)
SELECT flight_id, departure_date, arrival_date, src_airport_code, dest_airport_code, ticket_type
FROM cst363.flight;


INSERT INTO frs_olap_db.flight_reservations(reservation_id, flight_ID, passenger_ID)
SELECT reservation_id, flight_ID, passenger_ID
FROM cst363.reservation;







