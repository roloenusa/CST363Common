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
	
	
	ul{
		list-style-type: none;
		margin: 0;
		padding: 0;
		overflow: hidden;
		background-color: #333;
	  }

	li{
		float: left;
	  }

	li a{
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
	
	</style>
	</head>
	
	""")

def flights():
	print("<h3>all available flights:</h3>")    
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
	
	qsql = 'SELECT flight_id, concat(departure_date,"/",departure_time) as leaving, concat(arrival_date,"/",arrival_time) as arriving, flight_seat,ticket_type, src_airport_code, dest_airport_code from flight order by flight_id;'
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

def get_reservation():
	print("<h3>Your current reservation:</h3>")    
	print("""<table id = "flights">
	<tr>
		<th>Reservation ID:  </th>
		<th>Flight ID:</th>
		<th>Passenger ID:</th>
		<th>Booked by:</th>
	</tr	
	</table>""")
	find_reservations = 'SELECT * from reservation where  (select acc_number from login where user_name = %s)'
	try:
		cnx = db_connection()                                          
		cursor = cnx.cursor()  
		cursor.execute(find_reservations,(username,))	
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

# Function handles login
def login():
		
	qsql = 'select * from login where user_name = %s'

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
			print("""<ul>
						<li><a href="http://127.0.0.1:8000/login.html">Logout</a></li>
					</ul>""")
			print('<a href="http://127.0.0.1:8000/reservation.html">View Your Reservation |</a>')
			print('<a href="http://127.0.0.1:8000/reservation.html">Make a Reservation |</a>')
			print('<a href="http://127.0.0.1:8000/cancel.html">Cancel a Reservation |</a>')
			print('<a href="http://127.0.0.1:8000/search.html">Search a Reservation |</a>')
			print("<h2>Welcome to FRS!<h2>")
			get_reservation()
			flights()
			print("</body></html>")
			
			
			#process booking form

						
		else:
			print('your password is incorrect')
			print('<a href="http://127.0.0.1:8000/login.html">Click here to go back</a>')




print("Content-Type: text/html")    # HTML is following
print()
page_style()
print("<body><html>")
#site

login()


		
  

	

		
    

    


