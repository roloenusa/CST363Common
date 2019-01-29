#!/usr/bin/env python3

###########################################
# Class: CST-363
# Module 03, Project 01
# Authors: 
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: Models.py
#   Defines all database models.
###########################################

# this file must be in the /cgi-bin/ directory of the server
import mysql.connector

class Cnx(object):
  cnx = False

  def Connect(u, p, d, h):
    if not Cnx.cnx:
      Cnx.cnx = mysql.connector.connect(user=u, password=p, database= d, host= h)

  def RunQuery(query, params):
    cursor = Cnx.cnx.cursor()
    cursor.execute(query, params)
    return cursor

  def Disconnect():
    if Cnx.cnx:
      Cnx.cnx.commit()
      Cnx.cnx.close()  # close the connection
      Cnx.cnx = False

class Item(object):
  get_all_sql = """SELECT i.item_id, i.type_id, type.name as type_name, i.name, i.description, i.cost 
    FROM items i
    JOIN item_types type USING (type_id)
  """

  get_by_id_sql = """SELECT i.item_id, i.type_id, type.name as type_name, i.name, i.description, i.cost 
    FROM items i
    JOIN item_types type USING (type_id)
    WHERE i.item_id = %s
  """

  get_by_name_sql = """SELECT i.item_id, i.type_id, type.name as type_name, i.name, i.description, i.cost 
    FROM items i
    JOIN item_types type USING (type_id)
    WHERE i.name = %s
  """

  create_sql = """INSERT INTO items (type_id, name, description, cost) 
  VALUES (%s, %s, %s, %s)
  """

  def __init__(self, item_id, type_id, type_name, name, description, cost):
    self.item_id = item_id
    self.type_id = type_id
    self.type_name = type_name
    self.name = name
    self.description = description
    self.cost = cost

  def GetAll():
    cursor = Cnx.RunQuery(Item.get_all_sql, ())
    rows = cursor.fetchall()
    records = []
    for r in rows:
      records.append(Item(*r))
    return records

  def Get(item_id):
    cursor = Cnx.RunQuery(Item.get_by_id_sql, (item_id,))
    row = cursor.fetchone()
    if not row:
      return None
    return Item(*row)

  def Create(type_id, name, description, cost):
    cursor = Cnx.RunQuery(Item.create_sql, (type_id, name, description, cost))
    item_id = cursor.lastrowid
    return Item.Get(item_id)

class ItemType(object):
  get_all_sql = "SELECT type_id, name FROM item_types"

  get_by_id_sql = "SELECT type_id, name FROM item_types WHERE item_id = %s"

  get_by_name_sql = "SELECT type_id, name FROM item_types WHERE name = %s"

  def __init__(self, type_id, type_name):
    self.type_id = type_id
    self.name = type_name

  def GetAll():
    cursor = Cnx.RunQuery(ItemType.get_all_sql, ())
    rows = cursor.fetchall()
    records = []
    for r in rows:
      records.append(ItemType(*r))
    return records

class Quest(object):
  get_all_sql = """SELECT q.quest_id, q.type_id, type.name as type_name, q.title, q.description, q.reward, q.xp
    FROM quests q
    JOIN quest_types type USING (type_id)
  """

  get_by_id_sql = """SELECT q.quest_id, q.type_id, type.name as type_name, q.title, q.description, q.reward, q.xp
    FROM quests q
    JOIN quest_types type USING (type_id)
    WHERE q.quest_id = %s
  """

  get_by_name_sql = """SELECT q.quest_id, q.type_id, type.name as type_name, q.title, q.description, q.reward, q.xp
    FROM quests q
    JOIN quest_types type USING (type_id)
    WHERE q.name = %s
  """

  create_sql = """INSERT INTO quests (type_id, title, description, reward, xp) 
  VALUES (%s, %s, %s, %s, %s)
  """

  def __init__(self, quest_id, type_id, type_name, title, description, reward, xp):
    self.quest_id = quest_id
    self.type_id = type_id
    self.type_name = type_name
    self.title = title
    self.description = description
    self.reward = reward
    self.xp = xp

  def GetAll():
    cursor = Cnx.RunQuery(Quest.get_all_sql, ())
    rows = cursor.fetchall()
    records = []
    for r in rows:
      records.append(Quest(*r))
    return records

  def Get(quest_id):
    cursor = Cnx.RunQuery(Quest.get_by_id_sql, (quest_id,))
    row = cursor.fetchone()
    if not row:
      return None
    return Quest(*row)

  def Create(type_id, title, description, reward = 0, xp = 0):
    cursor = Cnx.RunQuery(Quest.create_sql, (type_id, title, description, reward, xp))
    quest_id = cursor.lastrowid
    return Quest.Get(quest_id)

