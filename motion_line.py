# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import urllib
import urllib2

from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

#5秒待機
sleep(5)

try:
        while True:        
            a = GPIO.input(18)
            sleep(1)
            if a == 1:
                break

#動作を検知したらLINENotifyにて通知する                    
        params = {"message":"動作を検知しました"}
       	params = urllib.urlencode(params)
            
        req = urllib2.Request("https://notify-api.line.me/api/notify")
        req.add_header("Authorization","Bearer " + "LINE Notify Token")
        req.add_data(params)

        res = urllib2.urlopen(req)

except KeyboardInterrupt:
        pass

GPIO.cleanup()
