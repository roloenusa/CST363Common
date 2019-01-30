# login.py
# this file must be in the /cgi-bin/ directory of the server
import cgitb , cgi
import mysql.connector
cgitb.enable()
form = cgi.FieldStorage()
username = form ["username"].value
password = form["password"].value


def db_connection():
	cnx = mysql.connector.connect(user='root',
		password='123.abc',
        database='cst363',
        host='127.0.0.1')
	return cnx

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
	
	
	</style>
	</head>
	
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
	


def login():
	print("Content-Type: text/html")    # HTML is following
	print()
	page_style()
	
	print("<body><html>")
	#print('<div id="logon"><span style="color:white">Logon as: %s</span></div>' %(user_name))
	qsql = 'select * from login where user_name = %s'
	insert_sql = 'insert into login (user_name, password, visits) values (%s, %s, 1)'
	update_sql = 'update login set visits = visits + 1 where user_name=%s'
	# connect to database
	cnx = db_connection()
    #  code to do SQL goes here
	cursor = cnx.cursor()
	cursor.execute(qsql, (username,))
	row = cursor.fetchone()
	if row == None: 
	# must be first visit or user does not exists
		print('No account exist for this Userid, please register')
		print('<a href="http://127.0.0.1:8000/login.html">Click here to go back</a>')
	else:
            # retrieve number of visits value from row and increment
		if password == row[5]:
			flights()
			booking()
			get_reservation()
			cancel_booking()
			
			#process booking form

						
		else:
			print('your password is incorrect')
			print('<a href="http://127.0.0.1:8000/login.html">Click here to go back</a>')
    
	print("</body></html>")
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
def cancel_booking():
	print("<h1>Cancel booking</h1>")
	print("""<div>
		<form action="/cgi-bin/cancel_reservation.py">
		<label for="reservationid">ReservationID:</label>
		<input type="text" id="reservationid" name="reservationid" required>
		
    <input type="submit" value="Submit">
	</form>
	</div>""")
login()
		
  

		
    

    


