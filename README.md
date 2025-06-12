# guntamatic_bmk20
class for guntamatic heating bmk


The data of the heating is:
http://192.168.0.204/daqdata.cgi

The description of the data is on:
http://192.168.0.204/daqdesc.cgi

Access to web server
http://192.168.0.204/demo/index.htm


i created this class and more to read ofer ethernet, analys the data and inform my self with email.

On my Raspberry Pi, this is called every 5 min.

I also save the state and calculate some data and check:
    over temperature -> email
    check startup -> by an abourt email
    all data to mysql, but maybe influx is better
    check buffer level -> three times email
    error message -> email

this code i will add, but before i must refactor it.