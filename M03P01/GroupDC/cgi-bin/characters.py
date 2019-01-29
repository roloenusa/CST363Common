#!/usr/bin/env python3

###########################################
# Class: CST-363
# Module 03, Project 01
# Authors:
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: Characters.py
#   Entry point for character creation and retrival.
###########################################

# this file must be in the /cgi-bin/ directory of the server
import cgitb
import cgi
from models import Cnx, Character, Klass

Cnx.Connect('gameadmin', 'sesame', 'gamedb', 'localhost')

cgitb.enable()
form = cgi.FieldStorage()

print("Content-Type: text/html")    # HTML is following
print()                             # blank line required, end of headers

print("<TITLE>Game Database</TITLE>")
print("<html>")
print("<head>")
print('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">')
print("</head>")
print("<body>")
print("<div class='container'>")

characters = Character.GetAll()
print("<h1>Character Database</h1>")
print("<hr />")
print("<table class=\"table table-striped\" >")
print(" <tr>")
print(" <th>ID</th>")
print(" <th>Name</th>")
print(" <th>Class</th>")
print(" <th>Level</th>")
print(" <th>Experience</th>")
print(" <th>Gold</th>")
print(" <th></th>")
print(" </tr>")
print(" <tbody>")
for character in characters:
  print(" <tr>")
  print(" <td>%s</td>" % character.character_id)
  print(" <td>%s</td>" % character.name)
  print(" <td>%s</td>" % character.class_name)
  print(" <td>%s</td>" % character.level)
  print(" <td>%s</td>" % character.experience)
  print(" <td>%s</td>" % character.gold)
  print(" <td><a href='./character.py?character_id=%s'>Load</a></td>" % character.character_id)
  print(" </tr>")
print(" </tbody>")
print("</table>")

classes = Klass.GetAll()
print("<h2>Character Creation</h2>")
print("<hr />")
print('<form action="/cgi-bin/character.py" method="post">')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Name</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="name" class="form-control" placeholder="character name" required>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Class</label>')
print('    <div class="col-sm-3">')
print('      <select class="form-control" name="class_id">')

for c in classes:
  print('        <option value="%s" >%s</option>' % (c.class_id, c.name))

print('      </select>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Level</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="level" value="0" class="form-control" placeholder="level" required>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Experience</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="experience" value="0" class="form-control" placeholder="experience" required>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Gold</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="gold" value="0" class="form-control" placeholder="gold" required>')
print('    </div>')
print('  </div>')
print('')
print('  <div class="form-group row">')
print('    <div class="col-sm-6">')
print('      <input type="submit" name="create" value="create" class="btn btn-primary" />')
print('    </div>')
print('  </div>')
print('</form>')

print("</div>")
print("</body></html>")
Cnx.Disconnect()
