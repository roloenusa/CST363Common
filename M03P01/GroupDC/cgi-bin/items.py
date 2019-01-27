#!/usr/bin/env python3

###########################################
# Class: CST-363
# Module 03, Project 01
# Authors: 
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: Items.py
#   Entry point for item creation and retrival.
###########################################

# this file must be in the /cgi-bin/ directory of the server
import cgitb
import cgi
from models import Cnx, Item, ItemType

Cnx.Connect('gameadmin', 'sesame', 'gamedb', 'localhost')

cgitb.enable()
form = cgi.FieldStorage()

alerts = []

if form:
  type_id = int(form["type_id"].value.strip())
  name = form["name"].value.strip()
  description = form["description"].value.strip()
  cost = int(form["cost"].value.strip())
  try:
    Item.Create(type_id = type_id, name = name, description = description, cost = cost)
  except Exception as e:
    alerts.append(('danger', e))

print("Content-Type: text/html")    # HTML is following
print()                             # blank line required, end of headers

print("<TITLE>Game Database</TITLE>")
print("<html>")
print("<head>")
print('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">')
print("</head>")
print("<body>")
print("<div class='container'>")

for m in alerts:
  print("  <div class='alert alert-%s' role='alert'>%s</div>" % (m[0], m[1]))

items = Item.GetAll()
print("<h1>Item Database</h1>")
print("<hr />")
print("<table class=\"table table-striped\" >")
print(" <tr>")
print(" <th>ID</th>")
print(" <th>Name</th>")
print(" <th>Description</th>")
print(" <th>Type</th>")
print(" <th>Cost</th>")
print(" </tr>")
print(" <tbody>")
for item in items:
  print(" <tr>")
  print(" <td>%s</td>" % item.item_id)
  print(" <td>%s</td>" % item.name)
  print(" <td>%s</td>" % item.description)
  print(" <td>%s</td>" % item.type_name)
  print(" <td>%s</td>" % item.cost)
  print(" </tr>")
print(" </tbody>")
print("</table>")

print("<h2>Item Creation</h2>")
print("<hr />")
itemTypes = ItemType.GetAll()
print('<form action="/cgi-bin/items.py" method="post">')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Name</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="name" class="form-control" placeholder="item name" required>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Description</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="description" class="form-control" placeholder="item description" required>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Type</label>')
print('    <div class="col-sm-3">')
print('      <select class="form-control" name="type_id">')

for it in itemTypes:
  print('        <option value="%s" >%s</option>' % (it.type_id, it.name))

print('      </select>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Cost</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="cost" class="form-control" placeholder="item cost" required>')
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
