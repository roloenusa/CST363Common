-- OLAP Query

-- Find the number of fight per airport per airpor in the month of February
SELECT count(r.flight_id) as NumberOfFlightPerAirportInFEB, a.airport_name as 'Airport Name', a.city_name AS 'City', a.country_name AS 'Country'
from flight_reservations r join flight f on r.flight_id = f.flight_id 
join airports a on f.src_airport_code = a.airport_code
where departure_date between '2019-02-01' and '2019-02-31' and f.src_airport_code= 'JFK';

-- Find total number of flight and the average passenger
Select count(r.flight_id) as numberOfFlights, round(avg(p.passenger_id), 0) as averagePassenger 
from passenger p join flight_reservations r on p.passenger_id = r.passenger_id
 join flight f on r.flight_id = f.flight_id
where f.dest_airport_code ='PHL';

-- Find flight with destination to USA
SELECT r.flight_id as NumberOfFlight, a.airport_name as 'Airport Name', a.city_name AS 'City', a.country_name AS 'Country'
from flight_reservations r join flight f on r.flight_id = f.flight_id 
join airports a on f.dest_airport_code = a.airport_code
where a.country_name = 'USA'
group by a.airport_name;

-- Find flight with international destination
SELECT r.flight_id as NumberOfFlight, a.airport_name as 'Airport Name', a.city_name AS 'City', a.country_name AS 'Country'
from flight_reservations r join flight f on r.flight_id = f.flight_id 
join airports a on f.dest_airport_code = a.airport_code
where a.country_name <> 'USA'
group by a.airport_name;

-- reservation_id to the count, then group by id and do a roll up

SELECT count(r.reservation_ID), f.ticket_type FROM flight_reservations r JOIN flight f ON r.flight_ID = f.flight_ID
WHERE f.ticket_type = 'economy'
group by r.reservation_ID with rollup;



