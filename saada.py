# -*- coding: utf-8 -*-
import os
import time
import syslog
import MySQLdb
import RPi.GPIO as GPIO
from datetime import datetime,timedelta
from time import strftime,localtime

'''rele1 =  Pesuhuone lattia = GPIO4,
   rele2 =  Khhlattia = GPIO17,
   rele3 =  Keittio = GPIO18,
   rele4 =  ykAula = GPIO21,
   rele5 =  Pumppu = GPIO22,
   rele6 =  llPumppu GPIO23,
   rele7 =  Patteri valve = GPIO24
   rele8 =  Attack Heatinng = GPIO25'''



def initialize():
	releet = (4,17,18,21,22,23,24,25)
	GPIO.setmode(GPIO.BCM)
	# Open database connection
	db = MySQLdb.connect(host="sweb",db="lampotilat",read_default_file='./.connect.mysql',use_unicode = True)
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	for n in releet:
		GPIO.setup(n, GPIO.OUT)
		GPIO.output(n, GPIO.HIGH)
		sql = "UPDATE reletilat SET state = '%s' WHERE gpio = '%s';" % ('0', n)
		try:
			# Execute the SQL command
			cursor.execute(sql)
			# Commit your changes in the database
			db.commit()
		except:
			# Rollback in case there is any error
			db.rollback()
		
	initialState = True
	# disconnect from server
	db.close()
	return initialState

def setState(rele, tila):
	# Open database connection
	db = MySQLdb.connect(host="sweb",db="lampotilat",read_default_file='./.connect.mysql',use_unicode = True)
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	if rele == 1:
	   releu = 4
	if rele == 2:
	   releu = 17
	if rele == 3:
	   releu = 18
	if rele == 4:
	   releu = 21
	if rele == 5:
	   releu = 22
	if rele == 6:
	   releu = 23
	if rele == 7:
	   releu = 24
	if rele == 8:
	   releu = 25

	if tila == 'HIGH':
		tila = 0
		GPIO.output(releu, GPIO.HIGH)
		sql = "UPDATE reletilat SET state = '%s' WHERE gpio = '%s';" % (tila, releu)
		try:
			# Execute the SQL command
			cursor.execute(sql)
			# Commit your changes in the database
			db.commit()
		except:
			# Rollback in case there is any error
			db.rollback()
		
	if tila == 'LOW':
		tila = 1
		GPIO.output(releu, GPIO.LOW)
		sql = "UPDATE reletilat SET state = '%s' WHERE gpio = '%s';" % (tila, releu)
		try:
			# Execute the SQL command
			cursor.execute(sql)
			# Commit your changes in the database
			db.commit()
		except:
			# Rollback in case there is any error
			db.rollback()
	# disconnect from server
	db.close()
