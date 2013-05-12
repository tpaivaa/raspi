#!/usr/bin/python
# -*- coding: utf-8 -*-
import syslog
import globaalit as g

def logaa():
    syslog.syslog('Tarve')
    syslog.syslog('Keittiö    = ' + str(g.attackKeittio))
    syslog.syslog('Khh        = ' + str(g.attackkhh))
    syslog.syslog('Olohuone   = ' + str(g.attackolohuone))
    syslog.syslog('Makuuhuone = ' + str(g.attackmakuuhuone))
    syslog.syslog('Sauna      = ' + str(g.attacksauna))
    syslog.syslog('WC Lattia  = ' + str(g.attackakWcLattia))
    syslog.syslog('Saadetty')
    syslog.syslog('GPIO4 Pesuhuone lattia = ' + str(g.gpio4))
    syslog.syslog('GPIO17 khh Lattia      = ' + str(g.gpio17))
    syslog.syslog('GPIO18 Keittio Lattia  = ' + str(g.gpio18))
    syslog.syslog('GPIO21 ykAula          = ' + str(g.gpio21))
    syslog.syslog('GPIO22 PääPumppu       = ' + str(g.gpio22))
    syslog.syslog('GPIO23 ll Pumppu       = ' + str(g.gpio23))
    syslog.syslog('GPIO24 Patteri Kierto  = ' + str(g.gpio24))
    syslog.syslog('GPIO25 Attack          = ' + str(g.gpio25))
    syslog.syslog('Olohuone: ' + str(g.olohuone))
    syslog.syslog('Olohuone LowLimit: ' + str(g.olohuoneLowLimit))
    syslog.syslog('Khh ' + str(g.khh))
    syslog.syslog('Sauna ' + str(g.sauna))
    syslog.syslog('Keittiö lattia ' + str(g.keittio))
    syslog.syslog('Khh Lattia ' + str(g.akWcLattia))
    syslog.syslog('varaajaDown ' + str(g.varaajaDown))
    syslog.syslog('Time to Sleep 10 minutes')
    print 'Tehty'