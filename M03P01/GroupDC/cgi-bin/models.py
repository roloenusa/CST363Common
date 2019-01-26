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
    print(row)
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