class QuestType(object):
  get_all_sql = "SELECT type_id, name FROM quest_types"

  def __init__(self, type_id, type_name):
    self.type_id = type_id
    self.name = type_name

  def GetAll():
    cursor = Cnx.RunQuery(QuestType.get_all_sql, ())
    rows = cursor.fetchall()
    records = []
    for r in rows:
      records.append(QuestType(*r))
    return records

class Character(object):
  get_all_sql = """SELECT c.character_id, k.class_id, k.name as class_name, c.name, c.level, c.experience, c.gold
    FROM characters c
    JOIN classes k USING (class_id)
  """

  get_by_id_sql = """SELECT c.character_id, c.class_id, k.name as class_name, c.name, c.level, c.experience, c.gold
    FROM characters c
    JOIN classes k USING (class_id)
    WHERE c.character_id = %s
  """

  get_by_name_sql = """SELECT c.character_id, c.class_id, k.name as class_name, c.name, c.level, c.experience, c.gold
    FROM characters c
    JOIN classes k USING (class_id)
    WHERE c.character_name = %s
  """

  create_sql = """INSERT INTO characters (class_id, name, level, experience, gold) 
  VALUES (%s, %s, %s, %s, %s)
  """

  complete_sql = """UPDATE characters SET gold = gold + %s, experience = experience + %s
  WHERE character_id = %s
  """

  award_sql = """UPDATE characters SET gold = gold + %s
  WHERE character_id = %s and gold + %s >= 0
  """

  def __init__(self, character_id, class_id, class_name, name, level, experience, gold):
    self.character_id = character_id
    self.class_id = class_id
    self.class_name = class_name
    self.name = name
    self.level = level
    self.experience = experience
    self.gold = gold

  def Create(class_id, name, level, experience, gold):
    cursor = Cnx.RunQuery(Character.create_sql, (class_id, name, level, experience, gold))
    character_id = cursor.lastrowid
    return Character.Get(character_id)
  
  def Get(character_id):
    cursor = Cnx.RunQuery(Character.get_by_id_sql, (character_id,))
    row = cursor.fetchone()
    if not row:
      return None
    return Character(*row)

  def GetAll():
    cursor = Cnx.RunQuery(Character.get_all_sql, ())
    rows = cursor.fetchall()
    records = []
    for r in rows:
      records.append(Character(*r))
    return records
  
  def CompleteQuest(character_id, quest_id):
    quest = Quest.Get(quest_id)
    Cnx.RunQuery(Character.complete_sql, (quest.reward, quest.xp, character_id))

  def Award(character_id, delta):
    cursor = Cnx.RunQuery(Character.award_sql, (delta, character_id, delta))
    return cursor.rowcount

  def canBuy(self, value):
    return self.gold >= value

  def Buy(character_id, item_id):
    item = Item.Get(item_id)
    awarded = Character.Award(character_id, -item.cost)
    if awarded:
      return Inventory.Award(character_id, item_id, 1)

  def Sell(character_id, item_id):
    item = Item.Get(item_id)
    awarded = Inventory.Award(character_id, item_id, -1)
    if awarded:
      return Character.Award(character_id, item.cost)
      

class Klass(object):
  get_all_sql = "SELECT class_id, name FROM classes"

  def __init__(self, class_id, name):
    self.class_id = class_id
    self.name = name

  def GetAll():
    cursor = Cnx.RunQuery(Klass.get_all_sql, ())
    rows = cursor.fetchall()
    records = []
    for r in rows:
      records.append(Klass(*r))
    return records

