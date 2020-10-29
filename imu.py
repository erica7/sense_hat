#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

# sense.set_imu_config(True, True, True)

# north = sense.get_compass()
# print("North: %s" % north)

accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

raw = sense.get_accelerometer_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))



