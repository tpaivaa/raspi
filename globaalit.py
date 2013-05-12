!/usr/bin/python
# -*- coding: utf-8 -*-
import lampo as l

gpio4 = 0
gpio17 = 0
gpio18 = 0
gpio21 = 0
gpio22 = 0
gpio23 = 0
gpio24 = 0
gpio25 = 0
# Ajustable?tarve variaabelit
global attackkhh
global attackolohuone
global attackmakuuhuone
global attacksauna
global attackakWcLattia
global attackKeittio
attackKeittio = False
attackakWcLattia = False
attacksauna = False
attackmakuuhuone = False
attackolohuone = False
attackkhh = False

# Muut variaabelit
global initState
initState = False

global olohuone
olohuone = l.latestLampo('olohuone')
global makuuhuone
makuuhuone= l.latestLampo('makuuhuone')
global ulko
ulko = l.latestLampo('ulkoE')
global khh
khh = l.latestLampo('khh')
global sauna
sauna = l.latestLampo('sauna')
global akWcLattia
akWcLattia = l.latestLampo('akWcLattia')
global puukattila
kattila = l.latestLampo('puukattila')
global kattilaCold
kattilaCold = l.latestLampo('kattilaCold')
global kattilaHot
kattilaHot = l.latestLampo('kattilaHot')
global varaajaDown
varaajaDown = l.latestLampo('varaajaDown')
global varaajaUp
varaajaUp = l.latestLampo('varaajaUp')
global keittio
keittio = l.latestLampo('keittio')
global greeHot
greeHot = l.latestLampo('greeHot')
global patteriL
patteriL = l.latestLampo('patteriL')
global maalamp?o
maalampo = l.latestLampo('maalampo')
global ulkosauna
ulkosauna = l.latestLampo('ulkosauna')
global LLlahto
LLlahto = l.latestLampo('LLlahto')


# Säätö limiitit
akWcLattiaLowLimit = 29
akWcLattiaHighLimit = 34
olohuoneLowLimit = 22
olohuoneHighLimit = 22
saunaLowLimit = 20
saunaHighLimit = 21
khhLowLimit = 21
khhHighLimit = 23
makuuhuoneLowLimit = 19
makuuhuoneHighLimit = 19
keittioLowLimit = 31
keittioHighLimit = 34

# 