from bmk20 import bmk20

HOST_IP = "192.168.0.204"

heizung = bmk20(HOST_IP)
response = heizung.getData()

if 200 == response.status_code:
    print(heizung.daten.betrieb)
else:
    print(response)
