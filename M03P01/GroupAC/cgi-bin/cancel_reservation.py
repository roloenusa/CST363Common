# reservation.py
# this file must be in the /cgi-bin/ directory of the server
import cgitb , cgi
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()

reservationid = form["reservationid"].value


def db_connection():
	cnx = mysql.connector.connect(user='root', password='123.abc', database='cst363',host='127.0.0.1')
	return cnx

#Handles the css of the page
def page_style():
	print(""" 
	<head>
	<style>
	table, th, td {
	border: 1px solid black;
	}
	
	#flights {
	font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
	border-collapse: collapse;
	width: 100%;
	}

	#flights td, #flights th {
	border: 1px solid #ddd;
	padding: 8px;
	}

	#flights tr:nth-child(even){background-color: #f2f2f2;}

	#flights tr:hover {background-color: #ddd;}

	#flights th {
	padding-top: 12px;
	padding-bottom: 12px;
	text-align: left;
	background-color: #4CAF50;
	color: white;
	}   
	    input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 1px;
}

#logon{
background-color: green
}


ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}

li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 16px 18px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}

.active {
  background-color: #4CAF50;
}

body {
 background-color: #d9f2d9;
	
}
	
	
	</style>
	</head>
	
	""")

def menu():	
	print("""
	<ul>
		<li><a class="active">Reservations:</a></li>
		<li><a href="/login.html">LogOut:</a></li>
	</ul>""")

def flights():
	print("<h1>Available Flights:</h1>")
    
	print("""<table id = "flights">
	<tr>
		<th>FilightID:  </th>
		<th>Departure date/Time:</th>
		<th>Arrival date/Time:</th>
		<th>Seat available:</th>
		<th>Ticket type:</th>
		<th>Ticket From:</th>
		<th>Ticket Destination:</th>		
	</tr	
	</table>""")
	
	qsql = 'SELECT flight_id, concat(departure_date,"/",departure_time) as leaving, concat(arrival_date,"/",arrival_time) as arriving, flight_seat,ticket_type, flight_from, flight_destination from flight order by flight_id;'
	# connect to database
	try:
		cnx = db_connection()                                          
		cursor = cnx.cursor()  
		cursor.execute(qsql)	
		row = cursor.fetchone()
		while row is not None:
			print ('<tr><td>%s <td>%s <td>%s <td>%s <td>%s <td>%s <td>%s</tr>' % row)
			row = cursor.fetchone()		
		print('</table>')
		print("<br>")
		print("<br>")        
	except mysql.connector.Error as err:
		print("ERROR", err)    
	finally:
		cnx.close()  # close the connection 

def booking():
	print("<h1>Book a flight</h1>")
	print("""<div>
	<form action="/cgi-bin/reservation.py">
    <label for="fname">Passenger First Name</label>
    <input type="text" id="fname" name="firstname" required>
    <label for="lname">Passenger Last Name</label>
    <input type="text" id="lname" name="lastname" required>
	<label for="email">Passenger email</label>
    <input type="text" id="email" name="email" required>
	<label for="flightid">FlightID</label>
    <input type="text" id="flightid" name="flightid" required>
	<label for="username">Logged in Username</label>
    <input type="text" id="username" name="username" required>
    <input type="submit" value="Submit">
	</form>
	</div>""")
	
def get_reservation():
	print("<h1>Your current reservation</h1>")    
	print("""<table id = "flights">
	<tr>
		<th>Reservation ID:  </th>
		<th>Flight ID:</th>
		<th>Passenger ID:</th>
		<th>Booked by:</th>
	</tr	
	</table>""")
	find_reservations = 'SELECT * from reservation'
	try:
		cnx = db_connection()                                          
		cursor = cnx.cursor()  
		cursor.execute(find_reservations)	
		row = cursor.fetchone()
		while row is not None:
			print ('<tr><td>%s <td>%s <td>%s <td>%s </tr>' % row)
			row = cursor.fetchone()		
		print('</table>')
		print("<br>")
		print("<br>")        
	except mysql.connector.Error as err:
		print("ERROR", err)    
	finally:
		cnx.close()  # close the connection 
		
	
def booking():
	print("<h1>Book a flight</h1>")
	print("""<div>
	<form action="/cgi-bin/reservation.py">
    <label for="fname">Passenger First Name</label>
    <input type="text" id="fname" name="firstname" required>
    <label for="lname">Passenger Last Name</label>
    <input type="text" id="lname" name="lastname" required>
	<label for="email">Passenger email</label>
    <input type="text" id="email" name="email" required>
	<label for="flightid">FlightID</label>
    <input type="text" id="flightid" name="flightid" required>
	<label for="username">Logged in Username</label>
    <input type="text" id="username" name="username" required>
    <input type="submit" value="Submit">
	</form>
	</div>""")

def cancel_booking():
	print("<h1>Cancel Reservation</h1>")
	print("""<div>
		<form action="/cgi-bin/cancel_reservation.py">
		<label for="reservationid">ReservationID:</label>
		<input type="text" id="reservationid" name="reservationid" required>
		
    <input type="submit" value="Submit">
	</form>
	</div>""")
	#cancel_reservation()
	
def cancel_reservation():	

	find_reservations = 'DELETE FROM reservation WHERE reservation_id = %s'
	find_flight_id = 'SELECT flight_ID FROM reservation where reservation_ID = %s;'
	#update ticket seat count
	set_seat_count = 'UPDATE flight SET flight_seat = %s WHERE (`flight_ID` = %s);'
	get_seat_count = 'SELECT flight_seat from flight where flight_ID = %s'
	
	try:
		cnx = db_connection()                                          
		cursor = cnx.cursor()  
		cursor.execute(find_flight_id, (reservationid,))	
		row = cursor.fetchone()
		flightid = row[0]
		
		#----------------
		cursor.execute(get_seat_count,(flightid,))
		row = cursor.fetchone()
		flight_seat = row[0]
		
		#----------------------		
		cursor.execute(find_reservations, (reservationid,))
		cursor.execute(set_seat_count,(flight_seat + 1,flightid))
		cnx.commit()
	except mysql.connector.Error as err:
		print("ERROR", err)    
	finally:
		cnx.close()  # close the connection


print("Content-Type: text/html")    # HTML is following
print()
page_style()
print("<body><html>")
menu()
flights()

get_reservation()
cancel_reservation()

cancel_booking()
booking()
booking()

print("</body></html>")