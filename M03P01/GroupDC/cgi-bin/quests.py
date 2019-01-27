#!/usr/bin/env python3

###########################################
# Class: CST-363
# Module 03, Project 01
# Authors: 
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: Quests.py
#   Entry point for quest creation and retrival.
###########################################

# this file must be in the /cgi-bin/ directory of the server
import cgitb
import cgi
from models import Cnx, Quest, QuestType, QuestLog

Cnx.Connect('gameadmin', 'sesame', 'gamedb', 'localhost')

cgitb.enable()
form = cgi.FieldStorage()

alerts = []

character_id = False
quest_id = False

if 'create' in form:
  type_id = int(form["type_id"].value.strip())
  title = form["title"].value.strip()
  description = form["description"].value.strip()
  reward = int(form["reward"].value.strip())
  xp = int(form["xp"].value.strip())
  try:
    Quest.Create(type_id = type_id, title = title, description = description, reward = reward, xp = xp)
  except Exception as e:
    alerts.append(('danger', e))

if 'character_id' in form:
  character_id = form['character_id'].value

if 'quest_id' in form:
  quest_id = form['quest_id'].value

if character_id and quest_id:
  res = QuestLog.AddQuest(character_id, quest_id)
  if res:
    alerts.append(('success', "Quest added!"))
  else:
    alerts.append(('danger', "Unable to add quest."))

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

quests = Quest.GetAll()
print("<h1>Quest Database</h1>")
print("<hr />")
print("<table class=\"table table-striped\" >")
print(" <tr>")
print(" <th>ID</th>")
print(" <th>Name</th>")
print(" <th>Description</th>")
print(" <th>Type</th>")
print(" <th>Reward</th>")
print(" <th>Experience</th>")
print(" <th></th>")
print(" </tr>")
print(" <tbody>")
for quest in quests:
  print(" <tr>")
  print(" <td>%s</td>" % quest.quest_id)
  print(" <td>%s</td>" % quest.title)
  print(" <td>%s</td>" % quest.description)
  print(" <td>%s</td>" % quest.type_name)
  print(" <td>%s</td>" % quest.reward)
  print(" <td>%s</td>" % quest.xp)
  if QuestLog.CanAdd(character_id, quest.quest_id):
    print(" <td><a href='./quests.py?character_id=%s&quest_id=%s'>Add</a></td>" % (character_id, quest.quest_id))
  else:
    print(" <td></td>")
  print(" </tr>")
print(" </tbody>")
print("</table>")

questTypes = QuestType.GetAll()
print("<h2>Quest Creation</h2>")
print("<hr />")
print('<form action="/cgi-bin/quests.py" method="post">')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Title</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="title" class="form-control" placeholder="quest title" required>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Description</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="description" class="form-control" placeholder="quest description" required>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Type</label>')
print('    <div class="col-sm-3">')
print('      <select class="form-control" name="type_id">')

for qt in questTypes:
  print('        <option value="%s" >%s</option>' % (qt.type_id, qt.name))

print('      </select>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">Reward</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="reward" value="0" class="form-control" placeholder="quest reward" required>')
print('    </div>')
print('  </div>')
print('  <div class="form-group row">')
print('    <label class="col-sm-2 col-form-label">XP</label>')
print('    <div class="col-sm-3">')
print('      <input type="text" name="xp" value="0" class="form-control" placeholder="quest xp" required>')
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
