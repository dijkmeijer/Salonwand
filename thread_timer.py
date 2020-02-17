#!/usr/bin/python

from threading import Timer
import rpyc
import json
import os

conn={}

address=[
        "192.168.2.61",
        "192.168.2.62",
        "192.168.2.63",
        "192.168.2.64",
        "192.168.2.65",
        "192.168.2.66",
        "192.168.2.67"]
        


def hello(naam, adres):
    if adres == "192.168.2.61":
	os.system("omxplayer  --aspect-mode fill -b media/"+naam)
    else:
        try:
            conn = rpyc.classic.connect(adres)
            print "start "+naam+" op " +adres
            conn.modules.os.system("omxplayer --aspect-mode fill -b "+naam)
            
        except:
            print "kan geen verbinding maken met " + adres

t = {}

json_data=open("/home/pi/salonwand/public/Content.json").read()

data = json.loads(json_data)

i =0
for film in data:
    naam = film["name"]
    if film["track" ] < 8:
        print naam
        Timer(film["begin"], hello, [film["name"],address[film["track"]-1]]).start()

    
    
