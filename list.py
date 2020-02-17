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
    if adres == 1:
	 if os.system("ls media/"+naam+" > /dev/null") == 512:
            print "bestand " +naam+" niet op "+address[adres-1]
       
    else:
        try:
            conn = rpyc.classic.connect(address[adres-1])
            if conn.modules.os.system("ls "+naam) == 512:
		print "bestand " +naam+" niet op "+address[adres-1] 
            conn.close()
        except:
            print "kan geen verbinding maken met " + address[adres-1]

t = {}

json_data=open("/home/pi/salonwand/public/Content.json").read()

data = json.loads(json_data)

i =0

for film in data:
    if film["track"] < 8:
        hello(film["name"], film["track"])
    


    
    
