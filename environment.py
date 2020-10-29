#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

def get_humidity():
    return sense.get_humidity()

def get_temp():
    return sense.get_temperature()

def get_temp_from_humidity():
    return sense.get_temperature_from_humidity()

def get_temp_from_pressure():
    return sense.get_temperature_from_pressure()

def get_pressure():
    return sense.get_pressure()

