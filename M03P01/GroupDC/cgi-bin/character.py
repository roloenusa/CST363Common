#!/usr/bin/env python3

###########################################
# Class: CST-363
# Module 03, Project 01
# Authors: 
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: Character.py
#   Entry point for character creation and retrival.
###########################################

# this file must be in the /cgi-bin/ directory of the server
import cgitb
import cgi
from models import *

Cnx.Connect('gameadmin', 'sesame', 'gamedb', 'localhost')

cgitb.enable()
form = cgi.FieldStorage()

alerts = []
character = False

if form:
  if 'character_id' in form:
    character = Character.Get(int(form['character_id'].value))
  else: 
    class_id = int(form["class_id"].value.strip())
    name = form["name"].value.strip()
    level = form["level"].value.strip()
    experience = int(form["experience"].value.strip())
    gold = int(form["gold"].value.strip())
    try:
      character = Character.Create(class_id = class_id, name = name, level = level, experience = experience, gold = gold)
    except Exception as e:
      alerts.append(('danger', e))

if not character:
    alerts.append(('danger', 'No character found'))

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
print(" </tr>")
print(" <tbody>")
print(" <tr>")
print(" <td>%s</td>" % character.character_id)
print(" <td>%s</td>" % character.name)
print(" <td>%s</td>" % character.class_name)
print(" <td>%s</td>" % character.level)
print(" <td>%s</td>" % character.experience)
print(" <td>%s</td>" % character.gold)
print(" </tr>")
print(" </tbody>")
print("</table>")
print("</div>")
#print("</body>")
print("</body></html>")

# get all the quest a specific character has completed
# use function GetCharacterQuests(character_id)

quests = QuestLog.GetCharacterQuests(character.character_id)
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

Cnx.Disconnect()