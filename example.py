from bmk20 import bmk20

heizung = bmk20()
response = heizung.getData("192.168.0.204")

print(heizung.daten.betrieb)