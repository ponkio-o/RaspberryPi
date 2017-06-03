# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

#3秒待機
sleep(3)

#動作を検知したら1を表示(それ以外は0)
try:
        while True:        
                print GPIO.input(18)
                sleep(1)

except KeyboardInterrupt:
        pass

GPIO.cleanup()
