#coding:utf-8
from w1thermsensor import W1ThermSensor

#センサーの取得
sensor = W1ThermSensor()
#温度の取得(摂氏)
celsius = sensor.get_temperature()

print("室温: {0:.2f}".format(celsius))
