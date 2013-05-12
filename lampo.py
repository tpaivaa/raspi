# -*- coding: utf-8 -*-
import os
import time
import syslog
import MySQLdb
from datetime import datetime,timedelta
from time import strftime,localtime

#return time 11 minutes before
def getAika():
    now = datetime.now() - timedelta(minutes=15) #past 11 minutes
    aika = now.strftime("%Y.%m.%d-%H:%M:%S")
    return aika
#return current time like half past twelve 1230
def getTime():
    now = datetime.now()
    aika = now.strftime("%H%M")
    return aika

#return current date monthday like first of november = 1101
def getDate():
    now = datetime.now()
    date = now.strftime("%m%d")
    return date

def getAikaNow():
    now = datetime.now()
    aika = now.strftime("%Y.%m.%d-%H:%M:%S")
    return aika

def latestLampo(room):
	# Open database connection
	db = MySQLdb.connect("sweb","lampo","lampotilat","lampotilat",use_unicode = True)
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "SELECT celsius FROM lampotilat WHERE sensor = '%s' ORDER BY tKey DESC LIMIT 1" % (room)

	try:
		# Execute the SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any error
		db.rollback()
	ll = cursor.fetchone()
	db.close()
	return int(ll[0])
    
def getRele(gpio):
	# Open database connection
	db = MySQLdb.connect("sweb","lampo","lampotilat","lampotilat",use_unicode = True)
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	sql = "SELECT state FROM reletilat WHERE gpio = '%s'" % (gpio)
	try:
		# Execute the SQL command
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any error
		db.rollback()
	r = cursor.fetchone()
	db.close()
	return int(r[0])
