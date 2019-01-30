#!/usr/bin/env python3

###########################################
# Class: CST-363
# Module 03, Project 01
# Authors: 
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: Character.py
#   Entry point for character specific information.
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

if 'character_id' in form and 'quest_id' in form:
  quest_id = int(form['quest_id'].value)
  character_id = int(form['character_id'].value)
  QuestLog.CompleteQuest(character_id, quest_id)

if 'character_id' in form and 'item_id' in form and 'action' in form:
  item_id = int(form['item_id'].value)
  character_id = int(form['character_id'].value)
  action = form['action'].value
  success = False
  if action == 'buy':
    success = Character.Buy(character_id, item_id)
  elif action == 'sell':
    success = Character.Sell(character_id, item_id)

  if success:
    alerts.append(('success', "You were able to %s this item" % action))
  else:
    alerts.append(('danger', "You were not able to %s this item" % action))

if 'character_id' in form:
    character = Character.Get(int(form['character_id'].value))

if form and not character:
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
print("<hr/><a href='./characters.py'>Go To Characters</a>")
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

# get all the quest a specific character has completed
# use function GetCharacterQuests(character_id)

quests = QuestLog.GetCharacterQuests(character.character_id)
print("<h1>My Quests</h1>")
print("<hr /><a href='./quests.py?character_id=%s'>Go To Quests</a>" % character.character_id)
print("<table class=\"table table-striped\" >")
print(" <tr>")
print(" <th>ID</th>")
print(" <th>Name</th>")
print(" <th>Description</th>")
print(" <th>Type</th>")
print(" <th>Experience</th>")
print(" <th>Reward</th>")
print(" <th></th>")
print(" </tr>")
print(" <tbody>")
for quest in quests:
  print(" <tr>")
  print(" <td>%s</td>" % quest.quest_id)
  print(" <td>%s</td>" % quest.title)
  print(" <td>%s</td>" % quest.description)
  print(" <td>%s</td>" % quest.type_name)
  print(" <td>%s</td>" % quest.xp)
  print(" <td>%s</td>" % quest.reward)
  if QuestLog.CanComplete(character.character_id, quest.quest_id):
    print(" <td><a href='./character.py?character_id=%s&quest_id=%s'>Complete</a></td>" % (character.character_id, quest.quest_id))
  else:
    print(" <td></td>")
  print(" </tr>")
print(" </tbody>")
print("</table>")


items = Item.GetAll()
inventory = Inventory.GetCharacterItems(character.character_id)
print("<h1>My Items</h1>")
print("<hr /><a href='./items.py?character_id=%s'>Go To Quests</a>" % character.character_id)
print("<table class=\"table table-striped\" >")
print(" <tr>")
print(" <th>ID</th>")
print(" <th>Name</th>")
print(" <th>Description</th>")
print(" <th>Type</th>")
print(" <th>Cost</th>")
print(" <th>Quantity</th>")
print(" <th></th>")
print(" </tr>")
print(" <tbody>")
for item in items:
  print(" <tr>")
  print(" <td>%s</td>" % item.item_id)
  print(" <td>%s</td>" % item.name)
  print(" <td>%s</td>" % item.description)
  print(" <td>%s</td>" % item.type_name)
  print(" <td>%s</td>" % item.cost)
  if item.item_id in inventory:
    print(" <td>%s</td>" % inventory[item.item_id].quantity)
  else:
    print(" <td>0</td>")
  print(" <td>")
  if item.item_id in inventory:
    print("<a href='./character.py?character_id=%s&item_id=%s&action=sell' class='btn btn-outline-danger btn-sm'>Sell</a>" % (character.character_id, item.item_id))
  if character.canBuy(item.cost):
    print("<a href='./character.py?character_id=%s&item_id=%s&action=buy' class='btn btn-primary btn-sm'>Buy</a>" % (character.character_id, item.item_id))
  print("  </td>")
  print(" </tr>")
print(" </tbody>")
print("</table>")

print("</div>")
print("</body></html>")
Cnx.Disconnect()