# -*- coding: utf-8 -*-
import requests

class bmk20Data:
    def __init__(self):
        self.betrieb             = ""
        self.kesseltemperatur    = 0.0
        self.abgastemperatur     = 0.0
        self.aussentemperatur    = 0.0
        self.pufferladung        = 0.0
        self.pufferoben          = 0.0
        self.puffermitte         = 0.0
        self.pufferunten         = 0.0
        self.kesselladepumpe     = 0.0
        self.saugzug             = 0.0
        self.primaerluft         = 0.0
        self.sekundaerluft       = 0.0
        self.hk1vorlaufsoll      = 0.0
        self.hk1vorlaufist       = 0.0
        self.hk1pumpe            = ""
        self.hk2vorlaufsoll      = 0.0
        self.hk2vorlaufist       = 0.0
        self.hk2pumpe            = ""
        self.programm            = ""
        self.hk1status           = ""
        self.hk2status           = ""
        self.stoerung_1          = ""
        self.stoerung_2          = ""
        self.swversion           = ""
        self.betriebszeit        = 0.0
        self.servicezeit         = 0.0
        self.co2                 = 0.0

class bmk20:
    def __init__(self):
        self.daten = bmk20Data()
    
    def getData(self, ip):
        try:
            url = "http://"+ip+"/daqdata.cgi"
            response = requests.get(url)
            
            if response.status_code == 200:
                databmk = response.text.split("\n")
   
                self.daten.betrieb             = databmk[1]
                self.daten.kesseltemperatur    = float(databmk[2])
                self.daten.abgastemperatur     = 0 ##float(databmk[4])
                self.daten.aussentemperatur    = float(databmk[5])
                self.daten.pufferladung        = float(databmk[6])
                self.daten.pufferoben          = float(databmk[7])
                self.daten.puffermitte         = float(databmk[8])
                self.daten.pufferunten         = float(databmk[9])
                self.daten.kesselladepumpe     = float(databmk[10])
                self.daten.saugzug             = float(databmk[11])
                self.daten.primaerluft         = float(databmk[12])
                self.daten.sekundaerluft       = float(databmk[13])
                self.daten.hk1vorlaufsoll      = 0 ##float(databmk[34])
                self.daten.hk1vorlaufist       = float(databmk[35])
                self.daten.hk1pumpe            = databmk[36]
                self.daten.hk2vorlaufsoll      = 0 ##float(databmk[39])
                self.daten.hk2vorlaufist       = float(databmk[40])
                self.daten.hk2pumpe            = databmk[41]
                self.daten.programm            = databmk[69]
                self.daten.hk1status           = databmk[71]
                self.daten.hk2status           = databmk[72]
                self.daten.stoerung_1          = databmk[79]
                self.daten.stoerung_2          = databmk[80]
                self.daten.swversion           = databmk[82]
                self.daten.betriebszeit        = float(databmk[83])
                self.daten.servicezeit         = float(databmk[84])
                self.daten.co2                 = float(databmk[14])
            else:
                pass
            
            return response
            
        except Exception as e:
            return e
