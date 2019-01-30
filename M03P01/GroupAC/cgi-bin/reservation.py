# reservation.py
# this file must be in the /cgi-bin/ directory of the server
import cgitb , cgi
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()

firstname = form ["firstname"].value
lastname = form["lastname"].value
email = form["email"].value
flightid = form["flightid"].value
username = form["username"].value


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
		
	
def reservation():
	insreservation = 'INSERT INTO reservation (flight_ID,passenger_ID, acc_number)value(%s,%s, %s)'
	insqsql = 'INSERT INTO passenger(first_name,last_name, email)VALUES(%s,%s, %s)';
	
	# Check if passenger exists
	chkpassenger = 'select * from passenger where first_name = %s and last_name = %s'
	
	#Find a reservation by ID
	chkreservation = 'select * from reservation where reservation_ID = %s'
	
	#find reservation by user_name
	user_reservation = 'SELECT reservation.acc_number, reservation.reservation_ID, login.user_name from reservation inner join login on  reservation.acc_number = login.acc_number'
	# get user ID from username	
	get_userid = 'SELECT acc_number from login where user_name = %s'
	
	#get ticket seat count
	get_seat_count = 'SELECT flight_seat from flight where flight_ID = %s'
	
	#update ticket seat count
	set_seat_count = 'UPDATE flight SET flight_seat = %s WHERE (`flight_ID` = %s);'
	
	
	cnx = db_connection()
	cursor = cnx.cursor()  
	cursor.execute(chkpassenger,(firstname,lastname))
	row = cursor.fetchone()
	if row == None: 
		# must be first visit or user does not exists	
		cursor.execute(insqsql,(firstname,lastname, email))
		cnx.commit()
		cursor.execute(chkpassenger,(firstname,lastname))
		row = cursor.fetchone()
	passenger_id = row[0]
	cnx.close()
		
	#obtain current logged in user name's ID
	cnx = db_connection()
	cursor = cnx.cursor()
	cursor.execute(get_userid,(username,))
	row = cursor.fetchone()
	acc_number = row[0]
	
	#update ticket seat count
	
	
	cursor.execute(get_seat_count,(flightid,))
	row = cursor.fetchone()
	flight_seat = row[0]
	
	if flight_seat < 0:
		print("<h3> There is no more space on this plane. Choose a different flight</h3>")
	else:
		cursor.execute(set_seat_count,(flight_seat - 1,flightid))
		cnx.commit()
		#add reservation
		cnx = db_connection()
		cursor = cnx.cursor()  
		cursor.execute(insreservation,(flightid,passenger_id,acc_number))
		cnx.commit()
		cnx.close()
		print("""<p> Your regirstration has been successfully completed. 
		Please note that you have 24 hours to cancel the reservation.
		To cancel the reservation, click on the cancall reservation button</p>
		""")
	
	

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

def cancel_booking():
	print("<h1>Cancel Booking</h1>")
	print("""<div>
		<form action="/cgi-bin/cancel_reservation.py">
		<label for="reservationid">ReservationID:</label>
		<input type="text" id="reservationid" name="reservationid" required>
		
    <input type="submit" value="Submit">
	</form>
	</div>""")
	


print("Content-Type: text/html")    # HTML is following
print()
page_style()
print("<body><html>")
menu()
reservation()
flights()

get_reservation()
cancel_booking()
booking()
print("</body></html>")