#!/usr/bin/python
# -*- coding: utf-8 -*-
import lampo as l
import saada as s
import time
import syslog
gpio4 = 0
gpio17 = 0
gpio18 = 0
gpio21 = 0
gpio22 = 0
gpio23 = 0
gpio24 = 0
gpio25 = 0
global initState 
global olohuone
global makuuhuone
global attackkhh
global attackolohuone
global attackmakuuhuone
global attacksauna
global attackakWcLattia

initState = False

while 1:
    syslog.syslog('Time to wake up')
    try:
        syslog.syslog(str(initState))
        if initState != 1:
            initState = s.initialize()
            syslog.syslog('initialisoinnissa')
            gpio4 = l.getRele('4')
            gpio17 = l.getRele('17')
            gpio18 = l.getRele('18')
            gpio21 = l.getRele('21')
            gpio22 = l.getRele('22')
            gpio23 = l.getRele('23') 
            gpio24 = l.getRele('24')
            gpio25 = l.getRele('25')
        else:
            syslog.syslog('Ei tarvii alustaa')
    except Exception, e:
        syslog.syslog('alustus ei onnannu')
        syslog.syslog(str(e))
        pass
    aika = l.getAikaNow()
    syslog.syslog(aika)
    
    try:
        try:
            khh = l.latestLampo('khh')
            olohuone = l.latestLampo('olohuone')
            sauna = l.latestLampo('sauna')
            akWcLattia = l.latestLampo('akWcLattia')
            ulko = l.latestLampo('ulkoE')
            kattila = l.latestLampo('varaajaDown')
            kattilaCold = l.latestLampo('kattilaCold')
            kattilaHot = l.latestLampo('kattilaHot')
            varaajaDown = l.latestLampo('varaajaDown')
            varaajaUp = l.latestLampo('varaajaUp')
            makuuhuone = l.latestLampo('makuuhuone')
            keittio = l.latestLampo('keittio')
        except Exception, e:
            khh = 0
            olohuone = 0
            sauna = 0
            akWcLattia = 0
            ulko = 0
            syslog.syslog('******** Virhe initialisoinnissa: *******')
            syslog.syslog(e)

        # Seems its Wintertime and cold! different limits   
        if ulko > 10 and ulko < 15:
            akWcLattiaLowLimit = 29
            akWcLattiaHighLimit = 30
            olohuoneLowLimit = 20
            olohuoneHighLimit = 21
            saunaLowLimit = 19
            saunaHighLimit = 20
            khhLowLimit = 20
            khhHighLimit = 20
            makuuhuoneLowLimit = 19
            makuuhuoneHighLimit = 19
            keittioLowLimit = 31
            keittioHighLimit = 31

        if ulko < 10:
            akWcLattiaLowLimit = 29
            akWcLattiaHighLimit = 34
            olohuoneLowLimit = 22
            olohuoneHighLimit = 23
            saunaLowLimit = 20
            saunaHighLimit = 21
            khhLowLimit = 21
            khhHighLimit = 23
            makuuhuoneLowLimit = 19
            makuuhuoneHighLimit = 19
            keittioLowLimit = 31
            keittioHighLimit = 34

        else:
            akWcLattiaLowLimit = 25
            akWcLattiaHighLimit = 30
            olohuoneLowLimit = 21
            olohuoneHighLimit = 21
            saunaLowLimit = 19
            saunaHighLimit = 19
            khhLowLimit = 20
            khhHighLimit = 21
            makuuhuoneLowLimit = 19
            makuuhuoneHighLimit = 22
            keittioLowLimit = 19
            keittioHighLimit = 25
            

        #Determine if heating needed temp limits lower than lowerlimits
        attackkhh = khhLowLimit > khh
        attackolohuone = olohuoneLowLimit > olohuone
        attackmakuuhuone = makuuhuoneLowLimit > makuuhuone
        attacksauna = saunaLowLimit > sauna
        attackakWcLattia = akWcLattiaLowLimit > akWcLattia
        attackKeittio = keittioLowLimit > keittio
        varaajaCold = varaajaDown < 33

        
        
        if keittio < keittioLowLimit  and keittio !=0:
            if l.getRele('18') == 0:
                s.setState(3, 'LOW')
                gpio18 = l.getRele('18')
        elif keittio > keittioHighLimit and keittio != 0:
            if l.getRele('18'):
                s.setState(3, 'HIGH')
                gpio18 = l.getRele('18')

        if akWcLattia < akWcLattiaLowLimit and akWcLattia != 0 and khh < 24:
            syslog.syslog('Toilet floor Gold and khh is < 24')
            if l.getRele('17') == 0:
                s.setState(2, 'LOW')
                gpio17 = l.getRele('17')
        elif akWcLattia > akWcLattiaHighLimit and akWcLattia != 0 and khh > 23:
            syslog.syslog('Toilet Floor Warm and khh is > 23')
            if l.getRele('17') == 1:
                s.setState(2, 'HIGH')
                gpio17 = l.getRele('17')
        else:
            syslog.syslog('Toilet floor Comfortable')

        if sauna < saunaLowLimit and sauna != 0:
            syslog.syslog('Sauna cold')
            if l.getRele('4') == 0:
                s.setState(1, 'LOW')
                gpio4 = l.getRele('4')
        if sauna > saunaHighLimit and sauna != 0:
            syslog.syslog('Sauna warm')
            if  l.getRele('4') == 1:
                s.setState(1, 'HIGH')
                gpio4 = l.getRele('4')
        #Olohuone cold open valve
        if attackolohuone:
            syslog.syslog('Olohuone cold')
            if l.getRele('24') == 1:
                s.setState(7, 'HIGH')
                gpio24 = l.getRele('24')
        else:
            syslog.syslog('Olohuone warm')
            if l.getRele('24') == 0:
                s.setState(7, 'LOW')
                gpio24 = l.getRele('24')


        #If somewhere is heating needed activate Pumps SET Every cotrol above this ****!!!!****   
        if (gpio4 or gpio17 or gpio18 or gpio21) and (ulko < 14):
            if gpio22 == 0:
                s.setState(5, 'LOW')
                gpio22 = l.getRele('22')
                syslog.syslog('Floor Pump On')
            if gpio23 == 0:
                s.setState(6, 'LOW')
                gpio23 = l.getRele('23')
                syslog.syslog('Main pump On')

        #If everywhere warm de-activate Pumps Set everything above this !!!*****************!!!!      
        elif (gpio4 and gpio17 and gpio18 and gpio21) == 0:
            if gpio22 == 1:
                s.setState(5, 'HIGH')
                gpio22 = l.getRele('22')
                syslog.syslog('Floor Pump Off')
            if gpio23 == 1:    
                s.setState(6, 'HIGH')
                gpio23 = l.getRele('23')
                syslog.syslog('Main pump Off')
        #Attack to help heating if needed
        #Heating needed if outtemp is less than 14 and  room temperatures lower than limits
        if (attackkhh or attackolohuone or attackmakuuhuone or attacksauna or attackakWcLattia) and ulko < 14 and varaajaCold:
            syslog.syslog('Attack tarvetta')
            s.setState(8, 'LOW')
            gpio25 = l.getRele('25')
            syslog.syslog('Attack On')
        else:
            if l.getRele('25') == 0:
                syslog.syslog('Attack taitaa olla Off')
            else:
                syslog.syslog('Attack tarvetta ei ole')
                s.setState(8, 'HIGH')
                gpio25 = l.getRele('25')
                syslog.syslog('Attack Off')
        if (attackkhh or attackolohuone or attackmakuuhuone or attacksauna or attackakWcLattia) != 1 and ulko > 14:
            syslog.syslog('Attack tarvetta ei ole')
            s.setState(8, 'HIGH')
            gpio25 = l.getRele('25')
            syslog.syslog('Attack Off')
        else:
            if l.getRele('25') == 0:
                syslog.syslog('Attack taitaa olla jo Off')

    except Exception, e:
        syslog.syslog('kesken Meno')
        syslog.syslog(str(e))
        pass

    syslog.syslog('Tarve')

    syslog.syslog('Keittiö    = ' + str(attackKeittio))
    syslog.syslog('Khh        = ' + str(attackkhh))
    syslog.syslog('Olohuone   = ' + str(attackolohuone))
    syslog.syslog('Makuuhuone = ' + str(attackmakuuhuone))
    syslog.syslog('Sauna      = ' + str(attacksauna))
    syslog.syslog('Varaaja alalämpö = ' + str(kattila))
    syslog.syslog('WC Lattia  = ' + str(attackakWcLattia))
    syslog.syslog('Saadetty')
    syslog.syslog('GPIO4 Pesuhuone lattia = ' + str(gpio4))
    syslog.syslog('GPIO17 khh Lattia      = ' + str(gpio17))
    syslog.syslog('GPIO18 Keittio Lattia  = ' + str(gpio18))
    syslog.syslog('GPIO21 ykAula          = ' + str(gpio21))
    syslog.syslog('GPIO22 PääPumppu       = ' + str(gpio22))
    syslog.syslog('GPIO23 ll Pumppu       = ' + str(gpio23))
    syslog.syslog('GPIO24 Patteri Kierto  = ' + str(gpio24) + ' jos 0 on kierto päällä')
    syslog.syslog('GPIO25 Attack          = ' + str(gpio25))
    syslog.syslog('Olohuone: ' + str(olohuone))
    syslog.syslog('Olohuone LowLimit: ' + str(olohuoneLowLimit))
    syslog.syslog('Khh ' + str(khh))
    syslog.syslog('Ulkona ' + str(ulko))
    syslog.syslog('Sauna ' + str(sauna))
    syslog.syslog('Keittiö lattia ' + str(keittio))
    syslog.syslog('Khh Lattia ' + str(akWcLattia))
    syslog.syslog('varaajaDown ' + str(varaajaDown))
    syslog.syslog('Time to Sleep 10 minutes')

    time.sleep(600)