class QuestLog(object):

  get_by_character_id_sql = """SELECT q.quest_id, q.type_id, type.name as type_name, q.title, q.description, q.reward, q.xp
    FROM quests q
    JOIN quest_log ql USING (quest_id)
    JOIN quest_types type USING (type_id)
    WHERE ql.character_id = %s
  """

  get_by_id_sql = """SELECT ql.character_id, ql.quest_id, ql.created, ql.completed
    FROM quest_log ql
    WHERE ql.quest_id = %s
  """

  create_sql = """INSERT INTO quest_log (character_id, quest_id) 
  VALUES (%s, %s)
  """

  complete_sql = """UPDATE quest_log SET completed = NOW()
  WHERE character_id = %s and quest_id = %s and completed IS NULL
  """

  can_complete_sql = """SELECT quest_id
  FROM quest_log
  WHERE character_id = %s and quest_id = %s and completed IS NULL
  """

  def __init__(self, ql_id, char_id, quest_id, created, completed):
    self.quest_log_id = class_id
    self.character_id = char_id
    self.quest_id = quest_id
    self.created = created
    self.completed = completed

  def GetCharacterQuests(character_id):
    cursor = Cnx.RunQuery(QuestLog.get_by_character_id_sql, (character_id,))
    rows = cursor.fetchall()
    records = []
    for r in rows:
      records.append(Quest(*r))
    return records
  
  def Get(quest_log_id):
    cursor = Cnx.RunQuery(QuestLog.get_by_id_sql, (quest_log_id,))
    row = cursor.fetchone()
    if not row:
      return None
    return QuestLog(*row)
  
  def CanAdd(character_id, quest_id):
    if character_id and quest_id:
      return not QuestLog.CanComplete(character_id, quest_id)
    return False

  def CanComplete(character_id, quest_id):
    if character_id and quest_id:
      cursor = Cnx.RunQuery(QuestLog.can_complete_sql, (character_id, quest_id))
      return cursor.fetchone()
    return False
  
  def AddQuest(character_id, quest_id):
    if QuestLog.CanAdd(character_id, quest_id):
      cursor = Cnx.RunQuery(QuestLog.create_sql, (character_id, quest_id))
      return cursor.lastrowid
    return False

  def CompleteQuest(character_id, quest_id):
    if QuestLog.CanComplete(character_id, quest_id):
      Cnx.RunQuery(QuestLog.complete_sql, (character_id, quest_id))
      Character.CompleteQuest(character_id, quest_id)


class Inventory(object):
  get_all_by_character_id_sql = """SELECT inv.item_id, inv.character_id, inv.quantity
    FROM  inventory inv
    WHERE inv.character_id = %s AND inv.quantity > 0
  """

  get_by_id_sql = """SELECT inv.item_id, inv.character_id, inv.quantity
    FROM  inventory inv
    WHERE inv.character_id = %s AND inv.item_id = %s
  """

  create_sql = """INSERT INTO inventory (character_id, item_id) 
  VALUES (%s, %s)
  """

  award_sql = """UPDATE inventory SET quantity = quantity + %s
  WHERE character_id = %s and item_id = %s and quantity + %s >= 0
  """

  def __init__(self, item_id, character_id, quantity):
    self.item_id = item_id
    self.character_id = character_id
    self.quantity = quantity

  def Create(character_id, item_id):
    cursor = Cnx.RunQuery(Inventory.create_sql, (character_id, item_id))
    item_id = cursor.lastrowid
    return Inventory.Get(character_id, item_id)

  def Get(character_id, item_id):
    cursor = Cnx.RunQuery(Inventory.get_by_id_sql, (character_id, item_id))
    row = cursor.fetchone()
    if not row:
      return None
    return Inventory(*row)

  def GetCharacterItems(character_id):
    cursor = Cnx.RunQuery(Inventory.get_all_by_character_id_sql, (character_id,))
    rows = cursor.fetchall()
    records = {}
    for r in rows:
      inv = Inventory(*r)
      records[inv.item_id] = inv
    return records

  def Award(character_id, item_id, delta):
    inv = Inventory.Get(character_id, item_id)
    if not inv:
      Inventory.Create(character_id, item_id)
    cursor = Cnx.RunQuery(Inventory.award_sql, (delta, character_id, item_id, delta))
    return cursor.rowcount
